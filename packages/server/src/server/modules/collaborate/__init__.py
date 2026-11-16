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
# packages/server/src/server/modules/collaborate/__init__.py
# ==================================================================================================

from starlette.routing import Route
from .routes import collaborate_get, collaborate_post
from ...config import RoutePath

collaborate_routes = [
    Route(RoutePath.COLLABORATE, endpoint=collaborate_get, methods=["GET"]),
    Route(RoutePath.COLLABORATE, endpoint=collaborate_post, methods=["POST"]),
]

# ==================================================================================================
