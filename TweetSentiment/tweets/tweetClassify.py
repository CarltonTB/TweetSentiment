
import pickle as pickle
from nltk.corpus import stopwords
import os
import re


def word_features(words):
    stopset = list(set(stopwords.words('english')))
    for i in  range(len(stopset)):
        stopset[i] = str(stopset[i])
    feats = []
    for word in words.split():
        for stopword in stopset:
            if word != stopword:
                feats.append((word, True))
    return dict(feats)

def classifyTweets(tweets, searchTerm):
    """Returns a list of sub lists are a pair of a tweet and its sentiment"""
    fobj = open(os.path.split(os.path.abspath(__file__))[0]+'/NBC.pickle', 'rb')
    nbc = pickle.load(fobj)
    fobj.close()
    sentiment = []
    for tweet in tweets:
        #Remove the search term from the tweet before classifying it's sentiment
        toClassify = tweet
        replacePattern = re.compile(searchTerm, re.IGNORECASE)
        toClassify = replacePattern.sub("",toClassify)
        sentiment.append([nbc.classify(word_features(toClassify)),tweet])
        # uprint(tweet)
    return sentiment

def classifySentiment(text):
    """Classify the sentiment of some text"""
    fobj = open(os.path.split(os.path.abspath(__file__))[0]+'/NBC.pickle', 'rb')
    nbc = pickle.load(fobj)
    fobj.close()
    return nbc.classify(word_features(text))

def computeSentimentStats(tweetSentimentPairs):
    totalNeg = 0.0
    totalPos = 0.0
    for pair in tweetSentimentPairs:
        if(pair[0] == "negative"):
            totalNeg += 1
        elif(pair[0] == "positive"):
            totalPos += 1
    total = totalNeg+ totalPos
    if(total > 0):
        return [round(100*(totalNeg/total),2),round(100*(totalPos/total),2)]
    else:
        return ["N/A","N/A"]


