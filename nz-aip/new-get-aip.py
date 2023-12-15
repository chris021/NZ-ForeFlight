from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request 
import os
import shutil

AIPURL = "https://www.aip.net.nz/document-category/Aerodrome-Charts"
AIPBASEURL = "http://www.aip.net.nz/"
IFR_Keywords = ['VOR', 'RNAV', 'Standard Route Clearances', 'SID', 'ILS', 'Visual Arrivals', 'NDB', 'DME', 'RNP', 'Docking']
#if not any(word.lower() in asset.name.lower() for word in IFR_Keywords):

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
        fh = open('aip/' + icao.upper() + '_' + prefix + '_' + name + '.pdf', "wb")
        fh.write(response.read())
        fh.close()
    else:
        print("Error downloading file")



for airfield in airfields:
    try:
        ICAO_code = airfield.find('div', class_='col-lg-12')['ref'][7:]
    except:
        print("Error on: " + str(airfield))
        continue
    Airfield_Name = airfield.find('template', slot='header').contents[0]
    files = airfield.find_all('a')
    print(Airfield_Name)


    for file in files:
        File_Name = file.contents[1]
        File_URL = file.get('href')
        intA = File_Name.find(' — ') + 3
        File_Name_Short = File_Name[intA:].replace('/', '-').replace('—','-')

        if not any(word.lower() in File_Name.lower() for word in IFR_Keywords):
            print(File_Name)
            print(File_URL)
            print(File_Name_Short)
            print('-----------')
            #if any(word in File_Name for word in ['Kaitaia','Kerikeri','Whangarei','Auckland','Ardmore']):
            #    downloadAIP(File_URL, File_Name_Short, ICAO_code,"Airport")

            if File_Name.find('Ground') > 0:
                downloadAIP(File_URL, File_Name_Short, ICAO_code,"Ground")
        #    downloadAIP(File_URL, File_Name, ICAO_code,"VFR")
            elif File_Name.find('Arrival') > 0:   
                downloadAIP(File_URL, File_Name_Short, ICAO_code,"Arrival&Departure")
            elif File_Name.find('Departure') > 0:
                downloadAIP(File_URL, File_Name_Short, ICAO_code,"Arrival&Departure")
            else:
                downloadAIP(File_URL, File_Name_Short, ICAO_code,"Airport")
    #except:
        #print(airfield)
        #pass

#print(airfields[2])

