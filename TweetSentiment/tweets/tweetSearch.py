
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
from nltk.corpus import stopwords
import sys
import re
from nltk import NaiveBayesClassifier


consumerKey = "aOeKsPYiHaNogKz839cOjNcrw"
consumerSecret = "7iVB2Wrmx5HgaDpKvEpQuOvSHSEbQvLPDRYlFBLWwLU3iQN8uh"
accessToken = "456738617-OdAQgKaDCsMpv3V2Ky20lhiphIqjGDQjbrpEAJ6v"
accessTokenSecret = "LalwuqFdMEi1CgC6t4GfQvn0J50ittqllZ2Uha6W3mPX4"
auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


def getTweets(n, contains):
    """returns n tweets that contain the contains parameter, but with that string removed from the tweet for classification purposes"""
    tweets = []
    i = 0
    for tweet in tweepy.Cursor(api.search,
                           q=contains + "-filter:retweets",
                           rpp=100,
                           result_type="mixed",
                           include_entities=True,
                           lang="en").items():
        #Replace the searched term so it is not used in sentiment classification
        tweetToAdd = cleanTweet(tweet.text)
        tweets.append(tweetToAdd)
        i += 1
        if i >= n:
            break
    return tweets

def cleanTweet(tweetText):
    """Remove links and no traditional characters from a tweet"""
    #Remove links
    cleaned = re.sub(r"(?:\@|https?\://)\S+", "", tweetText)
    #Remove non-alphanumeric characters
    pattern = re.compile('\W ')
    cleaned = re.sub(pattern,"", cleaned)
    #Remove non-ascii characters
    cleaned = re.sub(r'[^\x00-\x7F]+',' ', cleaned)
    return cleaned


