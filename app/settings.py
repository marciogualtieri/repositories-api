"""
Application level settings.
"""

from pydantic_settings import BaseSettings

from . import schemas


class Settings(BaseSettings):
    """
    These settings might be overwritten by environment variables
    having the same name as the class attribute, e.g.:

    > export GITHUB_API_ACCESS_TOKEN="<Some Token>"

    Would overwrite the default value with "<Some Token>".
    """

    DEFAULT_LIMIT: schemas.LimitChoices = schemas.LimitChoices.TEN
    DEFAULT_FROM_DAYS_AGO: int = 5 * 365
    GITHUB_API_ACCESS_TOKEN: str = ""
    GITHUB_API_CLIENT_CACHE_TTL_HOURS: int = 3
    GITHUB_API_CLIENT_CACHE_MAXSIZE: int = 500


settings = Settings()
