import csv
text = []
def show_tweets(tweets):
    for t in tweets:
        #print("------------------------------------")
        #print("tweet id: {}".format(t['id']))
        #print("screen_name: {}".format(t['user']['screen_name']))
        #print("user id: {}".format(t['user']['id']))
        #print("retweeted count: {}".format(t['retweet_count']))
        #print("quoted count: {}".format(t['quote_count']))
        #print("reply count: {}".format(t['reply_count']))
        if not "retweeted_status" in t:
            text.append(t['text'].replace('\n', ''))
            with open("デマツイート1.csv", "a", encoding="utf_8_sig", newline="") as files:
                print(t['created_at'], ",", t['text'].replace('\n', ''), file = files)
print(text)


