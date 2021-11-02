import requests
import json
import concurrent.futures

def crawl(i):
    print(i)
    # for i in range(1, 10):
    response = requests.get(
        "http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD{:06d}".format(i))
    with open('../html/PXD{:06d}.html'.format(i), 'w+') as f:
        f.write(response.text)

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(crawl,range(1,29446))