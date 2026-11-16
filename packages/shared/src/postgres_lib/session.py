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
# packages/shared/src/postgres_lib/session.py
# ==================================================================================================

from typing import Generator, AsyncGenerator
from contextlib import contextmanager, asynccontextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .config import postgres_config

# ==================================================================================================

sync_engine = create_engine(
    postgres_config.database_url,
    echo=postgres_config._echo,
    future=True
)
"""
Synchronous SQLAlchemy database engine configured via application settings.
"""

# ==================================================================================================

sync_session_factory = sessionmaker(
    autocommit=postgres_config._autocommit,
    autoflush=postgres_config._autoflush,
    expire_on_commit=postgres_config._expire_on_commit,
    bind=sync_engine,
)
"""
Synchronous session factory configured according to application-wide database behavior policies.
"""

# ==================================================================================================

@contextmanager
def get_sync_db_session() -> Generator[Session, None, None]:
    """
    Manage the lifecycle of an async database session for a single request.

    Opens a new async session, yields it for ORM operations, and guarantees
    cleanup with automatic rollback on failure. Committing is the caller's
    responsibility: a write that is not explicitly committed before the context
    exits is discarded when the session closes. On any exception the session is
    rolled back and the exception re-raised.

    Yields
    ------
    Session
        Active synchronous session bound to the sync engine.
    """
    with sync_session_factory() as db:
        try:
            yield db
        except Exception:
            db.rollback()
            raise

# ==================================================================================================

async_engine = create_async_engine(
    postgres_config.database_url,
    echo=postgres_config._echo,
    future=True
)
"""
Asynchronous SQLAlchemy database engine configured via application settings.
"""

# ==================================================================================================

async_session_factory = async_sessionmaker(
    autocommit=postgres_config._autocommit,
    autoflush=postgres_config._autoflush,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=postgres_config._expire_on_commit
)
"""
Asynchronous session factory configured according to application-wide database behavior policies.
"""

# ==================================================================================================

@asynccontextmanager
async def get_async_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Manage the lifecycle of an async database session for a single request.

    Opens a new async session, yields it for ORM operations, and guarantees
    cleanup with automatic rollback on failure. Committing is the caller's
    responsibility: a write that is not explicitly committed before the context
    exits is discarded when the session closes. On any exception the session is
    rolled back and the exception re-raised.

    Yields
    ------
    AsyncSession
        Active asynchronous session bound to the async engine.
    """
    async with async_session_factory() as db:
        try:
            yield db
        except Exception:
            await db.rollback()
            raise

# ==================================================================================================
