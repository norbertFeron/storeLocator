import googlemaps
import xlrd 
from xlutils.copy import copy

gmaps = googlemaps.Client(key='YourGoogleApiKey') # Need geocoding api access
excelFile = "resellers.xls"

# open your resellers list
myBook = xlrd.open_workbook(excelFile,formatting_info=True)
mySheet = myBook.sheet_by_index(0)
# make a copy for saving coordinates to excel
wb = copy(myBook)

# js file for leaflet map
file = open('resellers.js','w') 
file.write('var addressPoints = [') 

row = mySheet.row(0)
errors = []
for row_idx in range(1, mySheet.nrows):   
    find = False
    # to be set in function of your xls
    name = mySheet.cell(row_idx, 0).value
    adress = mySheet.cell(row_idx, 1).value
    postal_code = mySheet.cell(row_idx, 2).value
    city = mySheet.cell(row_idx, 3).value
    country = mySheet.cell(row_idx, 4).value
    lat = mySheet.cell(row_idx, 5).value
    long = mySheet.cell(row_idx, 6).value

    # check if lat and long already defined
    if lat and long:
        find = True
        loc = gmaps.reverse_geocode((lat, long))
    while not find:
        print('Searching: %s' % name)
        try:
            # asking google latitude and longitude 
            loc = gmaps.geocode(adress + ', ' + postal_code + '' + city +', ' + country)
            find = True
        except Exception as inst:
            print(inst)
    if loc[0]:
        if not (lat and long): # Save coordinates to xls 
            wb.get_sheet(0).write(row_idx, 5, loc[0]['geometry']['location']['lat'])
            wb.get_sheet(0).write(row_idx, 6, loc[0]['geometry']['location']['lng'])
        # write entry to js file for leaflet map
        if row_idx == mySheet.nrows - 1: # last entry
            file.write('[%s, %s, "%s %s, %s"]' % (str(loc[0]['geometry']['location']['lat']), str(loc[0]['geometry']['location']['lng']), name, adress, city))
        else:
            file.write('[%s, %s, "%s %s, %s"],' % (str(loc[0]['geometry']['location']['lat']), str(loc[0]['geometry']['location']['lng']), name, adress, city))
        print ('Store: %s Lat: %s Long : %s' % (name, str(loc[0]['geometry']['location']['lat']), str(loc[0]['geometry']['location']['lng'])))
    else:
        print ('ERROR On Store: %s Row : %s' % (name, str(row_idx +1)))
        errors.append('ERROR On Store: %s Row : %s' % (name, str(row_idx +1)))
print('-------------------------------------')
print('Automatic latitude/longitude fail on:')
for error in errors:
    print(error)
file.write('];') 
file.close()
# Save xls result with latitude and longitude
wb.save(excelFile)

