## NZ AIP

First of all, I would like to thank and acknowledge this blog https://www.herbert.org.nz/?p=202 and the author of the post / script. While I have created a new script some of the ideas, naming conventions and structure has most defiantly been aided by this initial work getting the AIP into AirNavPro.

This script in its current form is geared towards producing a VFR AIP with many of the IFR charts excluded. The script should be very simple to modify for IFR purposes.

The script is written in Python3 with 'Beautiful Soup 4' being the only extra thing needed. Please be very mindful about not hammering the AIP site. It is important that you understand the AIP terms of use and you do not cause undue strain on the AIP web server or else it is very easy for them to block scripts like this.

It is also key that you use this for personal use as per the terms of the AIP. I would also include the usual disclaimer about not reliving on the data without verifying it and pilot responsibility etc.

### What do do
1. Install Python if you havn't already 
2. pip install -r requirements.txt
3. python new-get-aip.py
4. This should create a folder called 'aip' 
5. Rename 'aip' to 'byop'.
6. Place the byop folder in a folder name of your choice for example 'NZAIP 202302' 
7. zip this folder 

You have a file ready for importing into ForeFlight. Best of luck! 
 
