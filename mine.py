# Twitter REST API v1.1 GET statuses/user_timeline script
# oauth2 library must be installed
 
import oauth2 as oauth
import urllib2 as urllib
import json
from time import sleep
import os
import pickle
 
TopDCfoodtrucks = ["pepebyjose", "LobstertruckDC", "dcslices", "DCEmpanadas", "CapMacDC", "bigcheesetruck", "TaKorean", "bbqbusdc", "hulagirltruck", "Borinquenlunchb"] 

# insert credentials
access_token_key = 
access_token_secret = 
 
consumer_key = 
consumer_secret = 
 
_debug = 0
 
oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
#Token = (key=access_token_key, secret=access_token_secret)


signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
 
http_method = "GET"
 
 
http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)
 
'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
    token=oauth_token,
    http_method=http_method,
    http_url=url, 
    parameters=parameters)
 
    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)
 
    headers = req.to_header()
 
    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()
 
    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
 
    response = opener.open(url, encoded_post_data)
 
    return response
     
def fetchsamples():
    global start_id
    global filenum
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    parameters = {'screen_name': username,    # name of twitterer
        'include_rts': 1,    # Include retweets
        'count': 200, # number of tweets (200 max)
        'max_id': str(start_id),        # start from this tweet and work back
        'since_id': str(stop_id)}    # dont get any tweets older than this, cause we already got them    
    response = twitterreq(url, "GET", parameters)
    data = json.load(response)
    with open(username+filenum+'.json','w') as outfile:
        json.dump(data, outfile)
        for tweet in data:
            start_id = tweet['id_str'].encode('utf-8')
            print(start_id)
            masterdict[username][tweet['id_str']] = {}
            masterdict[username][tweet['id_str']]['created_at'] = tweet['created_at']
            masterdict[username][tweet['id_str']]['text'] = tweet['text']
            masterdict[username][tweet['id_str']]['retweet_count'] = tweet['retweet_count']
            masterdict[username][tweet['id_str']]['favorite_count'] = tweet['favorite_count']
            masterdict[username][tweet['id_str']]['screen_name'] = tweet['user']['screen_name']
            masterdict[username][tweet['id_str']]['followers_count'] = tweet['user']['followers_count']
            masterdict[username][tweet['id_str']]['in_reply_to_user_id'] = tweet['in_reply_to_user_id']
    start_id = int(start_id) - 1
    print(start_id)
    tempfilenum = int(filenum) + 1
    filenum = str(tempfilenum)
    print(filenum)
 
#### Remember to: 
#### Go Grab a two week old Tweet from your profile, and set that id as start_id
#### Correct screen_name?
#### Correct outfile?
 
 
usernames = ["LobstertruckDC", 'pepebyjose', 'LobstertruckDC', 'dcslices', 'DCEmpanadas', 'CapMacDC', 'bigcheesetruck', 'TaKorean', 'bbqbusdc', 'hulagirltruck', 'Borinquenlunchb']
#usernames = ["LobstertruckDC"]
try:
    if type(masterdict) is dict:
        pass
 
except:
    masterdict = {}
  
     
for username in usernames:
    start_id = int('1125127903971295232')
    stop_id = int('0012')
    filenum = str(00)
    print(username)
    masterdict[username] = {}
         
 
         
    if os.path.isfile(username+'0.json') is False:    # range = 16 will collect up to 3,200 tweets if count = 200
        for i in range(16):
            print('on page ') + str(i)
            fetchsamples()
            sleep(5)