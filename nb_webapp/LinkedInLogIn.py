__author__ = 'jinguangzhou'
from linkedin import linkedin
import oauth2 as oauth
import httplib2
import time, os, simplejson
from xml.etree import ElementTree as ET


# Fill the keys and secrets you retrieved after registering your app
consumer_key = 'gxls9vtr7moe'
consumer_secret = 'efjIUM6aj3Fza2Nh'
user_token = '33713a5e-5c84-48b4-a19d-56f9333d5e99'
user_secret = '2f6c10e6-2413-4fb6-adb4-47c728fbcb2f'

# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)

# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
    key=user_token,
    secret=user_secret)

client = oauth.Client(consumer, access_token)

# Make call to LinkedIn to retrieve your own profile
resp, content = client.request(
    "http://api.linkedin.com/v1/people/id=YknZlHal2Y:(first-name,last-name,id,email-address,phone-numbers,industry)",
    "GET", "")

print content


# By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
resp, content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")

print content



