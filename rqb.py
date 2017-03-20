import praw
import return_quote
import pickle
import re
import os
from random import randint

#load word dictionary
word_id = {}

with open("serialize.txt", "rb") as f:
    word_id = pickle.load(f)
    
reddit = praw.Reddit('bot1')

#to avoid posting on the same posts
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

#bot signature
bot_sign = "\n \n ^^(I'm a bot. If I did something unexpected, please contact /u/wellfriedbeans.)"
#iterate through the subreddits

subreddit_list = ["politics", "worldnews", "news", "science", "Showerthoughts"]

for subreddits in subreddit_list:
    
    subreddit = reddit.subreddit(subreddits)
    for submission in subreddit.rising(limit = 50):

        if submission.id not in posts_replied_to:
            words = submission.title.split()

            for word in words:
                if word in word_id:
                    
                    quotes = return_quote.search(word_id[word])
                    submission.reply(">" + quotes[randint(0, len(quotes) - 1)])
                    print("Bot replied to: ", submission.title)

                    posts_replied_to.append(submission.id)
                    break
                
            print("Score: ", submission.score)
            print("\n")

with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
