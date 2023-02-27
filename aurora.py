import json
import simplekml
import requests

def main():
    downloadLatestAuroraData()

    with open('ovation_aurora_latest.json') as f:
        data = json.load(f)

    coordinates = data['coordinates']
    kml = simplekml.Kml()
    kmlMax = simplekml.Kml()
    maxIntensity = 0
    lonMax = 0
    latMax = 0
    for coord in coordinates:
        # Find the maximum intensity
        if coord[2] > maxIntensity:
            maxIntensity = coord[2]
            lonMax = coord[0]
            latMax = coord[1]

        # Save the non-zero coordinates to a json file
        # And also only the coordinates above the equator
        if coord[2] != 0 and coord[1] > 0:
                kml.newpoint(name=coord[2], coords=[(coord[0], coord[1])])

    kmlMax.newpoint(name=maxIntensity, coords=[(lonMax, latMax)])
    kmlMax.save('ovation_aurora_latest_max.kml')
    kml.save('ovation_aurora_latest.kml')

def downloadLatestAuroraData():
    url = 'https://services.swpc.noaa.gov/json/ovation_aurora_latest.json'
    r = requests.get(url, allow_redirects=False)
    open('ovation_aurora_latest.json', 'wb').write(r.content)

if __name__ == '__main__':
    main()

