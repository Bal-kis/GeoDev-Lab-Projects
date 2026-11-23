from shapely.geometry import box
import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask


print("Layers:", gpd.list_layers("data/processed/kwara_wards_projected.gpkg"))

with rasterio.open("data/raw/ilorin_dem.tif") as src:
  wards = gpd.read_file("data/processed/kwara_wards_projected.gpkg", layer="kwara_wards_projected").to_crs(src.crs)
  wards = wards[wards.within(box(*src.bounds))].copy()
  print(len(wards), "wards inside the raster")

  means = []
  for geom in wards.geometry:
    cells, _ = mask(src, [geom], crop=True, filled=False)
    means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means, 1)
print(wards[["ward", "mean_elevation_m"]])  

result = wards[["ward", "mean_elevation_m"]]
result.to_csv("month-03/week-12/my_zonal.csv", index=False)
print("Saved month-03/week-12/my_zonal.csv")