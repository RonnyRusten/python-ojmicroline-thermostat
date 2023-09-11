"""Energy Usage model for OJ Microline Thermostat."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any

@dataclass
class Usage:
    """Object representing a single usage."""

    no: int
    usage: float

    def __init__(self, no: int, usage: float) -> None:
        """
        Create a new Usage instance.

        Args:
            no: The usage number.
            usage: The energy usage.
        """
        self.no = no
        self.usage = usage

@dataclass
class EnergyUsage:
    """Object representing a enegy usage from a thermostat group."""

    usages: dict[str, list[Usage]]

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> EnergyUsage:
        """
        Return a new EnergyUsage instance based on the given JSON.

        Args:
            data: The JSON data from the API.

        Returns:
            A EnergyUsage Object.
        """

        usages = []
        n = 0
        for usage in data["EnergyUsage"][0]["Usage"]:
            usages.append(
                Usage(
                    n,
                    usage["EnergyKWattHour"],
                )
            )
            n += 1

        return cls(usages)
