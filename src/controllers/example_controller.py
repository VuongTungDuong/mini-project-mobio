#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from mobio.libs.logging import MobioLogging
from mobio.libs.validator import Required, InstanceOf
from mobio.sdks.admin import MobioAdminSDK
from mobio.sdks.base.controllers import BaseController


class ExampleController(BaseController):
    def _validate_create_item(self, data):
        rules = {
            'name': [Required, InstanceOf(str)]
        }

        BaseController.abort_if_validate_error(rules, data)

    def create_item(self):
        body = request.json
        MobioLogging().info('example_controller::create_item():request.body: %s' % body)

        self._validate_create_item(body)

        merchant_id = MobioAdminSDK().get_value_from_token('merchant_id')
        user_id = MobioAdminSDK().get_value_from_token('id')

        # TODO
