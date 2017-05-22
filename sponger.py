from twitter import *
import random,time

highest_id = 0

token = "X"
token_secret = "Y"
consumer_key = "Z"
consumer_secret = "J"

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

def sponge(stringo):
        dringo = ""
        for x in range(0,len(stringo)):
                char = stringo[x]
                if random.randint(0,1) == 0:
                        dringo = dringo + dringo.join(char.upper())
                else:
                        dringo = dringo + dringo.join(char.lower())
        return dringo

def removeName(stringo):
        stringo = stringo.replace("@spongebob_it","")
        return stringo

def lessThan140(text,id):
        front = id + text
        if len(front)+1 < 122:
                return text
        else:
                x = len(id)
                y = len(text)
                z = 121 - x
                text = text[:z]
        return text


def tweetIt(id, text):
        #Send a tweet
        text = text.replace("  ", "")
        text = lessThan140(text,id)
        with open("that-us.jpg", "rb") as imagefile:
                imagedata = imagefile.read()
        t_upload = Twitter(domain='upload.twitter.com',auth=OAuth(token, token_secret, consumer_key, consumer_secret))
        id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]

#       print("Total Length: ")
#       print(len('@'+id+text+id_img1))
#       print(len(id)+1)
#       print(len(text))
#       print(len(id_img1))
#       print(text)
        t.statuses.update(status="@"+id+" "+text, media_ids=id_img1)


## First run of script, set the since_id
startUp = t.statuses.mentions_timeline(count=1)
for tweet in startUp:
        text = removeName(tweet['text'])
        id = tweet['user']['screen_name']
        #tweetIt(id, sponge(text))
        if tweet['id'] > highest_id:
                highest_id = tweet['id']

while True:
        newTweets = t.statuses.mentions_timeline(count=5,since_id=highest_id)
        for tweets in newTweets:
                text = removeName(tweets['text'])
                id = tweets['user']['screen_name']
                tweetIt(id, sponge(text))
                if tweets['id'] > highest_id:
                        highest_id = tweets['id']
        time.sleep(20)
