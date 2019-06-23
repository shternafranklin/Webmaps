import folium
import pandas

#This is how you would set up a map

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

#add elements to the map
#map.add_child(folium.Marker(location=[80,-100], popup="Hi I am marker", icon=folium.Icon(color='green'))) #add children to the map

# a different approach is adding a feature group
fg = folium.FeatureGroup(name="My Map")
#add it to the feature object - keeps code organized
#fg.add_child(folium.Marker(location=[38.58,-99.09], popup="Hi I am marker", icon=folium.Icon(color='green'))) #add

#add a forloop to add multiple markers
for coordinates in :
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am marker", icon=folium.Icon(color='green'))) #add

map.add_child(fg)

map.save("Map2.html")
