import pandas as pd
from pathlib import Path

# Resolve data paths relative to the `ps` package root (two levels up from this file)
base = Path(__file__).resolve().parents[1]
data_dir = base / "data" / "external"

routes_fp = data_dir / "routes.txt"
trips_fp = data_dir / "trips.txt"

if not routes_fp.exists() or not trips_fp.exists():
    raise FileNotFoundError(f"Expected files at {routes_fp} and {trips_fp}")

routes = pd.read_csv(routes_fp)
trips = pd.read_csv(trips_fp)

trip_counts = (
    trips.groupby("route_id")
    .size()
    .reset_index(name="scheduled_trip_count")
)

print(trip_counts.head())
