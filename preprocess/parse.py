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
        if tables[2].find("td"):
            publication = tables[2].find("td").getText()
            publication_a = tables[2].find("a")
            if publication_a is not None:
                publication_url = publication_a['href']
                publication = publication.rstrip("[pubmed]")
            else:
                publication_url = ""
        else:
            publication = ""
            publication_url = ""
        keyword = tables[3].getText()[20:]
        row += [publication, publication_url, keyword]
        # row.append(keyword)
        df.append(row)
df = pd.DataFrame(df, columns=['id', 'Title', 'Description', 'HostingRepository', 'AnnounceDate',
                             'AnnouncementXML', 'DigitalObjectIdentifier', 'ReviewLevel',
                             'DatasetOrigin', 'RepositorySupport', 'PrimarySubmitter',
                             'SpeciesList', 'ModificationList', 'Instrument', 'Publication', 'PublicationURL', 'Keyword'])

df.to_csv('data_new.csv', index=False)
# with open('./HTMLdatasets.txt', 'w+') as f:
#     for line in datasets:
#         f.write(line+"\n")
