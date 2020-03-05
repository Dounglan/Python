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

counter = 0
filehandler = open(b"output.txt","wb")

#This code was taken and modified from Chapter 9 Cookbook
def oauth_login(): #accesses the twitter API, from the cookbook
#original app
    # CONSUMER_KEY = 'BcykI907niRSvaVG9nFq50ZQd'
    # CONSUMER_SECRET = 'ivAGXIU0uP4Efei2PghIEE64luTxRBhW4AbXaxzHwqSDLfqKqW'
    # OAUTH_TOKEN = '1222957955592740864-SnZ3Pp4W8XwJ14JW9LGNDEpELrgxez'
    # OAUTH_TOKEN_SECRET = '2Tobx8BKFfVbojg3z2OeXgmaGyRu60BENfivooHwo60GK'
#backup app(switch to original when done)
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
# A nested helper function that handles common HTTPErrors. Return an updated value for wait_period if the problem is a 500 level error. Block until the
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

def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None, friends_limit=5000, followers_limit=5000):
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

#This function is made to get the user_id and screen_name using twitter's API and return both the user_ID and the name of the account
def get_nameID(screenName):
    try:
        screenName = int(screenName)
        user = make_twitter_request(twitter_api.users.lookup, user_id=screenName)
    except:
        name = screenName.replace(" ","")
        user = make_twitter_request(twitter_api.users.lookup,screen_name=name)
    user = user[0]
    name_id = (user["id"], user["name"])
    return name_id

#In this function for every child add them into the graph
def add_top_5(parent, children, graph):
    for i in children:
        graph.add_node((i[0],i[1]))
        graph.add_edge((parent[0], parent[1]), (i[0],i[1]))

#find the index of the top 5 friends by finding the maximum followers for each friend in the list
def max_5_index(list):
    indexes = []
    #the actual function that will find the maximum number of followers for each person
    def maxIndexFinder(numOfFollowers, acc, num):
        if num > 0 and len(numOfFollowers)!=0:
            try:
                maximum = numOfFollowers[0]
                max_index = 0
                for i in range(len(numOfFollowers)):
                    if (numOfFollowers[i] > maximum):
                        maximum = numOfFollowers[i]
                        max_index = i
                acc.append(max_index)
                numOfFollowers[max_index] = 0
                maxIndexFinder(numOfFollowers, acc, num - 1)
            except:
                #If a user doesn't have any friends this will be returned
                print("ERROR: No Followers found for", acc)
    maxIndexFinder(list, indexes, 5)
    printFunc(indexes)
    return indexes

#This function is made to get reciprocal friends of a parent node for a given depth
def get_recip_friends(twitter_api, parent, depth, graph):
    if depth > 0:
        printFunc("Number of Nodes so far:", graph.number_of_nodes())
        printFunc("Parent:")
        printFunc(parent)

        #find the top 5 friends and assign them to top5 using the parent node's user_id
        top5 = find_top_5_friends(twitter_api, parent[0])

        printFunc("Top 5 Friends:")
        printFunc(top5)

        #add top 5 friends to the graph
        add_top_5(parent, top5, graph)
        for i in top5:
            get_recip_friends(twitter_api, i,depth-1,graph) #recursion to accomplish the same thing for 5 people

"""
This function has a couple of tasks:
1. Get the following and followers of the parent node
2. Find the reciprocals between the two by converting the lists to sets and using the included intersection function
3. Convert that set back into a list and connect them all together by using the join method to concatinate each reciprocal with comas
4. get top five indexes and add the top 5 friends to top_friends
"""
def find_top_5_friends(twitter_api, user_id):
    top_friends = []
    list_of_tuples = []
    followers_nums = []
    try:
        following, followers = get_friends_followers_ids(twitter_api, user_id=user_id, friends_limit=maxint, followers_limit=maxint)
        following = set(following) # Make a set ouf of the two lists to use intersection method
        followers = set(followers)
        printFunc("Following:", followers)
        printFunc("Followers:", following)

        reciprocal = followers.intersection(following)
        reciprocal = list(reciprocal)
        reciprocal = ','.join([str(item) for item in reciprocal[:100]])

        #all_reciprocals =  json.loads(json.dumps(twitter_api.users.lookup(user_id=reciprocal), indent=4))
        all_reciprocals = make_twitter_request(twitter_api.users.lookup,user_id=reciprocal)
        printFunc("Reciprocals:", all_reciprocals)

        for i in all_reciprocals:
            num_followers = i["followers_count"]
            protected_users = i["protected"]
            id = i["id"]
            name = i["screen_name"]
            all_together = (id, name, num_followers, protected_users)
            list_of_tuples.append((all_together))

        #list comprehension to get rid of private accounts
        list_of_actual_users = [x for x in list_of_tuples if x[3] == False]
        print(list_of_actual_users)
        for i in list_of_actual_users:
            #append the num_followers of each person into one single list with the updated Private accounts deleted
            followers_nums.append(i[2])

        #assign the top 5 indexes to five_index
        five_index = max_5_index(followers_nums)
        try:
            for j in five_index:
                top_friends.append((list_of_actual_users[j][0], list_of_actual_users[j][1]))
        except:
            printFunc("Unexpected error:", sys.exc_info())
        printFunc("These are the top 5 friends:")
        printFunc(top_friends)
        return top_friends
    except:
       printFunc("Unexpected outer layer error:", sys.exc_info()[0])
       return top_friends

#This function will make a graph from the tree and add the reciprocals to the tree
def make_recip_tree(twitter_api,user_ID,depth):
    tree = networkx.nx.Graph()
    seed = get_nameID(user_ID)
    tree.add_node((seed[0],seed[1]))
    get_recip_friends(twitter_api,seed,depth,tree)
    return tree

#custom function to print output to both console and a file using the pickle library
def printFunc(*args, **kwargs):
    pickle.dump("\n", filehandler)
    pickle.dump(" ".join(map(str, args)), filehandler)
    print(" ".join(map(str, args)))

#Main method
if __name__ == '__main__':
    twitter_api = oauth_login()
    f = open("Program_Output.txt", "w+")
    #get initial start time to see how long the script ran for at the end
    firstDT = datetime.datetime.now()
    printFunc("\n___________________________________STARTING TIME:",str(firstDT),"___________________________________\n")
    screenName = "edmundyu1001"
    #make a tree of all the nodes with the depth of 3 which will make 5^3 nodes which is 125
    tree = make_recip_tree(twitter_api,get_nameID(screenName)[0],3)
    #Draw the tree graph with labels of each node included
    networkx.nx.draw(tree, with_labels=1)
    #print out the details for the graph we made to all the outputs: console, detailed documentation file, and main output file
    printFunc("Total # of Nodes:", tree.number_of_nodes())
    string = "Total # of Nodes: " + str(tree.number_of_nodes())
    f.write(string)

    printFunc("Total # of Edges:", tree.number_of_edges())
    string = "\nTotal # of Edges: "+ str(tree.number_of_edges())
    f.write(string)

    printFunc("Diameter of the tree:", networkx.nx.diameter(tree))
    string = "\nDiameter of the tree: "+ str(networkx.nx.diameter(tree))
    f.write(string)

    string = "\nAverage Distance:"+ str(networkx.nx.average_shortest_path_length(tree))
    f.write(string)
    printFunc("Average Distance:", networkx.nx.average_shortest_path_length(tree))

    #get the time when the program finished
    lastDT = datetime.datetime.now()
    printFunc("\n___________________________________END TIME:", str(lastDT), "___________________________________\n")
    printFunc("\n___________________________________TOTAL RUNTIME:", str(lastDT-firstDT), "___________________________________\n")
    string = "\nTOTAL RUNTIME:" + str(lastDT-firstDT)
    f.write(string)
    #save a low-resolution picture of the graph
    plt.savefig("Map.png")
    #show the graph
    plt.show()
    #clsoe file writers
    filehandler.close()
    f.close()