from requests_oauthlib import OAuth1Session
import os
import json
import config


# ツイート取得用のURL
SEARCH_URL = 'https://api.twitter.com/1.1/search/tweets.json'


def search(params):
    twitter = OAuth1Session(config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    req = twitter.get(SEARCH_URL, params = params)
    tweets = json.loads(req.text)
    return tweets

# PHPにおけるparse_str関数の代わり
def parseToParam(parse_str, parse=None):
    if parse is None:
        parse = '&'
    return_params = {}
    parsed_str = parse_str.split(parse)
    for param_string in parsed_str:
        param, value = param_string.split('=', 1)
        return_params[param] = value
    return return_params

def main():
    search_word = '#Qiita'
    tweet_data = []

    # Tweet Search
    params = {
                'q'  : search_word,
            'count'  : 100,
             }
    tweet_count = 0

    while tweet_count < 1000:
        tweets = search(params)
        for tweet in tweets['statuses']:
            tweet_data.append(tweet)

        import csv  # csvライブラリの読み込み

        with open('predicted_data.csv', 'w', newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(["id", "user", "created_at", "text", "fav", "RT", "follower", "follows"])
            writer.writerows(tweet_data)
        pass
        # tweets['search_metadata']['next_results'] をパースしてparamへ
        if 'next_results' in tweets['search_metadata'].keys():
            next_results = tweets['search_metadata']['next_results']
            next_results = next_results.lstrip('?') # 先頭の?を削除
            params = parseToParam(next_results)
            tweet_count += len(tweets['statuses'])
        else:
            break


if __name__=='__main__':
    main()

