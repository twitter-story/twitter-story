import os 
import tweepy
from dotenv import load_dotenv


def autho():
    '''
    A function that takes the username of the Twitter user   
    and return the user's Tweets as a dataframe... 
    '''
    load_dotenv()
    api_key=os.getenv("api_key")
    key_secret=os.getenv("key_secret")
    access_token=os.getenv("access_token")
    token_secret=os.getenv("token_secret")

    authenticate=tweepy.OAuthHandler(api_key,key_secret)
    authenticate.set_access_token(access_token,token_secret)

    api=tweepy.API(authenticate,wait_on_rate_limit=True)
    return api
