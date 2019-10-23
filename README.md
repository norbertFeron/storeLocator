# Store Locator 

This project contain python code to query coordinates from adresses via Google maps api or Geocode Nomatim, and leaftlet library to draw marker on a map.

## Coordinates query

![Excel source file](./img/excel.png)

### Requirements

```
pip install xlrd
pip install xlutils
```
and
```
pip install googlemaps
```
or 
```
pip install geopy
```

### Launch

Set your var and api key and launch:
```
python getLatLongGoogleMaps.py
python getLatLongNomatim.py
```

## leaflet maps

![Resulting map](./img/map.png)

### Marker-clustering

Leaflet marker clusturing is a submodule from https://github.com/Leaflet/Leaflet.markercluster

#### Requirements

Install jake `npm install -g jake` then run `npm install`

#### Demo

Open marker-clustering-resellers.html in your browser