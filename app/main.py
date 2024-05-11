"""
Main module containing the web app and routes.
"""

import logging
from datetime import date, timedelta

from fastapi import FastAPI, Query
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse, Response

from . import crud, schemas
from .settings import settings

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Repositories API",
    summary="Implement CRUD services over GitHub API's repositories.",
)


async def _catch_exceptions(request: Request, call_next) -> Response:
    # pylint: disable=broad-exception-caught
    """
    Middleware that catches any unexpected exceptions.
    """
    try:
        return await call_next(request)
    except Exception:
        logger.exception("Unexpected exception.")
        return JSONResponse(
            {
                "detail": "It's been an internal server error. "
                "Please contact the service's administrator."
            },
            status_code=500,
        )


app.middleware("http")(_catch_exceptions)


@app.get("/", include_in_schema=False)
async def redirect_root_to_docs():
    """
    Redirects the root route to OPENAPI docs.
    """
    return RedirectResponse(url="/docs")


@app.get(
    "/tops/",
    response_model=list[schemas.Repository],
    description="Gets a list of top repositories sorted by number of stars.",
)
async def get_tops(
    from_date: date = Query(
        default=None,
        description="Only repositories created from this date (ISO 8601 format).",
    ),
    language: str = Query(
        default=None, description="Only repositories using this language."
    ),
    limit: schemas.LimitChoices = Query(
        default=settings.DEFAULT_LIMIT, description="Number of top repositories."
    ),
):
    """
    Returns the top repositories sorted by stars.
    """
    default_from_date = date.today() - timedelta(days=settings.DEFAULT_FROM_DAYS_AGO)
    return await crud.get_tops(
        from_date=from_date if from_date else default_from_date,
        limit=limit.value,
        language=language,
    )
