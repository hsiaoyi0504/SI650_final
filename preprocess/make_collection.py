import pandas as pd
import json
df = pd.read_csv('data.csv')
l = []
with open('./collection_json/documents.jsonl', 'w+') as f:
    for index, row in df.iterrows():
        dic = {'id':row['id'], 'contents': str(row['Title']) + str(row['Description'])}
        json.dump(dic, f)
        f.write("\n")

