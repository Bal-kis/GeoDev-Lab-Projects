import rasterio

with rasterio.open("data/raw/ilorin_dem.tif") as src:
  print("Width x Height:", src.width, "x", src.height)
  print("Bands:", src.count)
  print("Data Type:", src.dtypes)
  print("CRS:", src.crs)
  print("Pixel size:", src.res)
  print("Bounds:", src.bounds)
  print("Nodata:", src.nodata)
  print("Transform:")
  print(src.transform)
