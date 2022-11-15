import pandas as pd 
from autho import autho


# #################### user_tweets from Twitter API  #################### #

def user_tweets(user):
    '''
    A function that takes the username of the Twitter user   
    and return the user's Tweets as a dataframe... 
    '''
    api=autho()
    post=api.user_timeline(screen_name=user,count=100,lang='en',tweet_mode='extended')
    df=pd.DataFrame([tweet.full_text for tweet in post],columns=['Tweets'])

    return df


if __name__ == '__main__':
    df=user_tweets('BBCBreaking')
    print(df)
    
