"""The Tapo Vacuum Advanced integration."""
import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "tapo_vacuum"
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Tapo Vacuum from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    # This forwards the setup to your vacuum.py platform later
    await hass.config_entries.async_forward_entry_setups(entry, ["vacuum"])
    return True

async def async_unload_entry(hass: Assistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["vacuum"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
