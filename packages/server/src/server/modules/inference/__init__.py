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
# packages/server/src/server/modules/inference/__init__.py
# ==================================================================================================

from starlette.routing import Route
from .routes import inference_get, inference_post, inference_status_get
from ...config import RoutePath

inference_routes = [
    Route(RoutePath.INFERENCE, endpoint=inference_get, methods=["GET"]),
    Route(RoutePath.INFERENCE, endpoint=inference_post, methods=["POST"]),
    Route(
        RoutePath.INFERENCE_STATUS,
        endpoint=inference_status_get,
        methods=["GET"],
    ),
]

# ==================================================================================================
