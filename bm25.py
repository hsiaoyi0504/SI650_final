import sys
from pyserini.search import SimpleSearcher
from pyserini.analysis import Analyzer, get_lucene_analyzer


DEBUG = True
CUSTOMIZE_BM25 = True
QUERY_EXPANSION = False

# Parameters for BM25
BM25_k1 = 0.9 
BM25_b = 0.4

# Parameters for RM3 query_expansion
RM3_fb_terms = 10 # number of expansion terms.
RM3_fb_docs = 10 # number of expansion documents.
RM3_original_query_weight = 0.5 # weight to assign to the original query.

searcher = SimpleSearcher('indexes/')

if CUSTOMIZE_BM25:
    searcher.set_bm25(BM25_k1, BM25_b)
if QUERY_EXPANSION:
    searcher.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)

hits = searcher.search(sys.argv[1])

if DEBUG:
    analyzer = Analyzer(get_lucene_analyzer())
    tokens = analyzer.analyze(sys.argv[1])
    print(tokens)
    print("------------------------------")

for i in range(min(len(hits), 10)):
    print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')
