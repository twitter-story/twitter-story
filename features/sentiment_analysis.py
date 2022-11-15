import re
import matplotlib.pyplot as plt
from textblob import TextBlob
from user_tweets import user_tweets

def cleanTxt(text):
    text=re.sub(r'@[A-Za-z0-9]+', '', text)
    text=re.sub(r'#','', text)
    text=re.sub(r'RT[\s]+','', text)
    text=re.sub(r'https?:\/\/\S+','', text)
    return text

def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_analysis(score):
    if score <0:
        return 'Negative'
    elif score ==0:
        return 'Neutral'
    else:
        return 'Positive'

def sentiment_analysis(df):
    df['Tweets']=df['Tweets'].apply(cleanTxt)
    df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
    df['Polarity'] = df['Tweets'].apply(get_polarity)
    df['Analysis']=df['Polarity'].apply(get_analysis)
    df.to_csv('tweets.csv')
    return df

def percentage(df):
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    df.Analysis.value_counts().plot(kind='bar')
    plt.savefig('Sentiment_Analysis.png', bbox_inches='tight')


if __name__=='__main__':
    # df=user_tweets('elonmusk')
    # df=user_tweets('hellokitty')
    df=user_tweets('BBCBreaking')
    tweets=sentiment_analysis(df)
    print(tweets)
    percentage(tweets)
