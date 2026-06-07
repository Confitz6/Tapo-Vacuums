"""Support for Tapo Vacuum Robots."""
from __future__ import annotations

from typing import Any
from homeassistant.components.vacuum import (
    StateVacuumEntity,
    VacuumEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Modern feature flags including point/spot/area cleaning features
SUPPORT_TAPO = (
    VacuumEntityFeature.TURN_ON
    | VacuumEntityFeature.TURN_OFF
    | VacuumEntityFeature.RETURN_HOME
    | VacuumEntityFeature.STOP
    | VacuumEntityFeature.PAUSE
    | VacuumEntityFeature.START
    | VacuumEntityFeature.CLEAN_SPOT
    | VacuumEntityFeature.STATE
)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Tapo vacuum cleaner from a config entry."""
    async_add_entities([TapoVacuumAdvanced("Tapo Robot Vacuum")], True)

class TapoVacuumAdvanced(StateVacuumEntity):
    """Representation of an advanced Tapo Vacuum."""

    _attr_supported_features = SUPPORT_TAPO

    def __init__(self, name: str) -> None:
        """Initialize the vacuum."""
        self._attr_name = name
        self._attr_state = "docked"
        self._attr_unique_id = "tapo_vacuum_fresh_start"

    async def async_start(self) -> None:
        """Start or resume the cleaning task."""
        self._attr_state = "cleaning"
        self.async_write_ha_state()

    async def async_pause(self) -> None:
        """Pause the cleaning task."""
        self._attr_state = "paused"
        self.async_write_ha_state()

    async def async_return_to_base(self) -> None:
        """Set the vacuum to return to a base."""
        self._attr_state = "returning"
        self.async_write_ha_state()

    async def async_stop(self, **kwargs: Any) -> None:
        """Stop the vacuum."""
        self._attr_state = "idle"
        self.async_write_ha_state()
