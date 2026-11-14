import geopandas as gpd

wards = gpd.read_file("data/processed/kwara_wards_projected.gpkg", layer="kwara_wards_projected")

print("Before:")
print(wards["geometry"].is_valid.value_counts())

wards["geometry"] = wards["geometry"].make_valid()
print("After:")
print(wards["geometry"].is_valid.value_counts())