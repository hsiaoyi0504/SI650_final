import sys
from pyserini.search import SimpleSearcher
from evaluate.calculate_score import evaluation


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
# searcher.set_bm25(BM25_k1, BM25_b)
# searcher.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)

searcher_2 = SimpleSearcher('indexes/')
searcher_2.set_bm25(BM25_k1, BM25_b)

searcher_3 = SimpleSearcher('indexes/')
searcher_3.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)

searcher_4 = SimpleSearcher('indexes/')
searcher_4.set_bm25(BM25_k1, BM25_b)
searcher_4.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)

annotation = './evaluate/Annotations.csv'

print("Default:")
evaluation(searcher, annotation)

print("Enable RM3 query expansion:")
evaluation(searcher_3, annotation)


