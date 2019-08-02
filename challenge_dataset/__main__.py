import challenge_dataset


def main():
    news_data = challenge_dataset.NewsDataSet(shortten_corpus=True)
    print(news_data.data.head())


if __name__ == "__main__":
    '''
    I used this __main__ file for this module's testing
    '''
    main()
