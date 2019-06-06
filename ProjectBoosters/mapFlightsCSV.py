# Google spreadsheet/map of hometowns and travel routes
# instructions on how to do this with Sheets instead of a CSV: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# note: doing the mapping part with live Google API requires giving a credit card and being charged if go over the rate limit

# import libraries needed for program

import gmplot
import csv

# open csv file of places and read in the latitudes/longitudes; placesReader is a list of lists, that is a list of paired coordinates [lat, long]

placesFile = open("places.csv")
placesReader = csv.reader(placesFile)

# create and center map on the University of Victoria, zoom level 3

gmap = gmplot.GoogleMapPlotter(48.4634, -123.3117, 3)

# create lists of latitudes and longitudes
# we are looping through each list [lat, long] in placesReader

for location in placesReader:
	gmap.marker(float(location[0]), float(location[1]))

# create map, save as map.html in the working directory

gmap.draw('map.html')

# close the files so we don't accidentally corrupt them or crash something
placesFile.close()