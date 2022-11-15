from transformers import AutoTokenizer,AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np


def sa(tweet):
    # tweet = "@AmaniMALZoubi Today is not my day 😒 https://www.youtube.com/watch?v=w36ZmkgkPww"
    # tweet = '@AmaniMALZoubi I will not give up 💪  https://www.youtube.com/watch?v=tswf_A-jkAM'
    # precprcess tweet
    tweet_words = []
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        
        elif word.startswith('http'):
            word = "http"

        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    # # load model and tokenizer
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"

    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']

    # sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    x=''
    for i in range(len(scores)):
        x+=f'''
        {labels[i]}: {np.round(float(scores[i]), 3)}
        '''
    return x
if __name__=="__main__":
    tweet=input('write a tweet : ')
    print(sa(tweet))