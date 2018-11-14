import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk import PorterStemmer
stop_words = set(stopwords.words('english'))

def task2(corpus, destination, filename):
    '''
    Task2 takes a dataframe, applies text processing methods, and then applies stemming and returns a dataframe
    Args:
        Param1: dataframe
    Returns:
        cleaned dataframe
    '''
    corpus['cleaned'] =corpus['txt'].apply(text_processing)
    corpus.to_pickle((destination + filename))
    return corpus

def text_processing(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    nopunc = nopunc.lower()
    no_stopwords = [word for word in nopunc.split() if word not in stopwords.words('english')]
    stemmer = PorterStemmer()
    no_stopwords = [stemmer.stem(word) for word in no_stopwords]
    stemmed_no_stopwords = ' '.join(no_stopwords)
    return stemmed_no_stopwords