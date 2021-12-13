import sys
from pyserini.search import SimpleSearcher
from pyserini import analysis
from pygaggle.rerank.transformer import MonoT5
from pygaggle.rerank.transformer import MonoBERT
from evaluate.calculate_score import evaluation


CUSTOMIZE_BM25 = True
QUERY_EXPANSION = False

# Customized parameters for BM25
BM25_k1 = 0.7
BM25_b = 0.315

# Customized parameters for QE_BM25
QE_BM25_k1 = 0.54
QE_BM25_b = 0.32

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
searcher_5.set_bm25(QE_BM25_k1, QE_BM25_b)
searcher_5.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

searcher_6 = SimpleSearcher('indexes/')
searcher_6.set_bm25(BM25_k1, BM25_b)
searcher_6.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

# reranker = MonoT5()
reranker = MonoBERT()

annotation = './evaluate/Annotations.csv'

print("Default:")
evaluation(searcher, annotation)
print("-------------------------------------------------------------")
print("BM25 with customized parameters:")
print(f'k1:{BM25_k1}, b:{BM25_b}')
evaluation(searcher_2, annotation)
print("-------------------------------------------------------------")
print("With NER:")
evaluation(searcher_ner, annotation)

print("-------------------------------------------------------------")
print("BM25 with krovetz stemmer:")
evaluation(searcher_1, annotation)



print("-------------------------------------------------------------")
print("Enable RM3 query expansion with default BM25 parameter:")
evaluation(searcher_3, annotation)

# print("-------------------------------------------------------------")
# print("Enable RM3 query expansion with customized BM25 parameter:")
# print(f'k1:{QE_BM25_k1}, b:{QE_BM25_b}')
# evaluation(searcher_4, annotation)

print("-------------------------------------------------------------")
print("Without stemming and RM3 query expansion with customized BM25 parameter:")
print(f'k1:{QE_BM25_k1}, b:{QE_BM25_b}')
evaluation(searcher_5, annotation)

print("-------------------------------------------------------------")
print("Without stemming and RM3 query expansion with customized BM25 parameter and reranker:")
print(f'k1:{QE_BM25_k1}, b:{QE_BM25_b}')
evaluation(searcher_5, annotation, reranker=reranker)
