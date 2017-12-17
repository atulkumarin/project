import re
import nltk
import string
from functools import partial
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

nltk.download('averaged_perceptron_tagger')

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


def preprocess_contractions(series):
    """
    Clean abbreviations from english
    :param series: series with tweets text
    :return: series with replaced values
    """
    # series = series.str.lower()

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
    Remove stop words
    :param series: series with tweets text
    :return: string series wihtout stop words
    """
    regex_stop = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    series = series.str.replace(regex_stop, '')
    series = series.str.replace('realdonaldtrump', '')
    series = series.str.replace('thank', '')
    series = series.str.replace('trump', '')
    series = series.str.replace('donald', '')
    series = series.str.replace('amp', '')

    return series


def cleaner_text(to_lower, remove_punct, txt):
    """
    Remove customized stop words, transform to lower, remove digit and remove punctuation
    :param to_lower: boolean
    :param remove_punct: boolean
    :param txt: string with txt
    :return: filtered list of tokens
    """
    txt = word_tokenize(txt)

    TRUMP_STOPWORDS = ['realdonaldtrump', 'thank', 'trump', 'donald', 'amp', '&amp', '&amp;']
    stop_words = stopwords.words('english') + TRUMP_STOPWORDS

    punctuation = list(string.punctuation) + list('“’—.”’“--,”') + ['...', '``']

    if to_lower and remove_punct:
        return [t.lower() for t in txt if
                t.lower() not in stop_words and t.lower() not in punctuation and not t.isdigit()]

    elif to_lower:
        return [t.lower() for t in txt if t.lower() not in stop_words and not t.isdigit()]

    elif remove_punct:
        return [t for t in txt if t.lower() not in stop_words and t.lower() not in punctuation and not t.isdigit()]

    return [t for t in txt if t.lower() not in stop_words and not t.isdigit()]


def clean_series(series, to_lower=True, remove_punct=True):
    """
    :param series: series with tweets text
    :param to_lower: boolean
    :param remove_punct: boolean
    :return: 2 series, one with filtered tokens and other with filtered text
    """
    fn = partial(cleaner_text, to_lower, remove_punct)
    clean_tokens = series.apply(fn)
    clean_text = clean_tokens.apply(lambda x: ' '.join(x))

    return clean_tokens, clean_text


def count_tags(tokens_series):
    """
    Function classify token in (verb, adj, adv, noun)
    :param tokens_series: series of tokens
    :return: dataframe with token classified and proportion of each category
    """

    def lookup_type_word(type_word):
        if type_word.startswith('J'):
            return 'adj'
        elif type_word.startswith('V'):
            return 'verb'
        elif type_word.startswith('N'):
            return 'noun'
        elif type_word.startswith('R'):
            return 'adv'
        else:
            return None

    tags_series = tokens_series.apply(lambda tokens: list(map(lambda t:
                                                              lookup_type_word(t[1]),
                                                              pos_tag(tokens))))

    prop_verbs = (tags_series
                  .apply(lambda tag:
                         len([x for x in tag if x == 'verb']) / len(tag) if len(tag) > 0 else 0))

    prop_adj = (tags_series
                .apply(lambda tag: len([x for x in tag if x == 'adj']) / len(tag) if len(tag) > 0 else 0))

    prop_adv = (tags_series
                .apply(lambda tag: len([x for x in tag if x == 'adv']) / len(tag) if len(tag) > 0 else 0))

    prop_noun = (tags_series
                 .apply(lambda tag: len([x for x in tag if x == 'noun']) / len(tag) if len(tag) > 0 else 0))

    return pd.DataFrame({'tags': tags_series,
                         'prop_verbs': prop_verbs,
                         'prop_adj': prop_adj,
                         'prop_adv': prop_adv,
                         'prop_noun': prop_noun})


def get_hardcoded_subjects(df):
    df['hillary'] = (
        df['clean_text'].str.contains('hillary') | df['clean_text'].str.contains('hilary') | df[
            'clean_text'].str.contains(
            'clinton'))
    df['obama'] = df['clean_text'].str.contains('obama')
    df['make_america'] = (df['text'].str.lower().str.contains('great again') | df['text'].str.contains('GreatAgain'))
    df['war'] = df['clean_text'].str.contains('war')
    df['democra'] = df['clean_text'].str.contains('democra')

    return df
