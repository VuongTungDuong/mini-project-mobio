from typing import Annotated

from flask import Blueprint, jsonify, request
from flask.views import MethodView
from mobio.libs.logging import MobioLogging
from pydantic import BaseModel, conint, conlist, constr

user_bp = Blueprint("user", __name__)


class UserModel(BaseModel):
    id: Annotated[int, conint(gt=0, lt=1000000)]
    name: Annotated[str, constr(min_length=1, max_length=150)]
    password: Annotated[str, constr(min_length=1, max_length=100)]


class UserModelResponse(BaseModel):
    datas: Annotated[list, conlist(UserModel, min_length=1)]


class UserController(MethodView):
    def get(self, user_id: int):
        # Logic to get user data
        MobioLogging().debug(f"user_controller::create_user():user_id: {user_id}")
        request_data = request.args.get("data", "")
        MobioLogging().info(f"user_controller::get_user():request.body: {request_data}")
        return jsonify({"message": "Get user data"})

    def post(self, user_id: int):
        # Logic to create a new user
        # Validate request data using Pydantic
        MobioLogging().debug(f"user_controller::create_user():user_id: {user_id}")
        user_data = UserModel(**request.json)

        check = UserModelResponse(datas=[user_data])

        MobioLogging().info(f"user_controller::create_user():request.body: {user_data}")

        return jsonify({"message": "User created", "data": check.model_dump()})


user_bp.add_url_rule(
    "/user/<int:user_id>", view_func=UserController.as_view("user_controller")
)
