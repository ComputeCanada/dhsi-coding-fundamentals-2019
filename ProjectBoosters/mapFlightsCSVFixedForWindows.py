# Google spreadsheet/map of hometowns and travel routes
# instructions on how to do this with Sheets instead of a CSV: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# note: doing the mapping part with live Google API requires giving a credit card and being charged if go over the rate limit

# documentation for the gmplot library is here: https://github.com/vgm64/gmplot
# additional options are here: https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/


# import libraries needed for program

import gmplot
import csv
from sys import platform
import re

# open csv file of places and read in the latitudes/longitudes; placesReader is a list of lists, that is a list of paired coordinates [lat, long]

placesFile = open("places.csv")
placesReader = csv.reader(placesFile)

# create and center map on the University of Victoria, zoom level 3

#gmap = gmplot.GoogleMapPlotter.from_geocode("San Francisco")

gmap = gmplot.GoogleMapPlotter(48.4634, -123.3117, 3)

# create lists of latitudes and longitudes
# we are looping through each list [lat, long] in placesReader
# we are also adding a TITLE that is the third column from the spreadsheet and includes human-readable names: this will be visible on hover-over
# we are also adding a conditional statement to change the color of the marker if an (attribute) condition in a fourth column is satisfied

for location in placesReader:
    if location[3] == "AWESOME":
        gmap.marker(float(location[0]), float(location[1]), 'cornflowerblue', title=location[2])
    else:
        gmap.marker(float(location[0]), float(location[1]), title=location[2])

# create map, save as map.html in the working directory

gmap.draw('map.html')

# close the files so we don't accidentally corrupt them or crash something
placesFile.close()

# check to see if the machine running this is a windows machine - if it is, then use regular expressions to fix the backwards html slashes
if platform == "win32" or platform == "cygwin" or platform == "msys":
    with open('map.html','r') as originalMapFile:
        with open('map-clean.html','w') as cleanMapFile:
            for line in originalMapFile:
                cleanMapFile.write(re.sub(r'\\','/',line)+'\n')