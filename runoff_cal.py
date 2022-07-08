from osgeo import gdal
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
lulc = gdal.Open(r"C:/Users/samhi/Desktop/data/lulc.tif")
lulcr = lulc.ReadAsArray()
lulc.GetProjection()
# # plt.imshow(lulcr)
soil= gdal.Open(r"C:/Users/samhi/Desktop/data/RasterSoil.tif")
soilr = soil.ReadAsArray()
soil.GetProjection()
# plt.imshow(soilr)
# lulcr.shape
soilr.shape
soilrs=np.array(Image.fromarray(soilr).resize((14617,10519), Image.NEAREST))
soilrs.shape
plt.imshow(soilrs)
narray=np.zeros((10519,14617))

for i in range(10519):
  for j in range(14617):
    if (lulcr[i,j]==15 and soilrs[i,j]==0):
      narray[i,j]=-1
    elif(lulcr[i,j]<=1 and soilrs[i,j]==1):
      narray[i,j]=0
    elif(lulcr[i,j]<=2 and soilrs[i,j]==1):
      narray[i,j]=70
    elif(lulcr[i,j]<=4 and soilrs[i,j]==1):
      narray[i,j]=77
    elif(lulcr[i,j]<=5 and soilrs[i,j]==1):
      narray[i,j]=88
    elif(lulcr[i,j]<=6 and soilrs[i,j]==1):
      narray[i,j]=89
    elif(lulcr[i,j]<=7 and soilrs[i,j]==1):
      narray[i,j]=79
    elif(lulcr[i,j]<=11 and soilrs[i,j]==1):
      narray[i,j]=86
    elif(lulcr[i,j]<=1 and soilrs[i,j]==2):
      narray[i,j]=0
    elif(lulcr[i,j]<=2 and soilrs[i,j]==2):
      narray[i,j]=77
    elif(lulcr[i,j]<=4 and soilrs[i,j]==2):
      narray[i,j]=83
    elif(lulcr[i,j]<=5 and soilrs[i,j]==2):
      narray[i,j]=91
    elif(lulcr[i,j]<=6 and soilrs[i,j]==2):
      narray[i,j]=91
    elif(lulcr[i,j]<=7 and soilrs[i,j]==2):
      narray[i,j]=84
    elif(lulcr[i,j]<=11 and soilrs[i,j]==2):
      narray[i,j]=89
    j+=1
  i+=1
rainfall = gdal.Open(r"C:/Users/samhi/Desktop/data/Rainfallr.tif")
rainfallr = rainfall.ReadAsArray()
rainfall.GetProjection()
rainfallrep = "C:/Users/samhi/Desktop/data/rainfallrep.tif"

reprj = gdal.Warp(rainfallrep, rainfall, dstSRS = "EPSG:32643")
reprj= None 
# reprj.GetProjection()


rainfall = gdal.Open(r"C:/Users/samhi/Desktop/data/rainfallrep.tif")
rainfallr = rainfall.ReadAsArray()


plt.imshow(rainfallr)
rainfallrs.shape
rainfallrs=np.array(Image.fromarray(rainfallr).resize((14617,10519), Image.NEAREST))

plt.imshow(rainfallrs)
#Save CN image as tif
CN_II = "C:/Users/samhi/Desktop/data/curvenum.tif"
driver = gdal.GetDriverByName('GTiff')
dst_ds = driver.Create(CN_II, xsize=14617, ysize=10519,
                       bands=1, eType=gdal.GDT_Float32)
dst_ds.SetProjection("EPSG:32643")
out_band=dst_ds.GetRasterBand(1)
out_band.WriteArray(narray)
#clear cache
dst_ds.FlushCache()
dst_ds=None
del dst_ds





 print(narray)
print(narray.shape)
CN_II = gdal.Open(r"C:/Users/samhi/Desktop/data/curvenum.tif")
CN_r = CN_II.ReadAsArray()
print(CN_r)
CN= ((4.2*CN_r)/(10-0.058*CN_r))
S = ((25400/CN)-254)
R = ((rainfallrs-(0.2*S))*(rainfallrs-(0.2*S)))/(rainfallrs+(0.8*S))
runoff = "C:/Users/samhi/Desktop/data/runoff.tif"
driver = gdal.GetDriverByName('GTiff')
dst_ds = driver.Create(runoff, xsize=14617, ysize=10519,
                       bands=1, eType=gdal.GDT_Float32)
dst_ds.SetProjection("EPSG:32643")
out_band=dst_ds.GetRasterBand(1)
out_band.WriteArray(R)
#clear cache
dst_ds.FlushCache()
dst_ds=None
del dst_ds 
print(R)
