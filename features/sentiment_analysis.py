import re
import matplotlib.pyplot as plt
from textblob import TextBlob
from userName_tweets import user_tweets

def cleanTxt(tweet):
    '''
    A function that takes the tweet as argument and
    remove any hashtag, metion, Retweet , and url link 
    and return tweet itself.
    '''
    tweet=re.sub(r'@[A-Za-z0-9]+', '', tweet)
    tweet=re.sub(r'#','', tweet)
    tweet=re.sub(r'RT[\s]+','', tweet)
    tweet=re.sub(r'https?:\/\/\S+','', tweet)
    return tweet

def get_subjectivity(tweet):
    '''
    A function that takes tweet and return its subjectivity
    by using TextBlob library as float.
    '''
    return TextBlob(tweet).sentiment.subjectivity

def get_polarity(tweet):
    '''
    A function that takes tweet and return its polarity
    by using TextBlob library as float.
    '''
    return TextBlob(tweet).sentiment.polarity

def get_analysis(score):
    '''
    A function that takes score and return 
    'Negative' if its less than zero
    'Neutral' if its equal zero
    and 'Psitive' otherwise.
    '''
    if score <0:
        return 'Negative'
    elif score ==0:
        return 'Neutral'
    else:
        return 'Positive'

def sentiment_analysis(df):
    '''
    A function that takes dataFrame as argument and 
    create  1. Subjectivity column 
            2. Polarity column
            3. Analysis column
    save dataframe into csv file
    and return df itself. 
    '''
    df['Tweets']=df['Tweets'].apply(cleanTxt)
    df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
    df['Polarity'] = df['Tweets'].apply(get_polarity)
    df['Analysis']=df['Polarity'].apply(get_analysis)
    df.to_csv('user_tweets.csv')
    return df

def percentage(df):
    '''
    A function that takes dataFrame as an argument and 
    and make visualizations for its Analysis column
    and save it as a figure.
    '''
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    df.Analysis.value_counts().plot(kind='bar')
    plt.savefig('Sentiment_Analysis.png', bbox_inches='tight')


if __name__=='__main__':
    df=user_tweets('Microsoft')
    # df=user_tweets('BillGates')
    # df=user_tweets('BBCBreaking')
    tweets=sentiment_analysis(df)
    print(tweets)
    percentage(tweets)
