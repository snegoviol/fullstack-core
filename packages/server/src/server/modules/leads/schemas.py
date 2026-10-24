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
# packages/server/src/server/modules/leads/schemas.py
# ==================================================================================================

from dataclasses import dataclass
from postgres_lib import LeadStatus

# ==================================================================================================

@dataclass
class LeadStatusForm:
    """
    Request shape for the lead status update form.

    Normalizes the submitted status value on construction and exposes a
    parsed LeadStatus enum as a property. Handlers inspect that property
    and return a generic error when the value is not recognized.

    Attributes
    ----------
    status : str
        Target status value, stripped of surrounding whitespace. Default is
        empty string.
    """

    status: str = ""

    def __post_init__(self) -> None:
        """
        Normalize the submitted status field.
        """
        self.status = self.status.strip()

    @property
    def target_status(self) -> LeadStatus | None:
        """
        Return the parsed status enum value when recognized.

        Returns
        -------
        LeadStatus or None
            Parsed status when the submitted value maps to a known
            LeadStatus, otherwise None.
        """
        try:
            return LeadStatus(self.status)
        except ValueError:
            return None

# ==================================================================================================
