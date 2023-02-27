# Aurora data to KML
Aurora data to KML is a simple script that converts the data from the NOAA Aurora Forecast website to a KML file that can be used in Google Earth.

## Usage
1. Download the script
2. Run the script with the following command: `python aurora.py`
3. The script will create a file called `ovation_aurora_latest.kml` and `ovation_aurora_latest_max.kml` in the same directory as the script.
4. Open one of the KML files in Google Earth. 

## Description
The script will download the latest data from the NOAA Aurora Forecast website and convert it to a KML file that can be used in Google Earth. The name of the KML points will be the intensity of the aurora.

## Requirements (Tested with)
* Python 3.10.10
* requests 2.28.2
* simplekml 1.3.6

## License
MIT License

## Disclaimer
This script is not affiliated with the NOAA Aurora Forecast website or Google Earth. The script is provided as is and the author is not responsible for any damage caused by the script.

## Author
* **Elias Sörstrand** - [elisor1219](https://github.com/elisor1219)