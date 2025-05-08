#!/usr/bin/env python

from flask import request
from mobio.libs.logging import MobioLogging
from mobio.libs.validator import InstanceOf, Required
from mobio.sdks.admin import MobioAdminSDK
from mobio.sdks.base.controllers import BaseController


class ExampleController(BaseController):
    def _validate_create_item(self, data) -> None:
        rules = {"name": [Required, InstanceOf(str)]}

        BaseController.abort_if_validate_error(rules, data)

    def create_item(self):
        body = request.json
        MobioLogging().info(f"example_controller::create_item():request.body: {body}")

        self._validate_create_item(body)

        _ = MobioAdminSDK().get_value_from_token("merchant_id")
        _ = MobioAdminSDK().get_value_from_token("id")
        # TODO
