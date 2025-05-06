#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from mobio.sdks.base.configs import ApplicationConfig


class joApplicationConfig(ApplicationConfig):
    NAME = "jo"

    ApplicationConfig.WORKING_DIR = str(os.environ.get("JO_HOME"))
    ApplicationConfig.RESOURCE_DIR = os.path.join(
        ApplicationConfig.WORKING_DIR, "resources"
    )
    ApplicationConfig.CONFIG_DIR = os.path.join(
        ApplicationConfig.RESOURCE_DIR, "configs"
    )
    ApplicationConfig.LANG_DIR = os.path.join(ApplicationConfig.RESOURCE_DIR, "lang")

    ApplicationConfig.CONFIG_FILE_PATH = os.path.join(
        ApplicationConfig.CONFIG_DIR, "jo.conf"
    )
    ApplicationConfig.LOG_CONFIG_FILE_PATH = os.path.join(
        ApplicationConfig.CONFIG_DIR, "logging.conf"
    )
    ApplicationConfig.LOG_FILE_PATH = os.path.join(
        ApplicationConfig.APPLICATION_LOGS_DIR
    )

    JO_FOLDER_NAME = os.environ.get("JO_FOLDER_NAME")

    ADMIN_HOST = os.environ.get("ADMIN_HOST", "")


class RedisConfig:
    REDIS_URI = os.environ.get("REDIS_URI", "redis://redis-server:6379/0")
