from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")


def _split_csv(value: str | None, default: list[str]) -> list[str]:
    if not value:
        return default
    items = [item.strip() for item in value.split(",")]
    return [item for item in items if item]


@dataclass(frozen=True)
class Settings:
    gcs_bucket: str = field(default_factory=lambda: os.getenv("GCS_BUCKET", ""))
    gcs_prefix: str = field(default_factory=lambda: os.getenv("GCS_PREFIX", ""))
    gcp_project: str = field(default_factory=lambda: os.getenv("GCP_PROJECT", ""))
    duckdb_path: str = field(default_factory=lambda: os.getenv("DUCKDB_PATH", ":memory:"))
    cache_dir: Path = field(
        default_factory=lambda: Path(os.getenv("DASHBOARD_CACHE_DIR", Path(__file__).resolve().parents[3] / ".cache" / "parquet"))
    )
    cors_origins: list[str] = field(
        default_factory=lambda: _split_csv(
            os.getenv("CORS_ORIGINS"),
            ["http://localhost:3000", "http://127.0.0.1:3000"],
        )
    )


settings = Settings()
