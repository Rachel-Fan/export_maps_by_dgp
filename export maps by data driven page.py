import sys
import os
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser
import arcpy
import time



print time.strftime("%m-%d %X",time.localtime())+ " Exporting on. This may take a while."


mxd = arcpy.mapping.MapDocument(r"U:\20287030082\studies\MAP.REG02.101.08_Upper_Hudson_NY\production\discovery\templates\Information Exchange Map_Land_Layout_34x22_miles.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    fieldValue = mxd.dataDrivenPages.pageRow.POL_NAME3
    print time.strftime("%m-%d %X",time.localtime())+ " Start exporting page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))

    arcpy.mapping.ExportToPDF(mxd, r"U:\20287030082\studies\MAP.REG02.101.08_Upper_Hudson_NY\production\discovery\templates\PDF\HighQuality\Town_of_" + str(fieldValue) + "_Information_Exchange_Map.pdf",{},640,480,200,"BEST",)
    print time.strftime("%m-%d %X",time.localtime())+ str(fieldValue)+" Exported page {0} of {1} ".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))

print time.strftime("%m-%d %X",time.localtime())+ " Exporting finishes!"

