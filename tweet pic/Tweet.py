import tweepy, time, os

consumer_token = "AbvWXhLW9dLt7pOcqGyWAqkcN"
consumer_secret = "pxsXjJqQdlOH7HUmwdPy9q3EJiYDImKikDnmRD2bU655zGPe44"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
print "succesfully openend twiiter"

with open("../pic/config", "r") as f:
    if not f.read() == "":
        f.seek(0)
        if f.readline()[0] == "#":
            f.seek(0)
            key = f.readline()[1:]
            secret = f.readline()[1:]
            auth.set_access_token(key, secret)

    api = tweepy.API(auth)

while True:
    f = open("../pic/tweet", "r")
    lines = f.readline()
    f.close()

    f = open("../pic/tweet", "w")
    for line in lines:
        if line[0] == "$":
            print "tweeted file " + line[1:]
            api.update_with_media("../pic/" + line[1:], status="Someone walked throuth the door at " + time.strftime('%Y/%m/%d %H:%M:%S'))
            try:
                os.remove("../pic/" + line[1:])
            except OSError:
                print "file to tweet not found"
            f.write(line[1:])
    f.close()