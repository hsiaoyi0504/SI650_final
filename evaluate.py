import sys
from pyserini.search import SimpleSearcher
from pyserini import analysis
from evaluate.calculate_score import evaluation


CUSTOMIZE_BM25 = True
QUERY_EXPANSION = False

# Customized parameters for BM25
BM25_k1 = 0.855 
BM25_b = 0.373

# Parameters for RM3 query_expansion
RM3_fb_terms = 5 # number of expansion terms.
RM3_fb_docs = 10 # number of expansion documents.
RM3_original_query_weight = 0.9 # weight to assign to the original query.

searcher = SimpleSearcher('indexes/')
# searcher.set_bm25(BM25_k1, BM25_b)
# searcher.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)
searcher_ner = SimpleSearcher('indexes_ner')

searcher_1 = SimpleSearcher('indexes_krovetz/')
analyzer_1 = analysis.get_lucene_analyzer(stemmer='krovetz')
searcher_1.set_analyzer(analyzer_1)

searcher_2 = SimpleSearcher('indexes/')
searcher_2.set_bm25(BM25_k1, BM25_b)

searcher_3 = SimpleSearcher('indexes/')
searcher_3.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

searcher_4 = SimpleSearcher('indexes/')
searcher_4.set_bm25(BM25_k1, BM25_b)
searcher_4.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

searcher_5 = SimpleSearcher('indexes_without_stemming/')
analyzer_5 = analysis.get_lucene_analyzer(stemming=False)
searcher_5.set_analyzer(analyzer_5)
searcher_5.set_bm25(BM25_k1, BM25_b)
searcher_5.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

annotation = './evaluate/Annotations.csv'

print("Default:")
evaluation(searcher, annotation)

print("-------------------------------------------------------------")
print("With NER:")
evaluation(searcher_ner, annotation)

stop
print("-------------------------------------------------------------")
print("BM25 with krovetz stemmer:")
evaluation(searcher_1, annotation)

# print("-------------------------------------------------------------")
# print("BM25 with customized parameters:")
# evaluation(searcher_2, annotation)

print("-------------------------------------------------------------")
print("Enable RM3 query expansion with default BM25 parameter:")
evaluation(searcher_3, annotation)

print("-------------------------------------------------------------")
print("Without stemming and RM3 query expansion")
evaluation(searcher_5, annotation)
