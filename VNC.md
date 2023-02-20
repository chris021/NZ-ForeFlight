### NZ VNC Creation

ForeFlight supports the addition of custom charts. This guide will explain at a high level the steps that are needed to take the purchased VNC tiles and convert the into something usable in ForeFlight. This process is a little bit complex and does require a computer with a fair amount of processor and RAM. The uncompressed raw VNC is about 10GB and ideally you want to be able to fit that in memory. 

1. Purchase the Tiles from the AIP store

https://shop.aeropath.aero/collections/digital-visual-navigation-charts-2022-2023/products/digital-visual-navigation-charts-1-250-000-scale-chart-areas-effective-1-december-2022?variant=43837479354538

You must select GeoTiff MAP Tiles! 

2. Download and extract the Tiles.
3. Open this file in your GIS package. I used QGIS for this process. 
4. In QGIS there is the concept of pyramids. This makes lower resolution copies at lower zoom levels. 

The Tiles are in NZGD200 New Zealand Transverse Mercator 2000 (EPSG:2193) this isn't going to work for the format we need which is mbtiles. MBtiles needs EPSG:3857 (WGS 84 / Web Mercator projection) not to be confused with regular WGS 84 (EPSG:4326)!



