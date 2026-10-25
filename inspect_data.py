import csv

# with open("kwara_wards.csv", encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)
# print("Number of rows:", len(rows))
# print("Columns:", list(rows[0].keys()))  

def inspect_column(filename, column): 
  with open("kwara_wards.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

  values = []
  for row in rows:
    raw = row[column].strip()
    if raw == "":
        continue
    values.append(float(raw))
    # value = float(row["area_sqkm"])
    # values.append(value)
  return {
    "Smallest": min(values),
    "Largest": max(values),
    "Count": len(values), 
}
area_result = inspect_column("kwara_wards.csv", "area_sqkm")
name_count = inspect_column("kwara_wards.csv", "name_count")
print("Area:", area_result)
print("Name:", name_count)



    