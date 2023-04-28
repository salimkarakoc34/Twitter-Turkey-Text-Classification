import tweepy
import json






access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bearer_token='XXXXXXXXXXXXXXXXXX%XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
api_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
api_key_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'





import tweepy
import json

# API KEYS  
consumer_key = f'{api_key}'
consumer_secret = f'{api_key_secret}'
access_token = f'{access_token}'
access_token_secret = f'{access_token_secret}'


# AUTH
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API nesnesi oluşturma
api = tweepy.API(auth)

#username =['XX','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
username =['X']

len(username)

for user in username:


    tweets = tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode="extended").items(2000)




    with open(f'{user}.txt', 'w', encoding='utf-8') as file:


        for tweet in tweets:
            if not hasattr(tweet, 'retweeted_status') and tweet.in_reply_to_status_id is None and tweet.in_reply_to_user_id is None and tweet.in_reply_to_screen_name is None:
                file.write(tweet.full_text.replace('\n', '') + '\n\n')







