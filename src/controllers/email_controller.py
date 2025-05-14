import random

from flask import Blueprint, jsonify, request
from flask.views import MethodView
from src.models.email_model import EmailStatus, EmailModel, EmailValidate

email_bp = Blueprint("email", __name__, url_prefix="/email")


class EmailController(MethodView):
    def __init__(self):
        self.email_model = EmailModel()

    def get(self):
        # Here you would typically fetch the email requests from a database
        # For this example, we'll just return a dummy response
        return jsonify({"message": self.email_model.get_all_email()}), 200

    def post(self):
        data = request.json

        try:
            email_request = EmailValidate(**data)
            email_request.partition = random.randint(0, 9)  # Random partition number
            email_request.status = EmailStatus.CHECKING
            email_request.creaded_at = (
                email_request.creaded_at.now()
            )  # Set the current time

        except (TypeError, ValueError) as e:
            return jsonify({"error": str(e)}), 400

        # Insert the email request into the database
        if not self.email_model.insert_email(email_request):
            return jsonify({"error": "Failed to insert email request"}), 500

        return jsonify(
            {
                "message": "Email request inserted successfully",
                "data": email_request.model_dump(),
            }
        ), 201


email_bp.add_url_rule("/email", view_func=EmailController.as_view("email"))
