"""
Implementations for all CRUD operations on the GitHub API.
"""

from datetime import date, timedelta
from typing import Any, AsyncGenerator, List
from urllib.parse import urlencode

import aiohttp
import cachetools
from gidgethub.aiohttp import GitHubAPI

from . import schemas
from .settings import settings

cache: cachetools.Cache = cachetools.TTLCache(
    maxsize=settings.GITHUB_API_CLIENT_CACHE_MAXSIZE,
    ttl=timedelta(hours=settings.GITHUB_API_CLIENT_CACHE_TTL_HOURS).total_seconds(),
)


async def get_tops(
    from_date: date, limit: int, language: str | None = None
) -> list[schemas.Repository]:
    """
    Gets the top repositories using Gidgethub as the client.

    :param from_date: Get repositories created from this date.
    :param limit: Number of top repositories to get.
    :param language: Get repositories using this programming language.

    :return: The top repositories sorted by number of starts.
    """
    url_params = _build_url_params(from_date, limit, language)
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(
            session,
            "requester",
            oauth_token=settings.GITHUB_API_ACCESS_TOKEN,
            cache=cache,
        )
        repos = gh.getiter(url=f"search/repositories?{url_params}")
        return await _extract_repositories_data(limit, repos)


def _build_url_params(from_date: date, limit: int, language: str | None) -> str:
    """
    Builds the URL parameters string for the request.
    """
    query = f"created:>{from_date.isoformat()}"
    if language:
        query += f" language:{language}"
    parameters = {"sort": "star", "order": "desc", "per_page": limit}

    url_params = f"q={query}&{urlencode(parameters)}"
    return url_params


async def _extract_repositories_data(
    limit: int, repos: AsyncGenerator[Any, None]
) -> List[schemas.Repository]:
    """
    Extracts the repository payload data from GitHub API response.
    """
    tops = []
    for _ in range(limit):
        repo = await anext(repos)
        repository_data = schemas.Repository(
            id=repo["id"],
            name=repo["full_name"],
            description=repo["description"],
            url=repo["html_url"],
            language=repo["language"],
            created=repo["created_at"],
            stars=repo["stargazers_count"],
        )
        tops.append(repository_data)
    return tops
