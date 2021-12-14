import sys
from pyserini.search import SimpleSearcher
from pyserini import analysis
from evaluate.calculate_score import evaluation

CUSTOMIZE_BM25 = True
QUERY_EXPANSION = False

# Customized parameters for BM25
BM25_k1 = 0.7
BM25_b = 0.32

# Customized parameters for QE_BM25
QE_BM25_k1 = 0.75
QE_BM25_b = 0.28

without_stem_QE_BM25_k1 = 0.54
without_stem_QE_BM25_b = 0.32

# Parameters for RM3 query_expansion
RM3_fb_terms = 5 # number of expansion terms.
RM3_fb_docs = 10 # number of expansion documents.
RM3_original_query_weight = 0.9 # weight to assign to the original query.

searcher = SimpleSearcher('indexes/')
# searcher.set_bm25(BM25_k1, BM25_b)
# searcher.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)
searcher_ner = SimpleSearcher('indexes_ner')

searcher_1 = SimpleSearcher('indexes/')
searcher_1.set_bm25(BM25_k1, BM25_b)

searcher_2 = SimpleSearcher('indexes_krovetz/')
analyzer_2 = analysis.get_lucene_analyzer(stemmer='krovetz')
searcher_2.set_analyzer(analyzer_2)

searcher_3 = SimpleSearcher('indexes_without_stemming/')
analyzer_3 = analysis.get_lucene_analyzer(stemming=False)
searcher_3.set_analyzer(analyzer_3)

searcher_4 = SimpleSearcher('indexes/')
searcher_4.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

searcher_5 = SimpleSearcher('indexes/')
searcher_5.set_bm25(QE_BM25_k1, QE_BM25_b)
searcher_5.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

searcher_6 = SimpleSearcher('indexes_without_stemming/')
analyzer_6 = analysis.get_lucene_analyzer(stemming=False)
searcher_6.set_analyzer(analyzer_6)
searcher_6.set_bm25(without_stem_QE_BM25_k1, without_stem_QE_BM25_b)
searcher_6.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

# Customized parameters for QE_BM25 using indexes from doubling title and adding keyword
BM25_k1_new = 0.5
BM25_b_new = 0.37

searcher_7 = SimpleSearcher('indexes_without_stemming_new/')
analyzer_7 = analysis.get_lucene_analyzer(stemming=False)
searcher_7.set_analyzer(analyzer_7)
searcher_7.set_bm25(BM25_k1_new, BM25_b_new)

# Customized parameters for QE_BM25 using indexes from doubling title and adding keyword
QE_BM25_k1_new = 0.53
QE_BM25_b_new = 0.45
searcher_8 = SimpleSearcher('indexes_without_stemming_new/')
analyzer_8 = analysis.get_lucene_analyzer(stemming=False)
searcher_8.set_analyzer(analyzer_8)
searcher_8.set_bm25(QE_BM25_k1_new, QE_BM25_b_new)
searcher_8.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, False)

annotation = './evaluate/Annotations.csv'

print("Default:")
evaluation(searcher, annotation)
print("-------------------------------------------------------------")
print("BM25 with customized parameters:")
print(f'k1:{BM25_k1}, b:{BM25_b}')
evaluation(searcher_1, annotation)
# print("-------------------------------------------------------------")
# print("With NER:")
# evaluation(searcher_ner, annotation)

print("-------------------------------------------------------------")
print("BM25 with krovetz stemmer:")
evaluation(searcher_2, annotation)

print("-------------------------------------------------------------")
print("BM25 with no stemmer:")
evaluation(searcher_3, annotation)


print("-------------------------------------------------------------")
print("Enable RM3 query expansion with default BM25 parameter:")
evaluation(searcher_4, annotation)

print("-------------------------------------------------------------")
print("Enable RM3 query expansion with customized BM25 parameter:")
print(f'k1:{QE_BM25_k1}, b:{QE_BM25_b}')
evaluation(searcher_5, annotation)

print("-------------------------------------------------------------")
print("Without stemming, but with RM3 query expansion and customized BM25 parameters:")
print(f'k1:{without_stem_QE_BM25_k1}, b:{without_stem_QE_BM25_b}')
evaluation(searcher_6, annotation)

print("-------------------------------------------------------------")
print("Without stemming and RM3 query expansion, but with customized BM25 parameter, and weighted scoring scheme:")
print(f'k1:{BM25_k1_new}, b:{BM25_b_new}')
evaluation(searcher_7, annotation)


print("-------------------------------------------------------------")
print("Without stemming, but with RM3 query expansion, customized BM25 parameter, and weighted scoring scheme:")
print(f'k1:{QE_BM25_k1_new}, b:{QE_BM25_b_new}')
evaluation(searcher_8, annotation)
