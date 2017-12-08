import os
import json
import re
import pandas as pd
from functools import reduce
from bs4 import BeautifulSoup
from datetime import datetime
from profanity import profanity
import emoji

DATA_FOLDER = os.path.join(os.path.abspath(os.path.join(__file__, '../../../..')))
YEARS = ['2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009']
COLS = ['id', 'created_at', 'favorite_count','lang', 'place.country', 'place.name', 'geo.coordinates',
        'coordinates.coordinates', 'retweet_count', 'user.id', 'user.followers_count', 'user.location',
        'source', 'text'
         ]


def load_tweets():
    """
    Loads the data for all `YEARS`, filter and creates new usefull columns
    :return: dataframe with `COLS` plus transformed columns
    """
    data_paths = map(lambda x: os.path.join(DATA_FOLDER, 'data', 'master_{d}.json'.format(d=x)), YEARS)

    data = []
    for path in data_paths:
        with open(path) as f:
            for line in f:
                data.append(json.loads(line))

    data = reduce(lambda x, y: x + y, data)

    df = pd.io.json.json_normalize(data)[COLS]
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Filter just Trump, there is around 300 tweets that is not from him
    df = df[df['user.id'] == 25073877]

    # Filter missing text - around 1200 all from 2017
    df = df[pd.notnull(df['text'])]
    df[df['created_at'] >= datetime(2017, 4, 30)]

    df['weekday'] = df['created_at'].dt.weekday_name
    df['weekday_number'] = df['created_at'].dt.weekday
    df['month_cohort'] = df['created_at'].dt.strftime('%Y-%m')
    df['first_day_month_cohort'] = pd.to_datetime(df['month_cohort'])
    df['quarter_cohort'] = pd.PeriodIndex(df['created_at'], freq='Q')
    df['is_weekend'] = df['weekday'].apply(lambda x: x in ['Saturday', 'Sunday'])

    df['source'] = (df['source'].apply(lambda x: BeautifulSoup(x, 'html.parser').find_all('a')[0].text))

    df['count_url'] = df['text'].str.count('http')
    df['count_!'] = df['text'].str.count('!')
    df['count_?'] = df['text'].str.count('\?')
    df['count_#'] = df['text'].str.count('#')
    df['count_words'] = df['text'].str.split().str.len()

    df['has_url'] = df['count_url'] > 0
    df['has_!'] = df['count_!'] > 0
    df['has_?'] = df['count_?'] > 0
    df['has_#'] = df['count_#'] > 0

    # emojis
    emojis_list = map(lambda x:
                  ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
    regex_emojis = re.compile('|'.join(re.escape(p)
                                   for p in emojis_list))
    df['count_emojis'] = df['text'].str.count(regex_emojis)

    # bad words
    regex_bad = re.compile('|'.join(re.escape(p)
                                    for p in profanity.get_words()))

    df['count_profanity'] = df['text'].str.count(regex_bad)

    df['has_emojis'] = df['count_emojis'] > 0

    return df