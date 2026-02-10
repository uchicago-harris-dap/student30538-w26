# README

This file documents the source data files used in the spatial analysis and mapping for the project.

## Data Sources

### 1. [Global Power Plant Database (WRI)](https://energydata.info/dataset/world-global-power-plant-database-2018#:~:text=The%20Global%20Power%20Plant%20Database,updated%20as%20data%20becomes%20available)
- **Source data last accessed**: 7/7/2025
- **Folder:** `globalpowerplantdatabasev130/`
- **Description:** Contains global data on power plants, including geolocation, capacity, fuel type, and commissioning year.
- **Processing:** Only the U.S.-based plants (`country == 'USA'`) are extracted and saved to the derived-data folder.

---

### 2. [Independent Systems Operator Boundaries (NRDC)]( )
- **Source data last accessed**: 7/7/2025
- **File:** `Independent_System_Operator_3582480108073697601.geojson`
- **Description:** GeoJSON file with U.S.-based Independent System Operator (ISO) market boundaries. Cleaned and renamed in derived data.
- **Processing**: Cleaned ISO region names
---

### 3. [U.S. States Boundaries (Kaggle)](https://www.kaggle.com/datasets/pompelmo/usa-states-geojson)
- **Source data last accessed**: 7/7/2025
- **File:** `us-states.json`
- **Description:** JSON file of all U.S. state boundaries. 
**Processing**: Used to extract the lower 48 states.



---

### 4. [Principal Cities Data (via Andrew Van Leuven)](https://andrewvanleuven.com/post/cityshapefiles/)
- **Source data last accessed**: 7/7/2025
- **Folders:** 
  - `us_principal_city_dots/`
  - `us_principal_cities/`
- **Description:** Shapefiles containing point and polygon geometries for principal U.S. cities.
- **Processing:** Cities with population greater than 500,000 were selected for derived datasets.


---


## Notes

- All raw files are located in `data/raw-data/`.
- Code to preprocess is located in `preprocessing.py`
- Processed and cleaned files are written to `data/derived-data/` during preprocessing.

