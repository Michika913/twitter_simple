# -*- coding: utf-8 -*-
import got3 as got

import urllib
import urllib.request
import urllib.error

tweet_data = []  # 取得したツイートを格納するリスト

def print_tweets(tweets):
    for tweet in tweets:
        tweet_data.append([tweet.id, tweet.username, tweet.date, tweet.text, tweet.favorites, tweet.retweets])
        print("取得件数：", len(tweets))

        print("---------------------------------")
        print("ツイートID：", tweet.id)
        print("ツイートURL：", tweet.permalink)
        print("アカウントの文字列：", tweet.username)
        print(tweet.text)
        print("投稿日：", tweet.date)
        print("リツイート数：", tweet.retweets)
        print("いいねの数：", tweet.favorites)
        if tweet.mentions:
            print("メンションの内容：", tweet.mentions)
        if tweet.hashtags:
            print("ハッシュタグの内容", tweet.hashtags)

# キーワードで取得
tweetCriteria = got.manager.TweetCriteria().setQuerySearch("デマ AND 否定").setMaxTweets(1000).setSince("2020-11-09").setUntil("2020-11-10")
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
print("---------------------------------")
print("②キーワードで取得")
print_tweets(tweets)

import csv  # csvライブラリの読み込み

with open('デマ否定.csv', 'w', newline='', encoding='utf_8_sig') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["tweet.id", "tweet.username", "tweet.date", "tweet.text", "tweet.favorites", "tweet.retweets"])
    writer.writerows(tweet_data)
pass