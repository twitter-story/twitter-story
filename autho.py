import os 
import tweepy
from dotenv import load_dotenv


def autho():
    '''
    A function that takes authentication from Twitter API by passing 
    the API Key, Key Secret, Access Token, and Token Secretinto it...
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
