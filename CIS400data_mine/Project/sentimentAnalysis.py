#Sentiment Analysis
#4.21.2020

#packages
import twitter
from textblob import TextBlob
import datetime

def oauth_login(): #accesses the twitter API
    CONSUMER_KEY = 'BcykI907niRSvaVG9nFq50ZQd'
    CONSUMER_SECRET = 'ivAGXIU0uP4Efei2PghIEE64luTxRBhW4AbXaxzHwqSDLfqKqW'
    OAUTH_TOKEN = '1222957955592740864-SnZ3Pp4W8XwJ14JW9LGNDEpELrgxez'
    OAUTH_TOKEN_SECRET = '2Tobx8BKFfVbojg3z2OeXgmaGyRu60BENfivooHwo60GK'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Enter a company
def selectCompany():
    # starting time
    firstDT = datetime.datetime.now()
    print("Start time:", str(firstDT))

    company = input("Enter a company($AAL, $TSLA, $NFLX, or $ZM): ")

    while not (company == "$AAL" or company == "$TSLA" or company == "$NFLX" or company == "$ZM"): #asks user for company stock input
        company = input("Enter a company($AAL, $TSLA, $NFLX, or $ZM): ")
        return company
    return company

def polarity(stream):
    totalPolarity = 0
    tweetsCounted = 0

    for tweet in stream:
        tweetsCounted += 1
        text = tweet['text']
        print(text)
        blobText = TextBlob(text)
        polarity, subjectivity = blobText.sentiment
        totalPolarity += polarity
        if (tweetsCounted > 50):
            break

    print("The total polarity of ", company, " is: ", totalPolarity)
    if (totalPolarity > 0):
        print("Looks like the stock might go up today")
        print("Number of tweets: ", tweetsCounted)

    if (totalPolarity < 0):
        print("Looks like the stock might go down today")
        print("Number of tweets: ", tweetsCounted)

    if (totalPolarity == 0):
        print("Looks like the stock will stay the same today")
        print("Number of tweets: ", tweetsCounted)

    lastDT = datetime.datetime.now()
    print("End time:", str(lastDT))
    print("Total Time:", str(lastDT - firstDT))


#trending words when stocks go negative/positive

#correlation

#main
if __name__ == '__main__':
    twitter_api = oauth_login()
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

    company = selectCompany()

    stream = twitter_stream.statuses.filter(track=company)
    polarity(stream)