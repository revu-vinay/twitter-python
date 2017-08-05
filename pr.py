import tweepy
import time
import io
import json

consumer_key =''
consumer_secret =''
access_token = ''
access_token_secret =''
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
x= api.trends_place(23424848) #WOEID
try:
    to_unicode  =unicode
except NameError:
    to_unicode  =str
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(x,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
    
    
    
    

    
    
