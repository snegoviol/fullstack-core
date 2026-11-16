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
# packages/server/src/server/shared/__init__.py
# ==================================================================================================

from .utils import html_response, create_icon, calculate_pagination
from .auth import role_for_display, role_for_authorization, get_session_user, require_role
from .parsing import parse_form, parse_query
from .schemas import EmailFieldMixin, PasswordFieldMixin, PageQuery

# ==================================================================================================
