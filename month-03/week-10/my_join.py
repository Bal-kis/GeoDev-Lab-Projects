import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data/processed/kwara_wards.gpkg", layer='kwara_wards_projected_2')
pop = pd.read_csv("data/raw/ward_schools_count.csv")

first_try = wards.merge(pop, left_on="ward", right_on="ward", how="left" )
matched = first_try["name_count"].notna().sum()
print("Matched on first try:", matched, "of", len(wards))

def clean_name(name):
  return name.strip().upper().replace("-", " ").replace("/", " ")

wards["join_key"] = wards["ward"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["name_count"].notna().sum()
print("Matched after cleaning:", matched, "of", len(wards))
print(joined[["ward_x", "name_count"]])
