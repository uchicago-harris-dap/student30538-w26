# ## Pre-Processing from Raw Data
# set-up steps
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely
import warnings
import time
import os

warnings.filterwarnings("ignore")

# reset to working directory
current_wd = os.getcwd()
print(f"Working directory is now: {current_wd}")

# Restrict to Lower 48 States
output_path = "data/derived-data/lower_48_states.geojson"
if not os.path.exists(output_path):
    us_states_gdf = gpd.read_file('data/raw-data/us-states.json')
    lower48_states_gdf = us_states_gdf[~us_states_gdf['name'].isin(['Alaska', 'Hawaii', 'Puerto Rico'])]
    lower48_states_gdf.to_file(output_path, driver="GeoJSON")
    print(f"GeoDataFrame successfully exported to: {output_path}")
else:
    print(f"Skipping: {output_path} already exists.")

# Restrict GPPD datasets to just US-based ones
output_path = "data/derived-data/us_gppd.csv"
if not os.path.exists(output_path):
    # Define bounding box for lower 48 (approximate)
    min_lat, max_lat = 24.5, 49.5
    min_lon, max_lon = -125, -66.5
    gppd_df = pd.read_csv('data/raw-data/globalpowerplantdatabasev130/global_power_plant_database.csv')
    us_gppd_df = gppd_df[gppd_df['country'] == 'USA']
    # Further filter to lower 48 states using lat/lon
    us_gppd_df = us_gppd_df[
        (us_gppd_df['latitude'].between(min_lat, max_lat)) &
        (us_gppd_df['longitude'].between(min_lon, max_lon))
    ]
    us_gppd_df.to_csv(output_path, index=False)
    print(f"USA lower 48 states GPPD Data successfully exported to: {output_path}")
else:
    print(f"Skipping: {output_path} already exists.")

# Filter cities layer to population > 500k, and drop empty/missing geometries
output_path = "data/derived-data/cities_greater_500k.shp"
if not os.path.exists(output_path):
    cities_gdf = gpd.read_file('data/raw-data/us_principal_city_dots/us_principal_city_dots.shp')
    filtered_cities_gdf = cities_gdf[cities_gdf['pop_2010'] >= 500000]
    # Drop rows with missing or empty geometries
    filtered_cities_gdf = filtered_cities_gdf[
        ~filtered_cities_gdf.geometry.is_empty & 
        filtered_cities_gdf.geometry.notna()
    ]
    filtered_cities_gdf.to_file(output_path, driver='ESRI Shapefile')
    print(f"Filtered points with population data exported to: {output_path}")
else:
    print(f"Skipping: {output_path} already exists.")

# Clean names in ISO and export
output_path = "data/derived-data/Independent_System_Operator.geojson"
if not os.path.exists(output_path):
    iso_gdf = gpd.read_file('data/raw-data/Independent_System_Operator_3582480108073697601.geojson')
    iso_gdf["NAME"] = iso_gdf["NAME"].str.title()
    iso_gdf.to_file(output_path, driver="GeoJSON")
    print(f"Cleaned ISO exported to: {output_path}")
else:
    print(f"Skipping: {output_path} already exists.")
