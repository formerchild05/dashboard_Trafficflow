export type DatasetObject = {
  name: string;
};

export type DatasetListResponse = {
  bucket: string;
  prefix: string;
  items: DatasetObject[];
};

export type DayDataResponse = {
  target_date: string;
  columns: string[];
  row_count: number;
  rows: Record<string, unknown>[];
};

export type DayRoadCountResponse = {
  target_date: string;
  unique_roads: number;
  roads: string[];
};

export type DateRangeDataResponse = {
  start_date: string;
  end_date: string;
  columns: string[];
  row_count: number;
  rows: Record<string, unknown>[];
};