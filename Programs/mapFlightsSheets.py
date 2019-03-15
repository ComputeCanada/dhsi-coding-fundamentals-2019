# Google spreadsheet/map of hometowns and travel routes
# instructions on how to do this with Sheets instead of a CSV: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# note: doing the mapping part with live Google API requires giving a credit card and being charged if go over the rate limit

# import libraries needed for program

import gmplot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use credentials to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# find a Google Sheets workbook by name and open the first sheet in the workbook

sheet = client.open("mapFlights").sheet1
latitude = sheet.col_values(1)
longitude = sheet.col_values(2)

# create and center map on the University of Victoria, zoom level 3

gmap = gmplot.GoogleMapPlotter(48.4634, -123.3117, 3)

# initialize and use a while loop to go through all the points in the lat/long arrays and plot on map

i = 0
while i < len(latitude):
	gmap.marker(float(latitude[i]),float(longitude[i]))
	i = i+1

# create map, save as map.html in the working directory

gmap.draw('map.html')