import tweepy

ACCESS_TOKEN = "" #Put your access token in here
ACCESS_SECRET = "" #Put your access token secret in here
CONSUMER_KEY = "" #put your API key in here
CONSUMER_SECRET = "" #put your API key secret in here


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api
api = connect_to_twitter_OAuth()

words=[]
user = input("Select a user to get tweets: ");print("")
get_tweets = api.user_timeline(user, count=10, include_rts = False)

for tweet in get_tweets:
    words.append(tweet.text)

word_split=[]
for tweet in words:
    splited = tweet.split()
    word_split += splited

def sorting(list):
    list.sort(key=len)
    return list

sorting(word_split)

remover = '!@#$%^&*()_+=-{}[];:,.<>/?'


final = []
for element in word_split:
    temp = ""
    for ch in element:
        if ch not in remover:
            temp += ch
    final.append(temp)


print ("The 5 smallest:")
for i in range(5):
    print(final[i])

print("")

print ("The 5 largest:")
for j in reversed(range(len(final)-5,len(final))):
    print(final[j])
