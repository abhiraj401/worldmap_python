# Modules
####################
import os
import sys
import folium
import pandas
####################

# Input
#############################
path=sys.argv
df=pandas.read_csv(path[1])
#############################

# Main code
#####################################################################################
map = folium.Map(location=[45.372, -122.697],zoom_start=4,tiles='Stamen Terrain')

for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
    map.simple_marker(location=[lat,lon],popup=name,marker_color='red')

map.create_map(path='test.html')
#####################################################################################
