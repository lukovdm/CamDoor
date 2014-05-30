from twython import Twython

APP_KEY = "AbvWXhLW9dLt7pOcqGyWAqkcN"
APP_SECRET = "pxsXjJqQdlOH7HUmwdPy9q3EJiYDImKikDnmRD2bU655zGPe44"

with open("pic/config", "w") as f:
    twitter = Twython(APP_KEY, APP_SECRET)
    try:
        auth = twitter.get_authentication_tokens()
    except Twython.TwythonAuthError:
        print 'Error! Failed to get request token.'

    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

    print auth["auth_url"]
    verifier = raw_input("Verifier: ")

    twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    try:
        final_step = twitter.get_authorized_tokens(verifier)
    except Twython.TwythonAuthError:
        print 'Error! Failed to get access token.'

    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

    f.write("#" + OAUTH_TOKEN + "\n")
    f.write("#" + OAUTH_TOKEN_SECRET + "\n")