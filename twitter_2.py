import json
import argparse

from TwitterAPI import TwitterAPI
import config
import utils
import csv  # csvライブラリの読み込み


API = 'tweets/search/fullarchive/:{}'.format(config.DEV_ENV_LABEL)
api = TwitterAPI(config.API_KEY, config.API_SECRET_KEY, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)


def parse_arg():
    args = argparse.ArgumentParser(description="search tweets by query.")
    args.add_argument("-f", "--filename", type=str, help="specify output JSON filename.")
    args.add_argument("-q", "--query", type=str, help="specify query keyword.")
    return args.parse_args()


def search_tweets(query):
    tweets = []
    params = {
        'query': query
    }

    res = api.request(API, params=params)
    if res.status_code != 200:  # 正常終了出来なかった場合
        print("Error with code: %d" % res.status_code)
    else:
        for tweet in res:
            tweets.append(tweet)

    return tweets
text = []
def show_tweets(tweets):
    for t in tweets:
        #print("------------------------------------")
        #print("tweet id: {}".format(t['id']))
        #print("screen_name: {}".format(t['user']['screen_name']))
        #print("user id: {}".format(t['user']['id']))
        print(t['text'].replace('\n', ''))
        text.append(t['text'].replace('\n', ''))
    str_ = '\n'.join(text)
    with open("デマツイート1.csv", "a", encoding="utf_8_sig", newline="") as files:
        writer = csv.writer(files, lineterminator='\n')
        files.write(str_)
        #writer.writerows(text)


if __name__ == '__main__':
    args = parse_arg()
    if args.query:
        tweets = search_tweets(args.query)
        if args.filename:
            with open(args.filename, "w+") as f:
                json.dump(tweets, f, indent=2, ensure_ascii=False)
        else:
            show_tweets(tweets)




