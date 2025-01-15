import rasterio
import numpy as np
from rasterio.transform import from_origin


def ndviCalculation(outputPath,B4_band,B8__band):

    with rasterio.open(B4_band) as red_band:
        B4 = red_band.read(1)
        # transform = B4.transform 
        profile = red_band.profile

    with rasterio.open(B8__band) as B8:
        B8 = B8.read(1)

    assert B4.shape == B8.shape

    ndvi = (B8 - B4) / (B8 + B4)

    height, width = ndvi.shape

    profile.update({
        'count': 1,  
        'dtype': 'float32',  
        'width': width, 
        'height': height,  
        'nodata': -9999,  
    })


    with rasterio.open(outputPath, 'w', **profile) as dst:
        dst.write(ndvi,1)
    print('Ndvi saved successfully')    

if __name__ == '__main__':

    outputPath = r"E:\Rushikesh\lstData\ndvi\Ndvi.tif"
    B4_band = r"E:\Rushikesh\lstData\ndviData\T50_B4.tif"
    B8__band = r"E:\Rushikesh\lstData\ndviData\T50_B8.tif"


    ndviCalculation(outputPath,B4_band,B8__band)



    