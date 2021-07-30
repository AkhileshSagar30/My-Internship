import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
# Reading the Excel File
excel_df = pd.read_excel('Comb_Data.xlsx')
df = pd.DataFrame(excel_df)
# Creating GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Giving Diff colors to diff cities
ax1= world.plot(color='white',edgecolor='black')
ax2= world.plot(color='springgreen',edgecolor='darkgreen')
# Adding different colors to diff company names with LEGEND
gdf.plot(ax=ax1, color='orangered')
# COLORS-Spectral,hot,hsv,plasma,jet,RdYlGn,YlOrGn,gist_stern,BrBG,seismic,coolwarm
gdf.plot(ax=ax2, column='CO2emissions',cmap='gist_stern',legend=True, legend_kwds={'label':'CO2 Emissions'})

plt.show()
