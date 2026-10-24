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
# Originally from Human Pose Estimation Service 
# (https://github.com/snegoviol/pose-estimation-service).
# Modified for Full-Stack Core to suit the needs of this project.
# 
# ==================================================================================================
# packages/shared/src/postgres_lib/__init__.py
# ==================================================================================================

from .config import postgres_config
from .session import (
    sync_engine, sync_session_factory, get_sync_db_session,
    async_engine, async_session_factory, get_async_db_session
)
from .models import (
    Base, User, InferenceHistory, Lead, 
    LeadStatus, LeadStatusSQL, Role, RoleSQL
)
from .repositories import (
    BaseRepository, UserRepository, 
    InferenceHistoryRepository, LeadRepository
)

# ==================================================================================================
