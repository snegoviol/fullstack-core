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
# Originally from Backend Core (https://github.com/snegoviol/backend-core).
# Modified for Full-Stack Core to suit the needs of this project.
# 
# ==================================================================================================
# packages/server/src/server/modules/health/types.py
# ==================================================================================================

from enum import StrEnum

# ==================================================================================================
 
class ServiceStatus(StrEnum):
    """
    Enumeration of service health states for runtime availability reporting.

    Represents the operational status of the application and its external
    dependencies as observed during health checks. Used to drive readiness
    and liveness probes in container orchestration environments.

    Attributes
    ----------
    OK : ServiceStatus
        All critical components are reachable and responding within expected
        thresholds; the service is fully operational.
    DEGRADED : ServiceStatus
        Core application logic is functional but one or more non-critical
        dependencies are unavailable; partial feature set may be affected.
    UNAVAILABLE : ServiceStatus
        The service failed to respond to health probes or critical dependencies
        are unreachable; the instance should not receive production traffic.
    """

    OK = "ok"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"

# ==================================================================================================
