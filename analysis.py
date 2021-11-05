import operator
from functools import reduce
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


df = pd.read_csv("./preprocess/data.csv")

print('Announce Date: ', df['AnnounceDate'].min(), '-', df['AnnounceDate'].max())

text = ' '.join(df['Title'].astype(str)) + ' '.join(df['Description'].astype(str))
wordcloud = WordCloud(width=800, height=600, background_color='white').generate(text)
wordcloud.to_file('wordcloud.png')

keywords = df['Keyword'].to_list()
keywords = [k.replace('curator keyword:', '') for k in keywords]
keywrods = [k.replace('submitter keyword:', '') for k in keywords]
keywrods = [k.replace('keyword:', '') for k in keywords]
keywrods = [k.replace('submitter:', '') for k in keywords]
keywords = [k.replace('omedicalsubmitter keyword:', '') for k in keywords]
keywords = [k.replace('ologicalsubmitter keyword:', '') for k in keywords]
keywords = [k.replace('chnicalsubmitter keyword:', '') for k in keywords]
keywords = [k.split(',') for k in keywords if ',' in k ]
keywords = reduce(operator.concat, keywords)
# debug code: print(Counter(keywords).most_common(50))

text2 = ' '.join(keywords)
wordcloud2 = WordCloud(width=800, height=600, background_color='white').generate(text2)
wordcloud2.to_file('wordcloud_keyword.png')