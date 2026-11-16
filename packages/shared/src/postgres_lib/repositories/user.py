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
# packages/shared/src/postgres_lib/repositories/user.py
# ==================================================================================================

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseRepository
from ..models import User

# ==================================================================================================

class UserRepository(BaseRepository):
    """
    Concrete repository for managing User entities in the database.

    Attributes
    ----------
    model_class : ClassVar[type[User]]
        Bound to the User ORM class at class definition time.
    """

    model_class = User

    @classmethod
    async def get_by_email(
        cls,
        session: AsyncSession,
        email: str,
    ) -> User | None:
        """
        Fetch a User by email address.

        Parameters
        ----------
        session : AsyncSession
            Active async database session bound to the transaction.
        email : str
            Email address to look up. Must be an exact match.

        Returns
        -------
        User or None
            Matching User instance, or None if not found.
        """
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

# ==================================================================================================
