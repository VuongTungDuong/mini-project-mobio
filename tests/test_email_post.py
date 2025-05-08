from unittest import TestCase

from faker import Faker
from src.apis.v1_0.blueprints_api import app


class TestEmailPost(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_post_email_invalid(self):
        # Test invalid email
        response = self.app.post(
            "/api/v1.0/email", json={"email": "invalid_email_format"}
        )
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        print(response_data)

    def test_post_email(self):
        # Test valid email
        for _ in range(1000):
            response = self.app.post("/api/v1.0/email", json={"email": Faker().email()})
            self.assertEqual(response.status_code, 201)
            # response_data = response.get_json()
            # print(response_data)
            # sleep(randint(0, 100) / 1000)  # Random sleep between 1 and 3 seconds


if "__main__" == __name__:
    import unittest

    unittest.main()
