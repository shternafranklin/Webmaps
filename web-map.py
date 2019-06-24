import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"]) #added elevation to make the popup dyanmic
name = list(data["NAME"])

html = """
Volcano name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#Create function before the expression
def color_producer(elevation):
    if elevation < 1000:
       return 'purple'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=5, title="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")

#created a new feature group for layer control
fgp = folium.FeatureGroup(name="Population")



#Need to go through each list 
for lt, ln, el,name in zip(lat, lon, elev, name): #need to use zip because it will combine it as the same time
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt, ln], 
        popup=folium.Popup(iframe),
 #adding different colors of markers based on elevation
 #create a function that returns the str based on the elevation
        icon = folium.Icon(color=color_producer(el))))


#add more dimension to the map - Polygon
#add style that colors the map based on population

fgp.add_child(folium.GeoJson(data=open('world.json','r', 
encoding='utf-8-sig').read(),
#lambda functions are just functions but in a single line
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 1000000 
else 'oranange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child((fgp))

#add an element that tuns on/off these base layers - use layerControl class of folium
map.add_child(folium.LayerControl()) #you dont want to use this because it can turn off all the features 
#so make separate feature groups for each layer

map.save("Map3.html")
