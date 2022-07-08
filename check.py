from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image 
import math
import rasterio
lulc = gdal.Open(r"C:/Users/samhi/Desktop/AHP Layers/soil_reclassify.tif")
lulcr = lulc.ReadAsArray()
lulc.GetProjection()

lulcr.shape
datars=np.array(Image.fromarray(lulcr).resize((14617,10519), Image.NEAREST))

datars.shape
final = "C:/Users/samhi/Desktop/AHP Layers/FINAL/soil.tif"
driver = gdal.GetDriverByName('GTiff')
dst_ds = driver.Create(final, xsize=14617, ysize=10519,
                       bands=1, eType=gdal.GDT_Float32)
out_band=dst_ds.GetRasterBand(1)
out_band.WriteArray(datars)
#clear cache
dst_ds.FlushCache()
dst_ds=None
del dst_ds
plt.imshow(datars)
