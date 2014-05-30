import tweepy

with open("pic/config", "w") as f:
    consumer_token = "AbvWXhLW9dLt7pOcqGyWAqkcN"
    consumer_secret = "pxsXjJqQdlOH7HUmwdPy9q3EJiYDImKikDnmRD2bU655zGPe44"

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'

    print redirect_url
    verifier = raw_input("Verifier: ")

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    key = auth.access_token.key
    secret = auth.access_token.secret
    f.write("#" + key + "\n")
    f.write("#" + secret + "\n")

    api = tweepy.API(auth)