#Dounglan Cheung
#2.28.2020
#CIS 400, Assignment2
#UNCOMMMENT TEH 3 LINES after RUNNING OUTPUT on step 6 usage
import twitter
import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
from functools import partial
from sys import maxsize as maxint

def oauth_login(): #accesses the twitter API
    # CONSUMER_KEY = 'BcykI907niRSvaVG9nFq50ZQd'
    # CONSUMER_SECRET = 'ivAGXIU0uP4Efei2PghIEE64luTxRBhW4AbXaxzHwqSDLfqKqW'
    # OAUTH_TOKEN = '1222957955592740864-SnZ3Pp4W8XwJ14JW9LGNDEpELrgxez'
    # OAUTH_TOKEN_SECRET = '2Tobx8BKFfVbojg3z2OeXgmaGyRu60BENfivooHwo60GK'
    #backup
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
# Sample usage
#twitter_api = oauth_login()
##friends_ids, followers_ids = get_friends_followers_ids(twitter_api, screen_name, friends_limit=5000, followers_limit=5000)
#friends_ids, followers_ids = get_friends_followers_ids(twitter_api, screen_name=user, friends_limit=5000, followers_limit=5000)
#print("Friends:", friends_ids,"\nFollowers: ", followers_ids)

#3.use the 2 lists to find reciprocal friends
def reciprocal_friends(friends_ids, followers_ids):
    set1 = set(friends_ids) #friends set
    set2 = set(followers_ids) #followers set
    set3 = set1 & set2 #find the intersection of the two
    reciprocal = list(set3)  #turns the set to a list
    print("Mutual friends and followers: ", reciprocal)
    return reciprocal #returns the list of mutual friends
##usage
#reciprocal = reciprocal_friends(friends_ids, followers_ids)

#4.from that list, select 5 most popular friends(determined by their followers_count)
def num_followers(twitter_api, user_id=None, followers_limit=5000): #helper function to get the five followers, followers_count
    # Must have either screen_name or user_id (logical xor)
    get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids, count=5000)
    followers_ids = [] #the list for the five followers
    for twitter_api_func, limit, ids, label in [ [get_followers_ids, followers_limit, followers_ids, "followers"] ]: #some of the code is from the cookbook
        if limit == 0: continue
        cursor = -1
        while cursor != 0:
            # Use make_twitter_request via the partially bound callable...
            response = twitter_api_func(user_id=user_id, cursor=cursor)
            if response is not None:
                ids += response['ids']
                cursor = response['next_cursor']
#XXX: You may want to store data during each iteration to provide an additional layer of protection from exceptional circumstances
            if len(ids) >= limit or response is None:
                break
    # Do something useful with the IDs, like store them to disk...
    return len(ids)

def popular(reciprocal): #this function actually find the top 5 friend with the highet follower count
    followers_list = []
    top_five = []
    for a in range(len(reciprocal)): #loops until it finishes the five friends
        followers_list.append(num_followers(twitter_api,user_id=reciprocal[a], followers_limit=5000)) #adds the friends to an empty list

    idWithFollowers = list(zip(reciprocal, followers_list)) #zips the friend with their user id

    idWithFollowers = sorted(idWithFollowers, key=lambda x:x[1], reverse = True) #sorts it from highest to lowest(top 5 highest

    for i in range(5):
        top_five.append(idWithFollowers[i]) #appends to the top 5 list
    idFollowers, numF = list(zip(*top_five) ) #numF is the number of followers of the top 5 followers of the user
    print("Top 5 followers' ids: ", idFollowers)
    return idFollowers
##usage
#popular(reciprocal)

#5.Repeat this process(Steps 2, 3 & 4)for each of the distance 1 friends, then distance 2 friends, so on, using a crawler , until at least 100 users/nodes. modify crawl_followers() function from cookbook(Retrieves only followers, so need to modify to get both followers and friends, in order to compute the reciprocal friends)
def crawl_followers(twitter_api, screen_name): #from cookbook but modified
    friends, followers = get_friends_followers_ids(twitter_api, screen_name=user, friends_limit=5000, followers_limit=5000)
    response = popular(reciprocal_friends(friends, followers))

    ids = next_queue = response #sets the ids and next_queue as the top 5 friends
    depth = 1 #root node
    max_depth = 3 #the amount of nodes is 5^(max_depth - depth) so 125 users/nodes
    while depth < max_depth:
        depth += 1
        (queue, next_queue) = (next_queue, []) #sets the queue as the top 5 friends and next_ queue as a empty list for the next group of top 5 friends for each user/node
        for id in queue: #repeats getting the top 5 for each user
            friends, followers = get_friends_followers_ids(twitter_api, user_id = id, friends_limit=5000, followers_limit=5000)
            response = popular(reciprocal_friends(friends, followers))
            next_queue += response
            ids += next_queue
    print("The other friends of friends: ", ids)
    return ids #returns all the ids of the users
    #usage
#crawl_followers(twitter_api, screen_name=user)

#6.create social network based on results(nodes and edges, using networkX package)
import networkx as nx
def social_net(twitter_api, screen_name):
    n_graph = nx.Graph() #graph name
    friends, followers = get_friends_followers_ids(twitter_api, screen_name, friends_limit=5000, followers_limit=5000) #gets the crawl function for the users/nodes
    response = popular(reciprocal_friends(friends, followers)) #(original)
    # ids = next_queue = popular(reciprocal_friends(friends, followers)) #new
#    graph_info = [] #new
#    graph[screen_name] = list[ids] #new
    for i in range(5): #original
        n_graph.add_edge(screen_name, response[i])
    next_ids = next_queue = response #from the cookbook
    depth = 1
    max_depth = 4
    while depth < max_depth:
        depth += 1
        (queue, next_queue) = (next_queue, []) #sets the queue as the top 5 friends and next_ queue as a empty list for the next group of top 5 friends for each user/node
        for id in queue: #repeats until there are at least 100 users/nodes
            friends, followers = get_friends_followers_ids(twitter_api, user_id=id, friends_limit=5000, followers_limit=5000) #sets friends as the friends list and followers list
            response = popular(reciprocal_friends(friends, followers)) #sets response as the top 5 friends
            next_queue += response
            for n in range(5):
                n_graph.add_edge(id, response[n])  #original
                next_ids += next_queue #it was in the for id in queue loop for original
    print(nx.info(n_graph))
    return next_ids


#usage
twitter_api = oauth_login()
social_net(twitter_api, screen_name)
#UNCOMMMENT TEH 3 LINES after RUNNING OUTPUT
# plt.figure(figsize=(5,5))
# nx.draw_networkx(n_graph)
# plt.show()


#7.calculate diameter and avg distance of network using using certain built in functions provided by Networkx (in 3.22 Distance Measures & 3.48 Shortest Paths, or your own functions if you prefer.
#creates the graph
def graph(next_ids):
    g = nx.graph()
    g.add_nodes_from(next_ids) #creates nodes from the users ids
    for j in next_ids.items():
        g.add_edges_from([ (j,k) for k in y ]) #adds edges to the id nodes
    data = json_graph.node_link_data(G)
    with open('data.json', 'w', encoding ='utf-8') as f: json.dump(data, f, ensure_ascii=False, indent=4)
    diameter = nx.diameter(n_graph) #calculates diameter
    avg_distance = nx.average_shortest_path_length(n_graph)  #calculates the average distance
    print("Diameter: ", diameter, "\nAverage Distance: ", avg_distance)

#usage
#    graph(social_net(twitter_api, screen_name))

#main function
# if __name__ == "__main__":
# def main():
#     twitter_api = oauth_login()
#     user = "edmundyu1001"
#
#     friends_ids, followers_ids = get_friends_followers_ids(twitter_api, screen_name=user, friends_limit=5000, followers_limit=5000)
#     print("Friends: ", friends_ids ,"\nFollowers: ", followers_id )
#
#     setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids)
#
#     reciprocal = reciprocal_friends(friends_ids, followers_ids, screen_name = None, user_id = None, limit = 5000)
#
# idFollowers = popular(reciprocal)  # gets the top 5 followers
#
# ids = crawl_followers(twitter_api, screen_name)
#
# next_ids = social_net(twitter_api, screen_name=user)
# plt.figure(figsize=(5, 5))
# nx.draw_networkx(n_graph)
# plt.show()
#
# graph(next_ids)  # creates the graph and calculates the diameter and avg distance
#main()
#end