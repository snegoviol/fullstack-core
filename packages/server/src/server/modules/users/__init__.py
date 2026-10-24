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
# packages/server/src/server/modules/users/__init__.py
# ==================================================================================================

from starlette.routing import Route
from .routes import users_get, user_role_post, user_delete_post
from ...config import RoutePath

users_routes = [
    Route(RoutePath.USERS, endpoint=users_get, methods=["GET"]),
    Route(RoutePath.USER_ROLE, endpoint=user_role_post, methods=["POST"]),
    Route(RoutePath.USER_DELETE, endpoint=user_delete_post, methods=["POST"]),
]

# ==================================================================================================
