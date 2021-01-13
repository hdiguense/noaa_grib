import rasterio
import geopandas as gpd

lons = [-86]
lats = [9]

filepath = r'C:\Users\ldieg\Desktop\lluvia_centro_america\lluvia.tif'

with rasterio.open(filepath) as src:
    for val in src.sample(zip(lons, lats)):
        print(val)