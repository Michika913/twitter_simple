import pandas as pd
from requests_oauthlib import OAuth1Session
import json
import config
import tweepy

CK = config.API_KEY
CS = config.API_SECRET_KEY
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET


max_id = -1
url = "https://api.twitter.com/1.1/search/tweets.json"
keyword = '事務所'
count = 100
#検索ワード・期間指定、リツイートを除外
params = {'q' : keyword, 'since' : 2020-11-19, 'until' : 2020-11-20, 'exclude' : 'retweets', 'tweet_mode' : 'extended', 'count' : count, 'max_id' : max_id}


twitter = OAuth1Session(CK, CS, AT, ATS)
req = twitter.get(url, params = params)

tweet_data = []  # 取得したツイートを格納するリスト



from time import sleep

columns = ['ID', 'ユーザー名', '時間', 'ツイート', 'いいね数', 'リツイート数', 'フォロワー数', 'フォロー数']
df = pd.DataFrame(columns=columns)

while (True):
    if max_id != -1:
        params['max_id'] = max_id - 1
    req = twitter.get(url, params=params)

    if req.status_code == 200:
        search_timeline = json.loads(req.text)

        if search_timeline['statuses'] == []:
            break

        for tweet in search_timeline['statuses']:
            id_str = tweet['id']
            user_screen_name = tweet['user']['screen_name']
            created_at = tweet['created_at']
            text = tweet['text']
            favorite_count = tweet['favorite_count']
            retweet_count = tweet['retweet_count']
            follower_count = tweet['user']['followers_count']
            friend_count = tweet['user']['friends_count']

            print(id_str, user_screen_name, created_at, text, favorite_count, retweet_count,follower_count, friend_count)


            append_list = [id_str, user_screen_name, created_at, text, favorite_count, retweet_count,follower_count, friend_count]

            df_next = pd.DataFrame(
                [append_list],
                columns=columns
            )

            df = df.append(df_next)
        max_id = search_timeline['statuses'][-1]['id']



    else:
        print('1５分待ちます')
        sleep(15 * 60)

