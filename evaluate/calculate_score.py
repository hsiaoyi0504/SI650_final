from pyserini.search import SimpleSearcher
from sklearn.metrics import ndcg_score, dcg_score
import pandas as pd
import numpy as np
import math



def evaluation(searcher, annotation='./Annotations.csv'):
    df = pd.read_csv(annotation)
    queries = pd.unique(df['Query'].dropna())



    log = []
    for i in range(1,11):
        log.append(1/(math.log(i+1)/math.log(2)))
    log = np.array(log)

    total_ndcg = 0
    for query in queries:
        hits = searcher.search(query)
        true_label = np.append(df.loc[df['Query'] == query]['Score'].dropna().to_numpy(), [0]*10)
        true_label = np.sort(true_label)[-1:-11:-1]
        idcg = np.dot(true_label, log)

        output_label = [0]*10
        for i in range(min(10, len(hits))):
            # print(hits[i].docid)
            score = df.loc[df['Query'] == query].loc[df['Entry'] == hits[i].docid]
            if not score.empty:
                output_label[i] = score.iloc[0]['Score']
        output_label = np.array(output_label)

        dcg = np.dot(output_label, log)
        ndcg = dcg/idcg
        total_ndcg += ndcg
        # print(f'Query: {query}')
        # print(f'DCG: {dcg}')
        # print(f'iDCG: {idcg}')
        # print(f'NDCG: {ndcg}')
        # print(true_label)
        # print(output_label)
    print(f'Average NDCG: {total_ndcg/len(queries)}')

if __name__ == '__main__':
    searcher1 = SimpleSearcher('../indexes/')
    evaluation(searcher1)

