"""Minimal AstrBot plugin used to diagnose the marketplace parser path."""

from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_market_probe",
    "zjj1280637679-ship-it",
    "AstrBot 插件市场发布链路探针。",
    "0.0.1",
)
class MarketProbe(Star):
    """A deliberately inert plugin with no commands, tools, or background tasks."""

    def __init__(self, context: Context) -> None:
        super().__init__(context)
