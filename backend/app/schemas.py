from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DatasetObjectResponse(BaseModel):
    name: str


class DatasetListResponse(BaseModel):
    bucket: str
    prefix: str
    items: list[DatasetObjectResponse] = Field(default_factory=list)


class PreviewResponse(BaseModel):
    columns: list[str]
    rows: list[dict[str, Any]]


class DayDataResponse(BaseModel):
    target_date: str
    columns: list[str]
    row_count: int
    rows: list[dict[str, Any]]


class DayRoadCountResponse(BaseModel):
    target_date: str
    unique_roads: int
    roads: list[str] = Field(default_factory=list)


class RoadComparisonResponse(BaseModel):
    start_date: str
    end_date: str
    start_unique_roads: int
    end_unique_roads: int
    start_roads: list[str] = Field(default_factory=list)
    end_roads: list[str] = Field(default_factory=list)
    roads_only_in_start: list[str] = Field(default_factory=list)
    roads_only_in_end: list[str] = Field(default_factory=list)
    shared_roads: list[str] = Field(default_factory=list)


class DateRangeDataResponse(BaseModel):
    start_date: str
    end_date: str
    columns: list[str]
    row_count: int
    rows: list[dict[str, Any]]


class StatsResponse(BaseModel):
    rows: int | None = None
    rows_with_road_name: int | None = None
    unique_roads: int | None = None
    unique_weather: int | None = None
    min_record_datetime: str | None = None
    max_record_datetime: str | None = None

