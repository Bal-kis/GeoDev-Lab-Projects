import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/kwara_wards_projected.gpkg", layer="kwara_wards_projected").to_crs(epsg=32631)
schools = gpd.read_file("data/processed/schools.gpkg", layer="schools").to_crs(epsg=32631)

wards["area_km2"] = wards.area / 1_000_000

reach = schools[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1_000_000

gaps = uncovered[["ward", "uncovered_km2"]]
result = wards.merge(gaps, on="ward", how="left")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)
print(result[["ward", "area_km2", "uncovered_km2", "uncovered_pct"]].round(2))

result.to_file("data/processed/kwara_school_coverage.gpkg", layer="coverage")
print("Saved result layer to data/processed/kwara_school_coverage.gpkg")

#create a map.png
fig, ax = plt.subplots(figsize=(7, 8))
result.plot(column="uncovered_pct", ax=ax, edgecolor="#666666")
schools.plot(ax=ax, color="#004923", markersize=18)
ax.set_title("Ward areas beyond 2km of a school in kwara State")
ax.set_axis_off()

fig.savefig("month-03/week-11/my_reach_map.png", dpi=150, bbox_inches="tight")
print("Map saved")