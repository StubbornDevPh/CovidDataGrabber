import json
import requests

full_links = []
with open('links.json', 'r') as f:
    links = json.load(f)

for link in links:
    full_links.append('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+link)

for full_link in full_links:
    filename = full_link.split('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/')[1]
    req = requests.get(full_link)
    url_content = req.content
    csv_file = open('csv/'+filename, 'wb')
    csv_file.write(url_content)
    csv_file.close()
