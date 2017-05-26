import folium, pandas
map=folium.Map(location=[45.372,-121.697],zoom_start=4,tiles='Stamen Terrain')
df=pandas.read_csv("Volcanoes-USA.txt")
for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
    folium.Marker(location=[lat,lon],popup=name).add_to(map)
map.save('Volcanoes_1.html')
