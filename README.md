# SI650_final

## Indexing command
`python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -threads 1 -input ./collection_json/ -index ../indexes/ -storePositions -storeDocvectors -storeRaw`
