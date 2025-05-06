import os
from dataclasses import dataclass


@dataclass
class Env:
    # MongoDB
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    MONGODB_DB = os.environ.get("MONGODB_DB", "")
    MONGODB_USER = os.environ.get("MONGODB_USER", "")
    MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD", "")
    MONGODB_PORT = int(os.environ.get("MONGODB_PORT", "27017"))
