import tweepy, time, os

consumer_token = "AbvWXhLW9dLt7pOcqGyWAqkcN"
consumer_secret = "pxsXjJqQdlOH7HUmwdPy9q3EJiYDImKikDnmRD2bU655zGPe44"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
print "succesfully openend twiiter"

with open("pic/config", "r") as f:
    if not f.read() == "":
        f.seek(0)
        if f.readline()[0] == "#":
            f.seek(0)
            key = f.readline()[1:]
            secret = f.readline()[1:]
            auth.set_access_token(key, secret)

    api = tweepy.API(auth)

while True:
    f = open("pic/tweet", "r")
    lines = f.readlines()
    f.close()

    f = open("../pic/tweet", "w")
    for line in lines:
        if line[0] == "$":
            print "tweeted file: " + line[1:]
            fn = os.path.abspath("../pic/" + line[1:-1])
            print fn
            try:
                api.update_with_media(fn, status="Someone walked throuth the door at " + line[1:])
                os.remove("../pic/" + line[1:])
            except OSError, tweepy.error.TweepError:
                print "file to tweet not found"
                f.write(line)
            else:
                f.write(line[1:])
    f.close()