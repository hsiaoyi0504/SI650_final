from pyserini.search import SimpleSearcher

searcher = SimpleSearcher('indexes/')
hits = searcher.search('liver')

for i in range(10):
    print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')