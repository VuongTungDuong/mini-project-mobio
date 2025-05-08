import re
from typing import TypedDict

from flask import Blueprint, jsonify, request
from mobio.libs.validator import InstanceOf, Length, Required
from mobio.sdks.base.controllers import BaseController

user_bp = Blueprint("user", __name__)


class UserMobioModel(TypedDict):
    id: int
    name: str
    password: str


@user_bp.route("/user/<int:user_id>", methods=["GET", "POST"])
class UserMobioController(BaseController):
    def get(self, user_id: int):
        # Logic to get user data
        request_data = request.args.get("data", "")

        response_data = request.args.get("response", "")
        if request_data:
            try:
                _ = re.search(r"data=(.*)", request_data).group(1)
                response_data = re.search(r"response=(.*)", response_data).group(1)
            except AttributeError:
                return jsonify({"error": "Invalid data format"}), 400

        return jsonify({"message": "Get user data"}), 200

    def post(self, user_id: int):
        user_data = request.json
        self._validate_create_item(user_data)
        return jsonify({"message": "User created", "data": user_data}), 201

    def _validate_create_item(self, data):
        rules = {
            "id": [
                Required,
                InstanceOf(int),
            ],
            "name": [Required, InstanceOf(str), Length(min=1, max=150)],
        }

        BaseController.abort_if_validate_error(rules, data)


# user_bp.add_url_rule(
#     "/user/<int:user_id>", view_func=UserMobioController.as_view("user_controller")
# )
# user_bp.add_url_rule("/user", view_func=UserMobioController.as_view("user_controller"))
