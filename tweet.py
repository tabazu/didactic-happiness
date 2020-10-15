import tweepy
import config

auth= tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.key,config.secret)
api = tweepy.API(auth)

def post(message):
    api.update_status(message)
