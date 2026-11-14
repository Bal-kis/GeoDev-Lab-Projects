import geopandas as gpd

print(gpd.list_layers("data/processed/kwara_wards.gpkg"))

wards = gpd.read_file("data/processed/kwara_wards.gpkg", layer= "kwara_wards_projected_2")

print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)