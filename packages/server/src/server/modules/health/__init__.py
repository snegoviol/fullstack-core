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
# packages/server/src/server/modules/health/__init__.py
# ==================================================================================================

from starlette.routing import Route
from .routes import health_deep_get, health_shallow_get
from ...config import RoutePath

health_routes = [
    Route(RoutePath.HEALTH_SHALLOW, endpoint=health_shallow_get, methods=["GET"]),
    Route(RoutePath.HEALTH_DEEP, endpoint=health_deep_get, methods=["GET"]),
]

# ==================================================================================================
