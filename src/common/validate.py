from functools import wraps

from flask import request
from pydantic import BaseModel


def validate(data_check: type[BaseModel]):
    """
    Decorator to validate the request data using Pydantic.
    This decorator can be used to validate the request data in Flask routes.
    It takes a Pydantic model as an argument and validates the request data against it.
    If the validation fails, it raises a ValidationError and returns a 422 Unprocessable Entity response.
    If the validation succeeds, it adds the validated data to the keyword arguments of the decorated function.
    The validated data can be accessed in the decorated function using the 'data' keyword argument.
    The decorated function should accept the 'data' keyword argument to access the validated data.

    Args:
        data_check (type[BaseModel]): _description_
    """

    def decorator(f):
        @wraps(f)
        def decorator_func(*agrs, **kagrs):
            kagrs["data"] = data_check(**request.json)

            return f(*agrs, **kagrs)

        return decorator_func

    return decorator
