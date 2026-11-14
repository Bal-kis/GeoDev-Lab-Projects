import geopandas as gpd

wards = gpd.read_file("data/processed/kwara_wards_projected.gpkg", layer="kwara_wards_projected").to_crs(epsg=32631)
schools = gpd.read_file("data/processed/schools.gpkg", layer="schools").to_crs(epsg=32631)

#buffer
reach = schools.copy()
reach["geometry"] = schools.buffer(2000)
print("buffered:", len(reach), "schools")

#count schools per ward
joined = gpd.sjoin(schools, wards[["ward", "geometry"]], how="inner", predicate = "within")
counts = joined.groupby("ward").size().rename("school_count").reset_index()
wards = wards.merge(counts, on="ward", how="left")
wards["school_count"] = wards["school_count"].fillna(0).astype(int)
print(wards[["ward", "school_count"]].sort_values("school_count", ascending=False).head(10))
print("Total counted:", wards["school_count"].sum(), "of", len(schools))
