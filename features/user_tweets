import os 
import pandas as pd 
import tweepy
from dotenv import load_dotenv

# #################### Twitter API authentication #################### #

def autho():
    load_dotenv()
    api_key=os.getenv("api_key")
    key_secret=os.getenv("key_secret")
    access_token=os.getenv("access_token")
    token_secret=os.getenv("token_secret")

    authenticate=tweepy.OAuthHandler(api_key,key_secret)
    authenticate.set_access_token(access_token,token_secret)

    api=tweepy.API(authenticate,wait_on_rate_limit=True)
    return api

# #################### user_tweets from Twitter API  #################### #

def user_tweets(user):
    api=autho()
    post=api.user_timeline(screen_name=user,count=100,lang='en',tweet_mode='extended')
    df=pd.DataFrame([tweet.full_text for tweet in post],columns=['Tweets'])

    return df


if __name__ == '__main__':
    df=user_tweets('BillGates')
    # df.to_csv('tweet.csv')
    print(df)
    
