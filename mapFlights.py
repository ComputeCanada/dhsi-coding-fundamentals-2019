# Google spreadsheet/map of hometowns and travel routes

import gmplot

# import place names, or in this stub, arbitrarily code in lat/long points

latitude = [0, 5, 10]
longitude = [0, 10, 5]

#center map of first lat/long point, zoom level 5

gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0], 5) 

# in theory can use scatter to make all the points at once, haven't been able to get this working yet
# gmap.scatter(latitude, longitude, '#FF66666', edge_width=10)

# initialize and use a while loop to go through all the points in the lat/long arrays and plot on map

i = 0
while i < len(latitude):
	gmap.marker(latitude[i],longitude[i])
	i = i+1

# create map, save as map.html in the working directory

gmap.draw('map.html')