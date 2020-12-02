import tweepy

import json
import argparse
from TwitterAPI import TwitterAPI


import config
import utils

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)

auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
API = 'statuses/user_timeline'

tweet_data = []  # 取得したツイートを格納するリスト



for tweet in api.search(q =' since:2020-11-29 until:2020-11-30 exclude:retweets', tweet_mode='extended', count=200):
    try:
        tweet_data.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n', ''),
                           tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count,
                           tweet.user.friends_count])
    except Exception as e:
        print(e)

#since:2020-11-15_08:00:00_JST until:2020-11-25_07:36:51_JST exclude:retweets', tweet_mode='extended', count=200):

import csv  # csvライブラリの読み込み

with open('テスト1203.csv', 'a', newline='', encoding='utf_8_sig') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id", "user", "created_at", "text", "fav", "RT", "follower", "follows"])
    writer.writerows(tweet_data)
pass