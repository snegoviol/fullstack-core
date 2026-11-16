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
# packages/server/src/server/modules/logout/routes.py
# ==================================================================================================

from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse
from session_lib import SessionService, session_config
from ...config import RoutePath

# ==================================================================================================

async def logout_post(request: Request) -> RedirectResponse:
    """
    Terminate the user session and redirect to the landing page.

    Retrieves the session identifier from the request cookie and deletes
    the corresponding session entry from Redis. The cookie is cleared
    regardless of whether a valid session was found, so the client is
    always left in a logged-out state even if the session had already
    expired or was never created.

    Parameters
    ----------
    request : Request
        Incoming request object containing the session cookie.

    Returns
    -------
    RedirectResponse
        HTTP 303 redirect to the landing page after session termination.
        The 303 status code ensures the client issues a GET request to
        the destination rather than repeating the POST.
    """
    session_id = request.cookies.get(session_config.cookie_name)

    if session_id:
        await SessionService.delete(session_id)

    response = RedirectResponse(
        url=RoutePath.LANDING,
        status_code=status.HTTP_303_SEE_OTHER,
    )
    response.delete_cookie(
        key=session_config.cookie_name,
        path=session_config.cookie_path,
    )
    return response

# ==================================================================================================
