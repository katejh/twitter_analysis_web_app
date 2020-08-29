import src.creds.set_credentials as set_credentials
import tweepy
import re
from textblob import TextBlob


# object for collecting tweets and analyzing them
# code from https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
class TwitterClient():

    # initializes tweepy API
    def __init__(self):
        # attempt authentication       
        try:
            self.api = tweepy.API(set_credentials.auth)
        except:
            print("Error: Failed to create TwitterClient because authentication failed")

    # Helper function that removes links and special characters
    def clean_tweet_text(self, text):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

    # returns list of Tweet objects and their sentiments
    # each item in the list is formatted as a dictionary with keys "tweet": Tweet object, "sentiment": Sentiment(polarity, subjectivity)
    def get_tweets(self, query, count = 10, lang = "en"):

        tweets = []

        cursor = tweepy.Cursor(self.api.search, q=query, count=count, lang=lang)
        for tweet in cursor.items(count):
            parsed_tweet = {}
            parsed_tweet["tweet"] = tweet
            parsed_tweet["sentiment"] = TextBlob(self.clean_tweet_text(tweet.text)).sentiment # a tuple object, Sentiment(polarity, subjectivity)

            if tweet.retweet_count > 0:
                # search in tweets list if retweeted tweet already exists
                retweet_exists = False
                for twt in tweets:
                    if twt["tweet"] == tweet.retweeted:
                        retweet_exists = True
                    if retweet_exists:
                        break
                
                if not retweet_exists:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)

        return tweets


def main():

    client = TwitterClient()
    tweets = client.get_tweets("covid,covid19,covid-19,corona,coronavirus", count = 50)


if __name__ == "__main__":
    main()
    