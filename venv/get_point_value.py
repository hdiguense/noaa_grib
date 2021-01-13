#Diego Monge
#ldiego008@gmail.com

from osgeo import gdal
import sys
import numpy as np
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/rain/<year>/<coordinates>')
def avg_month_rain(coordinates, year):
    xy = escape(coordinates)
    y = float(coordinates.split(',')[0])
    x = float(coordinates.split(',')[1])
    point = [(y, x)]
    filepath = r'D:\noaa_grib\venv\lluvia\Lluvia_centro_america_' + str(escape(year)) + '.tif'

    raster = gdal.Open(filepath)

    #georeference info
    print('Getting raster info')
    cols = raster.RasterXSize
    rows = raster.RasterYSize

    transform = raster.GetGeoTransform()
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = transform[5]

    y = point[0][0]
    x = point[0][1]

    xOffset = int((x - xOrigin) / pixelWidth)
    yOffset = int((y - yOrigin) / pixelHeight)
    rain = []
    for mes in range(12):
        band = raster.GetRasterBand(mes + 1)
        print('raster to array month ' + str(mes +1))
        data = np.array(band.ReadAsArray(0, 0, cols, rows))
        value = data[yOffset, xOffset]
        print(xOffset, yOffset, value)
        rain.append(str(value))


    #return str(rain) + 'year: ' + str(escape(year))
    return render_template('lluvia.html', lluvia = ','.join(rain), anio = escape(year))