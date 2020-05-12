import requests
import json

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

from bs4 import BeautifulSoup

url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
linksko = []
for a in soup.find_all('a', href=True):
    if '/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/README.md' not in a['href'] and '/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/.gitignore' not in a['href']:
        if '/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/' in a['href']:
            linksko.append('https://github.com/'+a['href'])
            with open('links.json', 'w') as fp:
                json.dump(linksko, fp)
print('updatelinks done')

def retrieve():
    for link in linksko:
        filename= link.split('https://github.com//CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/')[1]
        req = requests.get(link)
        url_content = req.content
        csv_file = open('csv/'+filename, 'wb')
        csv_file.write(url_content)
        csv_file.close()

def get_latest():
    latestfile = linksko[-1]
    latestfilename= latestfile.split('https://github.com//CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/')[1]
    print(latestfilename)
