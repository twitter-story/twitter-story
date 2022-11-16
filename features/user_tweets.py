import pandas as pd 
from autho import autho
from dotenv import load_dotenv
import csv
from csv import DictWriter


# #################### user_tweets from Twitter API  #################### #

def user_tweets(user):
    '''
    A function that takes the username of the Twitter user   
    and return the user's Tweets as a dataframe... 
    '''
    api=autho()
    post=api.user_timeline(screen_name=user,count=100,lang='en',tweet_mode='extended')
    df=pd.DataFrame([tweet.full_text for tweet in post],columns=['Tweets'])

    
    # status = post[0]
    # data=json.dumps(status._json)
    
    # create new file called tweet.csv with eight attributes
    with open('tweet.csv', 'w', encoding='UTF8') as f_object:
        writer = csv.writer(f_object)
        writer.writerow(['Tweets','Name','data','location','favorite_count','verified','created_at','retweet_count'])

    for tweet in post:
        obj = {
            'Tweets': tweet.full_text,
            'Name' : tweet.user.name,
            'data': tweet.created_at,
            'location':tweet.user.location,
            'favorite_count':tweet.favorite_count,
            'verified':tweet.user.verified,
            'created_at':tweet.user.created_at,
            'retweet_count':tweet.retweet_count
        }
        # fill all data about user in tweet.csv file 
        with open('tweet.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=['Tweets','Name','data','location','favorite_count','verified','created_at','retweet_count'])
            dictwriter_object.writerow(obj)
            f_object.close()
    
    # preparation steps to clean the data
    data=pd.read_csv('./tweet.csv',encoding='cp1252')
    data.drop_duplicates(inplace=True)
    data.dropna()
    data.set_index('Tweets', inplace=True)

    data.to_csv('tweet.csv')


    return df


if __name__ == '__main__':
    df=user_tweets('BBCBreaking')
    print(df)
    
