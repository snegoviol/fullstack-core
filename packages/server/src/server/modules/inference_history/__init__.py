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
# packages/server/src/server/modules/inference_history/__init__.py
# ==================================================================================================

from starlette.routing import Route
from .routes import inference_history_get
from ...config import RoutePath

inference_history_routes = [
    Route(RoutePath.INFERENCE_HISTORY, endpoint=inference_history_get, methods=["GET"]),
]

# ==================================================================================================
