from autho import autho

def write_tweet(text):
    '''
    A function that takes text as argument and tweet it on twitter
    then return the id of that tweet...
    '''
    api=autho()
    tweet=api.update_status(status=text)
    return tweet._json['id']

def delete_tweet(id):
    '''
    A function that takes an ID of tweet and delete it from twitter
    '''
    api=autho()
    api.destroy_status(id)



if __name__ == '__main__':
    # print(write_tweet("hello"))
    delete_tweet(1593579303404539906)
    
