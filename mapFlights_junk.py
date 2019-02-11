# Google spreadsheet/map of hometowns and travel routes

import json
import gspread
import gmaps
from oauth2client.client import SignedJwtAssertionCredentials

# json_key = json.load(open('creds.json'))
# scope = ['https://spreadsheets.google.com/feeds']
# credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
# file = gspread.authorize(credentials)
# sheet = file.open("DHSI2019-Hometowns").sheet1
# hometowns = sheet.col_values(1)

import gmplot

# import place names

latitude = []
longitude = []

gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0])
gmap.scatter(latitude, longitude, '#FF66666', edge_width=10)
gmap.draw('map.html')