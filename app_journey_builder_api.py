#!/usr/bin/env python
"""Company: MobioVN
Date created: 2025/05/05
"""

from src.apis.v1_0.blueprints_api import app


def check_gi() -> None:
    """Check gi"""
    d = 0 / 0
    print(d)


print(app.url_map)
if __name__ == "__main__":
    check_gi()
    app.run(host="0.0.0.0", port=5000, debug=True)
