import twitter
import json
import networkx
import matplotlib
import numpy
import sys
import time
from functools import partial
from sys import maxsize as maxint
from urllib.error import URLError
from http.client import BadStatusLine
import matplotlib.pyplot as plt
import pickle
import datetime
import config

file1 = open(b"resultsB.txt", "wb")

def oauth_login(): #accesses the twitter API
    # CONSUMER_KEY = 'BcykI907niRSvaVG9nFq50ZQd'
    # CONSUMER_SECRET = 'ivAGXIU0uP4Efei2PghIEE64luTxRBhW4AbXaxzHwqSDLfqKqW'
    # OAUTH_TOKEN = '1222957955592740864-SnZ3Pp4W8XwJ14JW9LGNDEpELrgxez'
    # OAUTH_TOKEN_SECRET = '2Tobx8BKFfVbojg3z2OeXgmaGyRu60BENfivooHwo60GK'
    CONSUMER_KEY = 'nDcNcPhe4xQq3cCHsVtzYtclg'
    CONSUMER_SECRET = 'AFGfDfgjYwvApF6LbcsEfDGskybayQXqgr9y402cdNqdQFs5FW'
    OAUTH_TOKEN = '1222957955592740864-DOmb2Tgi3U4tzkW40ypHXN5No9r9VN'
    OAUTH_TOKEN_SECRET = 'PeJYB3LnLD5cfZ87m9ri2D9LlBdfbTcN6uKMBLscu9EO8'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#1.select a starting pt: Twitter user
screen_name = "edmundyu1001"
#2.Retrieve his/her friends, which should be a list of id’s, and followers, which is another list of id’s(from twitter cookbook ch9)
def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
# A nested helper function that handles common HTTPErrors. Return an updated  value for wait_period if the problem is a 500 level error. Block until the
# rate limit is reset if it's a rate limiting issue (429 error). Returns None for 401 and 404 errors, which requires special handling by the caller.
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
        if wait_period > 3600:  # Seconds
            print('Too many retries. Quitting.', file=sys.stderr)
            raise e
        if e.e.code == 401:
            print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
            return None
        elif e.e.code == 404:
            print('Encountered 404 Error (Not Found)', file=sys.stderr)
            return None
        elif e.e.code == 429:
            print('Encountered 429 Error (Rate Limit Exceeded)', file=sys.stderr)
            if sleep_when_rate_limited:
                print("Retrying in 15 minutes...ZzZ...", file=sys.stderr)
                sys.stderr.flush()
                time.sleep(60 * 15 + 5)
                print('...ZzZ...Awake now and trying again.', file=sys.stderr)
                return 2
            else:
                raise e  # Caller must handle the rate limiting issue
        elif e.e.code in (500, 502, 503, 504):
            print('Encountered {0} Error. Retrying in {1} seconds'.format(e.e.code, wait_period), file=sys.stderr)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e
# End of nested helper function
    wait_period = 2
    error_count = 0
    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError as e:
            error_count = 0
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("URLError encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise
        except BadStatusLine as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("BadStatusLine encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise

def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None, friends_limit=5000, followers_limit=5000): #from the cookbook
    # Must have either screen_name or user_id (logical xor)
    assert (screen_name != None) != (user_id != None), "Must have screen_name or user_id, but not both"
    get_friends_ids = partial(make_twitter_request, twitter_api.friends.ids, count=5000)
    get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids, count=5000)
    friends_ids, followers_ids = [], []
    for twitter_api_func, limit, ids, label in [ [get_friends_ids, friends_limit, friends_ids, "friends"],
                                                 [get_followers_ids, followers_limit, followers_ids, "followers"] ]:
        if limit == 0: continue
        cursor = -1
        while cursor != 0:
            # Use make_twitter_request via the partially bound callable...
            if screen_name:
                response = twitter_api_func(screen_name=screen_name, cursor=cursor)
            else:  # user_id
                response = twitter_api_func(user_id=user_id, cursor=cursor)

            if response is not None:
                ids += response['ids']
                cursor = response['next_cursor']
            print('Fetched {0} total {1} ids for {2}'.format(len(ids), label, (user_id or screen_name)),
                  file=sys.stderr)

            if len(ids) >= limit or response is None:
                break
    return friends_ids[:friends_limit], followers_ids[:followers_limit]

def nameIds(screenName): #parameter is the twitter user #Gets the user_id and screen name using twitter's API
    try:
        user = make_twitter_request(twitter_api.users.lookup, user_id=int(screenName)) #sets user id as the screen name
    except:
        name = screenName.replace(" ", "")
        user = make_twitter_request(twitter_api.users.lookup,screen_name=name)
    user = user[0] #takes the first item of the pair which is the user id
    name_id = (user["id"], user["name"])
    return name_id #return the user_ID and the name of the account in a pair

#find the index of the top 5 friends by finding the maximum followers for each friend in the list
def crawler(list): #helper function to get the five most popular
    indexes = []
    #the actual function that will find the maximum number of followers for each person
    def maxIndex(numOfFollowers, account, num):
        if (num > 0) and (len(numOfFollowers)!=0):
            try:
                maximum = numOfFollowers[0]
                max_index = 0
                for i in range(len(numOfFollowers)):
                    if (numOfFollowers[i] > maximum):
                        maximum = numOfFollowers[i]
                        max_index = i
                account.append(max_index)
                numOfFollowers[max_index] = 0
                maxIndex(numOfFollowers, account, num - 1)
            except:
                #If a user doesn't have any friends this will be returned
                print("ERROR: No Followers found for", account)
    maxIndex(list, indexes, 5)
    printF(indexes)
    return indexes

def five_popular(twitter_api, user_id):
    top_friends = []
    tuplesList = []
    followers_nums = []
    try:
        friends, followers = get_friends_followers_ids(twitter_api, user_id = user_id, friends_limit = maxint, followers_limit = maxint) #Get the following and followers of the parent node
        friendsList = set(friends)
        followersList = set(followers)
        printF("Following:", followersList, "\nFollowers:", friendsList)

        mutual = friendsList.intersection(followersList) #takes the intersection of the two sets and converts it back to a list
        mutual = list(mutual)
        mutual = ','.join([str(item) for item in mutual[:100]]) #adds the mutuals together via join method with commas separating them
        all_mutuals = make_twitter_request(twitter_api.users.lookup, user_id = mutual)
        printF("Mutual followers: ", all_mutuals)

        for user in all_mutuals:
            num_followers = user["followers_count"]
            protected_users = user["protected"]
            id = user["id"]
            name = user["screen_name"]
            all_together = (id, name, num_followers, protected_users)
            tuplesList.append((all_together)) #get top five indexes and add the top 5 friends to top_friends

        publicUsers = [i for i in tuplesList if i[3] == False] #list comprehension to ignore private accounts, only takes public users
        print(publicUsers)
        for i in publicUsers:
            followers_nums.append(i[2]) #append the num_followers of each person into one single list with the updated Private accounts deleted

        five_index = crawler(followers_nums) #assigns the top 5 indexes to five_index
        try:
            for i in five_index:
                top_friends.append((publicUsers[i][0], publicUsers[i][1]))
        except:
            printF("Unexpected error:", sys.exc_info())
            printF("These are the top 5 friends:", top_friends)
            return top_friends
    except:
       printF("Unexpected outer layer error:", sys.exc_info()[0])
       return top_friends

#Get mutual friends of a parent node for a given depth
def get_mutals(twitter_api, parent, depth, graph):
    if depth > 0: #0 is the root node
        printF("Number of Nodes so far:", graph.number_of_nodes())
        printF("Parent:", parent)
        #find the top 5 friends and assign them to top5 using the parent node's user_id
        top5 = five_popular(twitter_api, parent[0])
        printF("Top 5 Friends:", top5)
        #add top 5 friends to the graph
        add_popular(parent, top5, graph)
        for i in top5:
            get_mutals(twitter_api, i, depth - 1, graph) #recursion to accomplish the same thing for 5 people

#adds every top 5 friends of each user into the graph
def add_popular(parent, children, graph):
    for i in children:
        graph.add_node((i[0], i[1]))
        graph.add_edge((parent[0], parent[1]), (i[0], i[1]))

#6. Creates a graph from the network and add the reciprocals to it
def make_graph(twitter_api,user_ID,depth):
    network_graph = networkx.nx.Graph()
    seed = nameIds(user_ID)
    network_graph.add_node((seed[0],seed[1]))
    get_mutals(twitter_api,seed,depth, network_graph)
    return network_graph

#prints output to both console and a file using the pickle library
def printF(*args, **kwargs):
    pickle.dump("\n", file1)
    pickle.dump(" ".join(map(str, args)), file1)
    print(" ".join(map(str, args)))

#main
if __name__ == '__main__':
    twitter_api = oauth_login()
    infile = open("outputA.txt", "w+")
#get initial start time to see how long the script ran for at the end
    startTime = datetime.datetime.now()
    printF("STARTING TIME:",str(startTime) )
    screenName = "edmundyu1001"
#make a network of all the nodes with the depth of 3 which will make 5^3 nodes which is 125
    network_graph = make_graph(twitter_api, nameIds(screenName)[0], 3)
#Draw the graph with labels of each node included
    networkx.nx.draw(network_graph, with_labels = 1)
#print out the details for the graph we made to all the outputs: console, detailed documentation file, and main output file
    printF("Total Nodes:", network_graph.number_of_nodes())
    string = "Total Nodes: " + str(network_graph.number_of_nodes() )
    infile.write(string)

    printF("Total Edges:", network_graph.number_of_edges() )
    string = "\nTotal of Edges: "+ str(network_graph.number_of_edges() )
    infile.write(string)

    printF("Diameter: ", networkx.nx.diameter(network_graph))
    string = "\nDiameter: "+ str(networkx.nx.diameter(network_graph) )
    infile.write(string)

    printF("Average Distance: ", networkx.nx.average_shortest_path_length(network_graph))
    string = "\nAverage Distance: " + str(networkx.nx.average_shortest_path_length(network_graph) )
    infile.write(string)
#get the time when program is done
    finishTime = datetime.datetime.now()
    printF("End TIME:", str(finishTime) )

    printF("Total RUNTIME: ", str(finishTime - startTime) )
    string = "Total RUNTIME: " + str(finishTime - startTime)
    infile.write(string)
#creates a png for the graph
    plt.savefig("graph.png")
#show the graph
    plt.show()
#clsoe file writers
    file1.close()
    infile.close()
