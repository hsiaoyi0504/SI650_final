import requests
from bs4 import BeautifulSoup
import json

for i in range(1, 29446):
    response = requests.get(
    "http://proteomecentral.proteomexchange.org/api/proxi/v0.1/datasets/PXD{:06d}".format(i))
    data = response.json()
    if data.get('status'):
        continue
    with open('../json/PXD{:06d}.json'.format(i), 'w+') as f:
        json.dump(data, f)


