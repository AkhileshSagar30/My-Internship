import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Reading the excel data using pandas
excel_df = pd.read_excel('Comb_Data.xlsx')

print('\nThis is the data taken from the EXCEL SHEET.\n')
print(excel_df.head())

# Creating A DataFrame
df = pd.DataFrame(excel_df)
pd.set_option('display.max_rows',None)
pd.set_option('display.width',None)

# Creating GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
# Ensure that in GeoDataFrame the geometry takes 'longitude' first then 'latitude'

print("\nThis is Geo-DataFrame Representation: \n")
print(gdf.head())

# Plotting the coordinates on the Map.
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot()#color='skyblue', edgecolor='black')

gdf.plot(ax=ax, color='red')
plt.show()
