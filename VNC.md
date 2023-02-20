### NZ VNC Creation

ForeFlight supports the addition of custom charts. This guide will explain at a high level the steps that are needed to take the purchased VNC tiles and convert the into something usable in ForeFlight. This process is a little bit complex and does require a computer with a fair amount of processor and RAM. The uncompressed raw VNC is about 10GB and ideally you want to be able to fit that in memory. 

Some background on why this is a bit complex: 

The Tiles from the AIP shop are in NZGD2000 New Zealand Transverse Mercator 2000 (EPSG:2193) this isn't going to work for the format we need which is mbtiles. MBtiles needs EPSG:3857 (WGS 84 / Web Mercator projection) not to be confused with regular WGS 84 (EPSG:4326)! To make matters worse the extent of NZGD2000 crosses over the edge of the map to wrap around to the other side of the world. QGIS does NOT like this at all and this causes a number of issues. To get around this I used an intermediate projection WGS 84 / PDC Mercator (EPSG:3832) then trim east from about 179.6 Degrees E, just before it becomes W! There isn't anything much of interest in the VNC out there, just some boundaries which are contained in the ForeFlight data anyway. 

Each time you reproject (Warp) you can choose to save a new file, this will be about 10GB each time or you can just use a temp / memory file. To start with you don't need to merge the GeoTiff tiles you can use the layer as loaded. 

The steps:

1. Purchase the Tiles from the AIP store

https://shop.aeropath.aero/collections/digital-visual-navigation-charts-2022-2023/products/digital-visual-navigation-charts-1-250-000-scale-chart-areas-effective-1-december-2022?variant=43837479354538

> **_NOTE:_** You must select GeoTiff MAP Tiles! 

2. Download and extract the Tiles.
3. Open this file in your GIS package. I used QGIS for this process. 
4. OPTIONAL: In QGIS there is the concept of pyramids. This makes lower resolution copies at lower zoom levels and stops QGIS hanging as much. Right click on the layer, select pyramids, choose some resolutions and click Build pyramids. 
5. WARP to WGS 84 / PDC Mercator (EPSG:3832) (WARP tool is in processing tool box)
6. Clip Raster by extent (also in the tool box) to crop out anything further East of 179.9 Degrees
7. WARP to WGS 84 / Web Mercator projection (EPSG:3857)
8. Generate XYZ Tiles (in the tool box) 

All going to plan you should have about a 950Mb file or less which you can import into ForeFlight! 





