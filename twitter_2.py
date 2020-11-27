import tweepy
from requests_oauthlib import OAuth1Session
import pandas as pd

import json
import argparse
from TwitterAPI import TwitterAPI


import config
import utils

SEARCH_URL = 'https://api.twitter.com/1.1/search/tweets.json'
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)

auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)


def search(params):
    twitter = OAuth1Session(config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    req = twitter.get(SEARCH_URL, params = params)
    tweets = json.loads(req.text)
    return tweets

def parseToParam(parse_str, parse=None):
    if parse is None:
        parse = '&'
    return_params = {}
    parsed_str = parse_str.split(parse)
    for param_string in parsed_str:
        param, value = param_string.split('=', 1)
        return_params[param] = value
    return return_params

tweet_data = []  # 取得したツイートを格納するリスト
api = tweepy.API(auth)

params = {
    'q': "事務所",
    'count': 1000,
}
tweet_count = 0

while tweet_count < 1000:
    tweets = search(params)
    for tweet in api.search(q ='事務所否定 since:2020-11-19_08:00:00_JST until:2020-11-20_07:27:19_JST exclude:retweets', tweet_mode='extended',count=1000):

        tweet_data.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n', ''),
                           tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count,
                           tweet.user.friends_count])

    # tweets['search_metadata']['next_results'] をパースしてparamへ
    if 'next_results' in tweets['search_metadata'].keys():
        next_results = tweets['search_metadata']['next_results']
        next_results = next_results.lstrip('?')  # 先頭の?を削除
        params = parseToParam(next_results)
        tweet_count += len(tweets['statuses'])
    else:
        break





import csv  # csvライブラリの読み込み

with open('事務所4.csv', 'w', newline='', encoding='utf_8_sig') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id", "user", "created_at", "text", "fav", "RT", "follower", "follows"])
    writer.writerows(tweet_data)
pass