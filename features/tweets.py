import snscrape.modules.twitter as sntwitter
import pandas as pd



def tweet(query): 
# query = "(from:elonmusk) until:2020-01-01 since:2010-01-01" ******* 
# query = "elonmusk"
    # query= input()
    tweets = []
    limit = 5 # numbers of tweets


    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.username, tweet.content])
            
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    All_tweets='''
        '''
    tweet=df['Tweet']
    for i in range(len(tweet)):
        All_tweets+=f'''
            tweet {i+1} : {tweet[i]}
            ----------------------------
            '''
    return All_tweets
    # return df['Tweet']
    
if __name__=="__main__":
    query=input()
    tweet=tweet(query)
    x=tweet['Tweet'][0].replace('\n',' ')
    print(x)
