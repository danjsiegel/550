from gensim.models import LdaModel
import gensim
from gensim import corpora, models
import nltk
import numpy as np
import re
import pandas as pd

def task4(corpus):
    corpus['Tokenized'] = np.nan
    for row in range(len(corpus)):
        corpus['Tokenized'].iloc[row] = nltk.word_tokenize(corpus['cleaned'].iloc[row])
    dictionary = corpora.Dictionary(corpus.Tokenized)
    corpa = [dictionary.doc2bow(text) for text in corpus.Tokenized]
    ldamodel = gensim.models.ldamodel.LdaModel(corpa, num_topics=10, id2word = dictionary, passes=20)
    topics = ldamodel.print_topics(num_topics=10, num_words=1)
    with open('C:\\Users\\Dan Siegel\\Desktop\\Classes\\550\\final\\reports\\report2.md', 'a+') as mdWriter:
        for i in range(len(corpus)):
            line_extract = corpus['Tokenized'].iloc[i]
            new_review_bow = dictionary.doc2bow(line_extract)
            new_review_lda = ldamodel[new_review_bow]
            topic_no = new_review_lda[0][0]
            topic = re.findall('[A-z]\w+', topics[topic_no][1])[0]
            mdWriter.writelines(('Comment:', str(i+1),' Topic:', str(topic),'\n'))