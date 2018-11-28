# Google spreadsheet/map of hometowns and travel routes
# instructions on how to do this with Sheets instead of a CSV: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# note: doing this with live Google API requires giving a credit card and being charged if go over the rate limit

# import libraries needed for program

import gmplot
import csv

# open csv file of places and read in the latitudes/longitudes; originalDatesReader is a list of lists

placesFile = open("places.csv")
placesReader = csv.reader(placesFile)

# create and center map on the University of Victoria, zoom level 3

gmap = gmplot.GoogleMapPlotter(48.4634, -123.3117, 3)

# create lists of latitudes and longitudes
# we are looping through each list in placesReader

for location in placesReader:
	gmap.marker(float(location[0]), float(location[1]))

##this was the original code for an arbitrary set of lat/long points
#latitude = [0, 5, 10]
#longitude = [0, 10, 5]
#
##center map of first lat/long point, zoom level 5
#
#gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0], 5) 
#
## in theory can use scatter to make all the points at once, haven't been able to get this working yet
## gmap.scatter(latitude, longitude, '#FF66666', edge_width=10)
#
## initialize and use a while loop to go through all the points in the lat/long arrays and plot on map
#
#i = 0
#while i < len(latitude):
#	gmap.marker(latitude[i],longitude[i])
#	i = i+1

# create map, save as map.html in the working directory

gmap.draw('map.html')

# close the files so we don't accidentally corrupt them or crash something
placesFile.close()