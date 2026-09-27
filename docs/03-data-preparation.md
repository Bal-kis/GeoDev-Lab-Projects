# Data preparation

## 1. Cordinate system decision.

**Working CRS:** The kwara ward and schools datas arrived in **EPSG:4326**.

**Why this one:**
- reprojected both layers from EPSG:4326 to EPSG:32631(UTM Zone 31N).
- Reason: I reprojected so the spatial join count schools per ward correctly.

## 2. Clipping to the study area.
- **Boundary used:** Operational ward boundary data.  
- **Features before clipping:** wards data for 24 states.
- **Features after clipping:** feature was clipped to kwara state which is my study area.

## 3. Five quality checks.
### 1.  **completeness:**
schools are more concentrated in urban ilorin than the rurals. Mosts of the school points and polygon arent named.This might suggest incomplete attribute data even where features exist.

### 2. **currency:** 
GRID3 wards published june 2026, downloaded september 2026. OSM schools downloaded in september 2026.

### 3. **Positional Accuracy:** 
points and polygon appear in reasonable locations, no obvious displacement.

### 4. **Attribute Accuracy:** 
No mixed values found.

### 5. **Fitness for purpose:** 
60% of mapped schools points carry no name which means i can count school points per ward, but i can't identify most of them aren't named.

## 4. problem encountered
-  No major problems encountered. Both layers are loaded aand reprojected cleanly.

## 5. Analysis-ready output
- **File**:kwara_school_projects/data/processed/wards_school_count.gpkg
- **Format:** Geopackage.
- **CRS**: EPSG: 32631

- **Status:** Week 3 completed. Data acquisition in month 1 summary, see [month-1-summary](month-1-summary.md)
