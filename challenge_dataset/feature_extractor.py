import numpy as np
import pandas as pd

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import gensim


class FeatureExtractor(object):
    '''
    Extractor to extract the features from corpus

    args:
        corpus: DataFrame only with index and one column

    '''
    def __init__(corpus):
        self.corpus = corpus
        self.tfidf_vocab = []
        self.tf_idf = np.array()

    def cal_tf_idf(self):
        corpus_tf_idf = [' '.join(content['TokenizedTitle'])
                         for index, content in corpus.iterrows()]

        vectorizer = CountVectorizer()
        transformer = TfidfTransformer()

        tfidf = transformer.fit_transform(
            vectorizer.fit_transform(corpus_tf_idf))
        vocabulary = vectorizer.get_feature_names()
        weight = tfidf.toarray()

        self.tfidf_vocab = vocabulary
        self.tf_idf = weight
        return weight

    def get_tf_idf(self):
        return self.tf_idf

    def train_word_vector(self, model='Word2Vec', pre_trained=False):
        '''
        Train the word_vector. The word2vec by default.
        args:
            model: ['Word2Vec','Glove']
        '''
        if model in ['Word2Vec', 'Glove']:
            pass
        else:
            raise ValueError(
                "The word vector model {} not in the list of supporting models.".format(model))
        return

    def get_word_vectors(self):
        return
