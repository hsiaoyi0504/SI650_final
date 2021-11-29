# SI650_final

## Indexing command
`python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocument -generator DocumentGenerator -threads 1 -input ./collection_json/ -index ../indexes/ -storePositions -storeDocvcetors -storeRaw`
