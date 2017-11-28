import re
import nltk
from nltk.corpus import stopwords
from profanity import profanity
import emoji

nltk.download('stopwords')


def preprocessing_text(series):
    """
    Clean elements of a series of string

    Parameters
    ----------
    series : series of strings

    Returns
    -------
    series with treated text

    """
    series = series.str.lower()

    series = series.str.replace('<user>', '')
    series = series.str.replace('<url>', '')

    series = series.str.replace('n\'t', 'not')
    series = series.str.replace('i\'m', 'i am')
    series = series.str.replace('\'re', ' are')
    series = series.str.replace('it\'s', 'it is')
    series = series.str.replace('that\'s', 'that is')
    series = series.str.replace('\'ll', ' will')
    series = series.str.replace('\'l', ' will')
    series = series.str.replace('\'ve', ' have')
    series = series.str.replace('\'d', ' would')
    series = series.str.replace('he\'s', 'he is')
    series = series.str.replace('she\'s', 'she is')
    series = series.str.replace('what\'s', 'what is')
    series = series.str.replace('who\'s', 'who is')
    series = series.str.replace('could\'ve', 'could have')
    series = series.str.replace('\'s', '')

    regex_letters = re.compile(r"[^\w\d\s]")
    series = series.str.replace(regex_letters, '')

    return series


def remove_stop_words(series):
    """
    Remove stop words from a series of string

    Parameters
    ----------
    series : series of strings

    Returns
    -------
    series without stop words

    """
    regex_stop = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    series = series.str.replace(regex_stop, '')
    series = series.str.replace('realdonaldtrump', '')
    series = series.str.replace('thank', '')
    series = series.str.replace('trump', '')
    series = series.str.replace('donald', '')
    series = series.str.replace('amp', '')

    return series


def features_eng(df):
    """
    Apply feature enginneing

    Parameters
    ----------
    dataframe : dataframe with columns of treated_text and clean_text

    Returns
    -------
    dataframe with feature enginnering (basic counts)

    """
    df['count_user'] = df['raw_tweet'].str.count('<user>')
    df['count_url'] = df['raw_tweet'].str.count('<url>')
    df['count_!'] = df['raw_tweet'].str.count('!')
    df['count_?'] = df['raw_tweet'].str.count('\?')
    df['count_#'] = df['raw_tweet'].str.count('#')
    #     df['count_tsk'] = df['raw_tweet'].str.count('tsk')
    df['count_<3'] = df['raw_tweet'].str.count('<3')
    df['count_lol'] = df['raw_tweet'].str.count('lol')
    df['count_words'] = df['clean_tweet'].str.split().str.len()

    # emojis
    emojis_list = map(lambda x:
                      ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
    regex_emojis = re.compile('|'.join(re.escape(p)
                                       for p in emojis_list))
    df['count_emojis'] = df['raw_tweet'].str.count(regex_emojis)

    # bad words
    regex_bad = re.compile('|'.join(re.escape(p)
                                    for p in profanity.get_words()))

    df['count_profanity'] = df['clean_tweet'].str.count(regex_bad)

    return df
