# to use set_credentials in another file, import set_credentials
# with the tweepy modules, simply pass in set_credentials.auth anywhere an
#   authentication token is required
# e.g. api = tweepy.API(set_credentials.auth)

import tweepy
from tweepy import OAuthHandler
import json

# import API keys from credentials file
# this credentials file can be named anything but should be in json format
credentials_file = "src/creds/credentials.json"
with open(credentials_file) as creds:
    credentials = json.load(creds)

consumer_key = credentials["API-key"]
consumer_secret = credentials["API-secret-key"]
access_token = credentials["access-token"]
access_secret = credentials["access-token-secret"]

try:
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
except:
    print("Error: Authentication failed")