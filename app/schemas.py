"""
Responses payload schemas.
"""

from enum import Enum
from typing import Union

from pydantic import BaseModel


class Repository(BaseModel):
    """
    Repository's payload schema.
    """

    id: int
    name: Union[str, None] = None
    description: Union[str, None] = None
    url: Union[str, None] = None
    language: Union[str, None] = None
    created: Union[str, None] = None
    stars: Union[int, None] = None


class LimitChoices(int, Enum):
    """
    Limit choices (enumeration).
    """

    TEN = 10
    FIFTY = 50
    ONE_HUNDRED = 100
