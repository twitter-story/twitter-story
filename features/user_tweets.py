import pandas as pd 
from autho import autho
from dotenv import load_dotenv
import csv
from csv import DictWriter

from save_file import *


# #################### user_tweets from Twitter API  #################### #

def user_tweets(user):
    '''
    A function that takes the username of the Twitter user   
    and return the user's Tweets as a dataframe... 
    '''
    api=autho()
    post=api.user_timeline(screen_name=user,count=20,tweet_mode='extended')
    df=pd.DataFrame([tweet.full_text for tweet in post],columns=['Tweets'])

    create_csv(post)

    return df


if __name__ == '__main__':
    df=user_tweets('BillGates')
    # print(df)
    
