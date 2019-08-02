## main goal

Given the data set contains the information of news articles, try to identify the breaking news event and extract information for each event.

## Module Require

This project is built by the PyTorch. The required modules are list as below.

- torch
- pytorch-transformers
    - For the implementation of BERT. 
- spacy
- nltk

## How to run

The code are organized in the jupyter notebook.

Before run, make sure there are `data/` and `output/` two file folders are build in the current path.

Install modules and download pre-trained model.

```bash
pip install spacy
python -m spacy download en_core_web_sm
# python -m spacy link en_core_web_sm en_core_web_sm
```

(You may also encouter this in the notebook.)

I did the project on my own laptop and tested it on the server. To save time, the shorten data `data_news_shorten.xlsx` set could be used. It contains the first 1000 items from original data set.

## Files

- data/: the file folder containing the data set
  - `data_news_shorten.xlsx`: the truncated data set (1000 from the original data)
  - `data_news.xlsx`: the original data (has been renamed)
  - `news_corpus_for_doc2vec.csv`: the csv file for training doc2vec. 
- `challenge_dataset` : custom module for the data set. (though didn't use in the final version of my project) In the beginning I wanted to build some scripts for this challenge.
- `0. EDA of the News Dataset.ipynb`: EDA 
- `1. Identify the Breaking News Event.ipynb` : the notebook for solving the first task
- `2 Information Extraction.ipynb`: the notebook for solving the second task
- `3. Further Idea.ipynb`: for third task
- `Using BERT NextSentence Prediction for Task1.ipynb`: experience of exploring BERT. The supplement of the `3. Further Idea.ipynb`.


Finally,
Thanks to echobox for supplying me such a good opportunity to do the challenge!