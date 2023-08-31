"""Energy Usage model for OJ Microline Thermostat."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any
import async_timeout
from aiohttp import ClientError, ClientSession, hdrs
from yarl import URL
import asyncio
import json
import socket
# from ..exceptions import (
#     OJMicrolineAuthException,
#     OJMicrolineConnectionException,
#     OJMicrolineException,
#     OJMicrolineResultsException,
#     OJMicrolineTimeoutException,
# )

@dataclass
class Usage:
    """Object representing a single usage."""

    date: datetime
    usage: float

    def __init__(self, date: datetime, usage: float) -> None:
        """
        Create a new Usage instance.

        Args:
            date: The date of the event.
            temperature: The temperature of the event.
        """
        self.date = date
        self.usage = usage
