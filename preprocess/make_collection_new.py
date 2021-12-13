import pandas as pd
import json
df = pd.read_csv('data_new.csv')

with open('./collection_json_new/documents.jsonl', 'w+') as f:
    for index, row in df.iterrows():
        dic = {'id':row['id'], 'contents': (str(row['Title']) + ' ')*2 + str(row['Description']) + ' ' + ' '.join([each.strip() for each in str(row['Keyword']).split(',')])}
        json.dump(dic, f)
        f.write("\n")

