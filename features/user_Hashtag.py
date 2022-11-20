from dotenv import load_dotenv
import pandas as pd
from autho import autho

user="AJArabic"
keyword='#قطر'
def search_by_UserAndHashtag(user, hashtag):
        api=autho()
        

        #tweets=api.search_tweets(q=keyword,include_entities=True)
        tweets=api.user_timeline(screen_name=user,count=100,tweet_mode='extended')

        df=pd.DataFrame([tweet.full_text for tweet in tweets],columns=['Tweets'])
        All_tweets=''
        x=df["Tweets"]
        
        for i in range(5):
                All_tweets+=f'tweet {i+1} : {x[i]} \n\n '
        return All_tweets
        # print(f'Tweets for {user} with {hashtag} are:')
        # print(All_tweets)
#search_by_UserAndHashtag(user,keyword)