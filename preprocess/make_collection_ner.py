import json

import spacy
import scispacy
from scispacy.linking import EntityLinker

import pandas as pd

nlp = spacy.load("en_ner_bc5cdr_md")
# nlp = spacy.load('en_core_web_lg')
# nlp = spacy.load("en_core_sci_sm")
# nlp = spacy.load("en_core_sci_lg")
nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls", "max_entities_per_mention": 1})
linker = nlp.get_pipe("scispacy_linker")

df = pd.read_csv('data.csv')
l = []
with open('./collection_json_ner/documents.jsonl', 'w+') as f:
    for index, row in df.iterrows():
        dic = {'id':row['id'], 'contents': str(row['Title']) + ' ' + str(row['Description']), 'NER': {}}
        doc = nlp(str(row['Title']) + ' ' + str(row['Description']))
        for entity in doc.ents:
            if entity.label_ in dic['NER']:
                if entity.text not in dic['NER'][entity.label_]:
                    dic['NER'][entity.label_].append(entity.text)
            else:
                dic['NER'][entity.label_] = [ entity.text ]
            # print("Entity:", entity)
            # print(entity.text, entity.start_char, entity.end_char, entity.label_)
            # print(entity.label_)
            # print(len(entity._.kb_ents))
            # for umls_ent in entity._.kb_ents:
            #    print(linker.kb.cui_to_entity[umls_ent[0]])
            # break
        # for ent in doc.ents:
        #    print(ent.text, ent.start_char, ent.end_char, ent.label_)
        json.dump(dic, f)
        f.write("\n")

