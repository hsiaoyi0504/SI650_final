# SI650_final

## Prerequisite
- [Pyserini](https://github.com/castorini/pyserini)
- Java 11

## Indexing command
``` bash
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -threads 1 -input ./preprocess/collection_json/ -index ./indexes/ -storePositions -storeDocvectors -storeRaw # default indexing using porter stemmer
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -stemmer none -threads 1 -input ./preprocess/collection_json/ -index ./indexes_without_stemming/ -storePositions -storeDocvectors -storeRaw # without using stemmer
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -stemmer krovetz -threads 1 -input ./preprocess/collection_json/ -index ./indexes_krovetz/ -storePositions -storeDocvectors -storeRaw # indexing using krovetz stemmer
python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -threads 1 -input ./preprocess/collection_json_ner/ -index ./indexes_ner/ -storePositions -storeDocvectors -storeRaw # default indexing using porter stemmer
```

## Run the evaluation script
``` bash
python evaluate.py
```

## How to run search engine website
``` bash
export FLASK_APP=search 
export FLASK_ENV=development 
flask run  # then, open the browser and go to http://localhost:5000
```
