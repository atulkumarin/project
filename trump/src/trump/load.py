import os
import json
import pandas as pd
from functools import reduce
from bs4 import BeautifulSoup

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

    # Filter just Trump, there is around 300 tweets that is not from him
    df = df[df['user.id'] == 25073877]

    df['created_at'] = pd.to_datetime(df['created_at'])
    df['weekday'] = df['created_at'].dt.weekday_name
    df['month_cohort'] = df['created_at'].dt.strftime('%Y-%m')
    df['quarter_cohort'] = pd.PeriodIndex(df['created_at'], freq='Q')
    df['is_weekend'] = df['weekday'].apply(lambda x: x in ['Saturday', 'Sunday'])

    df['source'] = (df['source'].apply(lambda x: BeautifulSoup(x, 'html.parser').find_all('a')[0].text))

    return df
