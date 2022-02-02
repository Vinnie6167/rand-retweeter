import tweepy
import json

with open("keys.json", "r") as keysFile:
    keys = json.load(keysFile)

auth = tweepy.OAuthHandler(keys["API_KEY"], keys["API_KEY_SECRET"])
auth.set_access_token(keys["ACCESS_TOKEN"], keys["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    tweet.retweet()