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
# packages/server/src/server/shared/ui/__init__.py
# ==================================================================================================

from .navbar import create_navbar
from .footer import create_footer
from .pagination import create_pagination
from .empty_state import create_empty_state
from .forms import create_form_card, create_form_control
from .spinner import create_spinner
from .alert import create_alert, create_form_alert_slot, Alert
from .layout import create_layout, create_page_header
from .error_page import create_error_page
from .confirmation_modal import create_confirmation_modal

# ==================================================================================================
