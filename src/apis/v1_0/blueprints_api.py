#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Company: MobioVN
Date created: 2025/05/05
"""

from mobio.sdks.base.apis.check_service import checking_service_mod

from src.apis import app
from src.controllers.email_controller import email_bp
from src.controllers.user.user_mobio_controller import user_bp

v1_0_prefix = "/api/v1.0"

app.register_blueprint(checking_service_mod, url_prefix=v1_0_prefix)


app.register_blueprint(user_bp, url_prefix=v1_0_prefix)

app.register_blueprint(email_bp, url_prefix=v1_0_prefix)
