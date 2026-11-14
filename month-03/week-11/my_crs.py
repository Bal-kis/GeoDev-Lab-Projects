import geopandas as gpd

print("Layers:", gpd.list_layers("data/processed/kwara_wards_projected.gpkg"))
print("Layer:", gpd.list_layers("data/processed/schools.gpkg"))

wards = gpd.read_file("data/processed/kwara_wards_projected.gpkg", layer="kwara_wards_projected")
schools = gpd.read_file("data/processed/schools.gpkg", layer="schools")

print("Ward crs:", wards.crs)
print("Schools crs:", schools.crs)
print("Suggested UTM:", wards.estimate_utm_crs())

wards_UTM = wards.to_crs(epsg=32631)
schools_UTM = schools.to_crs(epsg=32631)

wards_UTM["area_km2"]= wards_UTM.area / 1_000_000
print(wards_UTM[["ward", "area_km2"]].head(5))
print("Total Kwara wards area:", round(wards_UTM["area_km2"].sum(), 1), "km2")

