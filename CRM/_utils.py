import os
import yaml
from typing import Any
from _types import AppConfig


def load_config(file_path: str = os.path.join(os.path.dirname(__file__), "config.yaml")) -> AppConfig:
    with open(file_path, "r") as f:
        data: dict[str, Any] = yaml.safe_load(f)
    return AppConfig(**data)
