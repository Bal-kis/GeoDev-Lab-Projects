import pandas as pd
import geopandas as gpd
table = pd.read_csv("data/raw/kwara_schools.csv")
print(table.head(3))

schools = gpd.GeoDataFrame(
  table,
  geometry = gpd.points_from_xy(table["X"], table["Y"]), crs = "EPSG:4326",
)

print(schools.head(3))
print(schools.crs)

schools.to_file("data/processed/schools.gpkg", layer="schools")
print("Saved", len(schools), "schools")