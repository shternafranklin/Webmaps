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
fg = folium.FeatureGroup(name="My Map")

#Need to go through each list 
for lt, ln, el,name in zip(lat, lon, elev, name): #need to use zip because it will combine it as the same time
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], 
        popup=folium.Popup(iframe), 
 #adding different colors of markers based on elevation
 #create a function that returns the str based on the elevation
        icon = folium.Icon(color=color_producer(el))))


map.add_child(fg)
map.save("Map3.html")
