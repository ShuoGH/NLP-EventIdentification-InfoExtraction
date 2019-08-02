import pandas as pd
import os

CURRENT_PATH = os.getcwd() + "/data"


class NewsDataSet(object):
    '''
    Get the corpus.

    Attributes:
        - data_path: the path of the filefolder
        - shortten_corpus: indicate whether to use the shortten corpus.
            if `True`, use the shorrten data set (head 1000 news from the origin data set)

    '''

    def __init__(self, data_path=CURRENT_PATH, shortten_corpus=False):
        data_type = {'ArticleId': 'str', 'ArticleURL': 'str', 'ArticleTitle': 'str', 'ArticleDescription': 'str',
                     'ArticlePublishedTime': 'int'}
        self.data_path = data_path
        self.shortten_corpus = shortten_corpus
        self.dataset = pd.DataFrame()

        if self.shortten_corpus:
            self.dataset = pd.read_excel(
                self.data_path + "/data_news.xlsx", dtype=data_type)
        else:
            self.dataset = pd.read_excel(
                self.data_path + "/data_news_shortten.xlsx", dtype=data_type)

    def __len__(self):
        return len(self.data.shape[0])

    @property
    def data(self):
        return self.dataset
