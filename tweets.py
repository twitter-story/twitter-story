import snscrape.modules.twitter as sntwitter
import pandas as pd




# query = "(from:elonmusk) until:2020-01-01 since:2010-01-01" ******* 
# query = "elonmusk"
query= input()
tweets = []
limit = 10 # numbers of tweets


for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)