import tweepy

consumer_token = "AbvWXhLW9dLt7pOcqGyWAqkcN"
consumer_secret = "pxsXjJqQdlOH7HUmwdPy9q3EJiYDImKikDnmRD2bU655zGPe44"

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

with open("../pic/config", "r") as f:
    if not f.read() == "":
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
            api.update_status(line[1:])
            f.write()