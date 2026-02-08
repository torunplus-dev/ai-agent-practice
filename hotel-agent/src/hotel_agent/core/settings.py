from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_settings() -> dict[str, Any]:
    """Load config/config.yaml if present, otherwise return empty settings."""
    root = Path(__file__).resolve().parents[3]
    config_path = root / "config" / "config.yaml"
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}
