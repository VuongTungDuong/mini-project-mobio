#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Company: MobioVN
Date created: 2025/05/05
"""

from flask_cors import CORS

from src.apis.v1_0.blueprints_api import app

CORS(app)

print(app.url_map)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
