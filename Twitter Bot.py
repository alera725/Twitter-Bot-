#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:52:27 2019

@author: Aera
"""

import tweepy #The Twitter API
from tkinter import * #For the GUI
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data

#%% Codigos de autorizacion
consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_token = 'XXXX'
access_token_secret = 'XXXX'

#%% Abrir conexion con la API de tweeter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

#%% Seguir a mis seguidores 

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

#%% Buscar palabra clave y retweet o marcar como favorito
    
search = "Bitcoin" # Choose the word you want to interact
numberOfTweets = 3
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet() #tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
        
#%% Interactuar respondiendo a un tweet con un usuario especifico
date = datetime.now().strftime("At: %H:%M:%m-%d-%y")
phrase = "%s... trying bot twitter" %date
try:
    tweetId = 1234567890 #User ID
    username = 'username' #Username
    api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
    print ("Replied with " + phrase)
except tweepy.TweepError as e:
    print(e.reason)



    
    
    
    
    
    
