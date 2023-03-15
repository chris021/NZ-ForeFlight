from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request 
import os
import shutil

AIPURL = "https://www.aip.net.nz/document-category/Aerodrome-Charts"
AIPBASEURL = "http://www.aip.net.nz/"


cj = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
response = opener.open('https://www.aip.net.nz/disclaimer/setCookie')

response = opener.open(AIPURL)
if response.code != 200:
   print("Error connecting to AIP site")
else:
   print("Successfully connected to AIP site")

html_doc = response.read().decode(response.headers.get_content_charset())
soup = BeautifulSoup(html_doc, 'html.parser')


airfields = soup.find_all('div', class_="row")[1:]

#print(airfields[2].find('div', class_='col-lg-12')['ref'][7:])
#print(airfields[2].find('template', slot='header').contents[0])

if os.path.exists('aip'):
  shutil.rmtree('aip')
if not os.path.exists('aip'):
   os.mkdir('aip')



#         if not any(word.lower() in asset.name.lower() for word in IFR_Keywords):
            #response = urllib2.urlopen(asset.url)


def downloadAIP(url, name, icao ,prefix=''):
    response = opener.open(AIPBASEURL + url)
    print(response)
    if response.code == 200:
        fh = open(os.path.normcase('aip/' + icao + '_' + prefix + '_' + url.rsplit('/', 1)[-1]), "wb")
        fh.write(response.read())
        fh.close()
    else:
        print("Error downloading file")



for airfield in airfields:
    ICAO_code = airfield.find('div', class_='col-lg-12')['ref'][7:]
    Airfield_Name = airfield.find('template', slot='header').contents[0]
    files = airfield.find_all('a')
    print(Airfield_Name)

    for file in files:
        File_Name = file.contents[1]
        File_URL = file.get('href')

        if File_Name.find('VFR') > 0:
            print('VFR')
            downloadAIP(File_URL, File_Name, ICAO_code,"VFR")
        elif File_Name.find('Ground') > 0:   
            print('Taxi')
            downloadAIP(File_URL, File_Name, ICAO_code,"TAXI")
        elif File_Name.find('Arrival') > 0:
            print('Arrival')
        elif File_Name.find('Departure') > 0:
            print('Departure')
        elif File_Name.find('Aerodrome') > 0:
            print('Aerodrome')
            downloadAIP(File_URL, File_Name, ICAO_code,"AIRPORT")
        elif File_Name.find('Operational') > 0:
            print('Operational')
            downloadAIP(File_URL, File_Name, ICAO_code,"AIRPORT")
        elif File_Name.find('Noise') > 0:
            print('Noise')            
        print('------------------------------')
    #except:
        #print(airfield)
        pass

#print(airfields[2])

