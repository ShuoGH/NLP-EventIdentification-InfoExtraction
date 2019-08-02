import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

import gensim
import datetime
# import glove

'''
This is the module which contains the utils to get the emdedding of words other than the tools within the BERT.

Here are mainly about the word2vec and glove.
'''

list_of_stop_words = set(stopwords.words('english'))
punctuations = list(string.punctuation)


def remove_stopwords(token_list):
    '''
    Remove the stops words from the tokenized sentence.

    `Stopwords` is from the NLTK stopwords.

    args:
        token_list: the token list of the sentence
    return:
        token_list without the stopwords
    '''
    words_without_stopwords = []
    for token in token_list:
        if token not in list_of_stop_words:
            words_without_stopwords.append(token)
    return words_without_stopwords


def remove_punctuation(token_list):
    '''
    Remove the punctuations from the tokenized sentence

    `punctuations` is from `string.punctuation`.
    args:
        token_list: the token list of the sentence
    return:
        token_list without the punctuations
    '''
    words_without_punctuations = []
    for token in token_list:
        if token not in punctuations:
            words_without_punctuations.append(token)
    return words_without_punctuations


def pre_process_sentence(sentence):
    '''
    combine three functions: word tokenization, `remoce_stopwords` and `remove_punctuation`
    args:
        sentence: the sentence to be pre-process
    return:
        tokens: list of tokens, which have been removed stopwords, punctuations
    '''
    out = word_tokenize(sentence)
    out = remove_punctuation(out)
    out = remove_stopwords(out)
    return out


def embedding_word2vec(word_list):
    '''
    Embedding the word into word vector by word2vec.
    `word2vec` is supplied by the gensim module here.

    args:
        word_list: the list of words
    return:
        word vectors
    '''
    return


def embedding_glove(word_list):
    '''
    Embedding the word into vector by glove
    args:
        word_list: the list of words
    return:
        word vectors
    '''
    return


def unixtime_converter(unixtimestamp):
    '''
    convert the unix timestamp into readable time format
    args:
        unixtimestamp: int of the time stamp
    return:
        rtime: readable time of the `datetime` type
    '''
    return datetime.utcfromtimestamp(x)
