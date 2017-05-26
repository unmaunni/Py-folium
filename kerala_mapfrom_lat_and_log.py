import folium
from geopy.geocoders import Nominatim
nom=Nominatim()
location=nom.geocode("Thrissur,kerala,india")
#print(str(location.latitude)+ " " + str(location.longitude))
lat=location.latitude
log=location.longitude
#to get the map
map=folium.Map(location=[lat,log],zoom_start=12)
map.save("kerala.html")
#in terrain form
map1=folium.Map(location=[lat,log],zoom_start=14,tiles='Stamen Terrain')
map1.save("keralaterrain.html")
#To add markers to map
map2=folium.Map(location=[lat,log],zoom_start=10)
folium.Marker(location=[10.5243,76.214],popup='Vadakkunnathan temple').add_to(map2)
folium.Marker(location=[10.094,76.493],popup="Unma's residence").add_to(map2)
map2.save("keralaMarker.html")
