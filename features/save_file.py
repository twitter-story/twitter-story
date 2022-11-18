import pandas as pd 
import csv
from csv import DictWriter
    
def create_csv(post):
    '''this function create new file called tweet.csv with eight attributes'''

    with open('./data/tweet.csv', 'w', encoding='UTF8') as f_object:
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
        with open('./data/tweet.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=['Tweets','Name','data','location','favorite_count','verified','created_at','retweet_count'])
            dictwriter_object.writerow(obj)
            f_object.close()
    preparation()

def preparation():
    '''this function preparation steps to clean the data'''
    data=pd.read_csv('./data/tweet.csv',encoding='cp1252')
    data.drop_duplicates(inplace=True)
    data.dropna()
    data.set_index('Tweets', inplace=True)
    
    data.to_csv('./data/tweet.csv')