# SI650_final

## Indexing command
``` bash
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -threads 1 -input ./preprocess/collection_json/ -index ./indexes/ -storePositions -storeDocvectors -storeRaw # default indexing using porter stemmer
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -stemmer none -threads 1 -input ./preprocess/collection_json/ -index ./indexes_without_stemming/ -storePositions -storeDocvectors -storeRaw # without using stemmer
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -stemmer krovetz -threads 1 -input ./preprocess/collection_json/ -index ./indexes_krovetz/ -storePositions -storeDocvectors -storeRaw # indexing using krovetz stemmer
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -threads 1 -input ./preprocess/collection_json_ner/ -index ./indexes_ner/ -storePositions -storeDocvectors -storeRaw # default indexing using porter stemmer
```

## How to run search engine website
```
export FLASK_APP=search 
export FLASK_ENV=development 
flask run
```
Open localhost:5000
