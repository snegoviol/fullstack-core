# ==================================================================================================
# 
# Copyright (c) 2026 Ilya Snegov
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# ==================================================================================================
# packages/server/src/server/modules/leads/__init__.py
# ==================================================================================================

from starlette.routing import Route
from .routes import leads_get, lead_status_post
from ...config import RoutePath

leads_routes = [
    Route(RoutePath.LEADS, endpoint=leads_get, methods=["GET"]),
    Route(RoutePath.LEAD_STATUS, endpoint=lead_status_post, methods=["POST"]),
]

# ==================================================================================================
