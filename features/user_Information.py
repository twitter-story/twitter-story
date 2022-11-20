from autho import autho
import tweepy

def Get_user_Information(user):
    '''
    This function accept the name of the user and return the important information about him.
    '''
    api=autho()
    #user='elonmusk'
    
    user_Object=api.get_user(screen_name=user)
    user_Info={
        
        'Username': user_Object.name,
        'Location': user_Object.location,
        'Description':user_Object.description,
        'Followers_count': user_Object.followers_count,
        'Friends_count':user_Object.friends_count,
        'Created_at':str(user_Object.created_at),
        'Verified':user_Object.verified,

        'Profile_image':user_Object.profile_image_url_https,
        'Profile_banner':user_Object.profile_banner_url




    }
    return user_Info

#print(Get_user_Information('alm7seery'))

#username, screenName, location,followers,friend,created at ,deicreption ,verified 

