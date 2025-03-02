import tweepy
import json
import nltk
import csv
import time

from src.Data import Data
from deprecation import deprecated
from nltk.sentiment import SentimentIntensityAnalyzer


class Crawler():
    def __init__(self):
        nltk.download('vader_lexicon')
        data = Data()
        
        api_key = data.get_api()[0]
        api_secret = data.get_api()[1]
        access_token = data.get_access()[0]
        access_secret = data.get_access()[1]
        bearer_token_key = data.get_bearer()

        self.auth = tweepy.OAuth1UserHandler(
            api_key, api_secret, access_token, access_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        self.client = tweepy.Client(bearer_token=bearer_token_key)

    @deprecated(deprecated_in="0.1", removed_in="1.0", details="V1.1 is no longer required, user V2 instead!")
    def crawl_tweets_v1(self, keyword, count):
        """Mengambil tweet berdasarkan keyword"""
        tweets_data = []
        for tweet in tweepy.Cursor(self.api.search_tweets, q=keyword, lang="id", tweet_mode='extended').items(count):
            tweets_data.append({
                "id": tweet.id_str,
                "text": tweet.full_text,
                "user": tweet.user.screen_name,
                "created_at": str(tweet.created_at)
            })
        return tweets_data


    def crawl_tweets_v2(self, keyword, count):
        tweets = self.client.search_recent_tweets(query=keyword, max_results=count, tweet_fields=["created_at", "text", "author_id"])

        tweets_data = []
        if tweets.data:
            for tweet in tweets.data:
                tweets_data.append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "user": tweet.author_id,
                    "created_at": str(tweet.created_at)
                })
        return tweets_data


    def analyze_sentiment(self, tweets):
        """Melabeli sentimen positif, negatif, atau netral"""
        sia = SentimentIntensityAnalyzer()
        count_pos = 0
        count_neg = 0
        count_net = 0
        
        for tweet in tweets:
            score = sia.polarity_scores(tweet["text"])
            if score['compound'] >= 0.05:
                tweet["sentiment"] = "positif"
                count_pos += 1
            elif score['compound'] <= -0.05:
                tweet["sentiment"] = "negatif"
                count_neg += 1
            else:
                tweet["sentiment"] = "netral"
                count_net += 1
                
        print("Total of Positive Sentiment: ", count_pos)
        print("Total of Negative Sentiment: ", count_neg)
        print("Total of Neutral Sentiment: ", count_net)
        
        return tweets


    def save_json(self, data, filename):
        """Menyimpan data ke dalam file JSON"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    def save_csv(self, data, filename):
        """Menyimpan data ke dalam file CSV"""
        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
            
    
    def execute(self, keyword, count) : 
        raw_tweets = self.crawl_tweets_v2(keyword, count=count)
        labeled_tweets = self.analyze_sentiment(raw_tweets)
        self.save_json(labeled_tweets, f"tweets_{keyword}.json")
        self.save_csv(labeled_tweets, f"tweets_{keyword}.csv")
        print(f"Data berhasil disimpan ke tweets_{keyword}")
