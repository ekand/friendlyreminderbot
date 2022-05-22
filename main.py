# Task: Open reminders.txt, which contains a list of reminders, and print a random one out.
import os
from load_env import load_twitter_env # function for loading keys!
from time import sleep
import random
import tweepy
from yaml import load, dump
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

# Loading twitter credentials
consumer_key, consumer_secret, access_token, access_token_secret = load_twitter_env()

# Authenticate to Twitter using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connect to the TWITTER API
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def reminder():
    while True:
        with open('reminders.txt') as f: reminder_data = load(f.read(), Loader=Loader)
     
        # Select a random line from the reminders file.
        reminders = []     
        for category_key in reminder_data.keys():
            category_data = reminder_data[category_key]
            for subcategory_key in category_data.keys():
                for reminder_raw_text in category_data[subcategory_key]:
                    reminders.append(reminder_raw_text.strip())

        reminder = random.choice(reminders)
    
        # Random reminder tweets 
        print(reminder)
        #api.update_status(status=reminder)
        # sleeps for 4 hours
        sleep(14400)

if __name__ == "__main__":
   reminder()
