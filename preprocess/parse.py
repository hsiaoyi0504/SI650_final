from bs4 import BeautifulSoup
import pandas as pd
datasets = []
df = []
for i in range(1,29446):
    with open('../html/PXD{:06d}.html'.format(i), 'r') as f:
        if i%1000==0:
            print(i)
        data = f.read()
        soup = BeautifulSoup(data, "html.parser")
        tables = soup.find_all("table", class_="dataset-summary")
        if not tables:
            continue
        datasets.append('PXD{:06d}.html'.format(i))

        summary = tables[0]
        summary = summary.find_all("td")
        row = ['PXD{:06d}'.format(i)]+[summary[i].getText() for i in range(1,26,2)]
        # print(tables[2])
        # publication = tables[2].find("td").getText()
        keyword = tables[3].getText()[20:]
        # row += [publication, keyword]
        row.append(keyword)
        df.append(row)
df = pd.DataFrame(df, columns=['id', 'Title', 'Desciption', 'HostingRepository', 'AnnounceDate',
                             'AnnouncementXML', 'DigitalObjectIdentifier', 'ReviewLevel',
                             'DatasetOrigin', 'RepositorySupport', 'PrimarySubmitter',
                             'SpeciesList', 'ModificationList', 'Instrument', 'Keyword'])

df.to_csv('data.csv', index=False)
with open('./HTMLdatasets.txt', 'w+') as f:
    for line in datasets:
        f.write(line+"\n")