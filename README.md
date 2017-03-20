# RelevantQuotesBot
The  [RelevantQuotesBot](https://www.reddit.com/user/RelevantQuotesBot/?sort=top) of Reddit fame.
Created by Ameya Daigavane.

# The Idea
Reddit is an extremely popular social news aggregation and discussion website, ranking as the #7 most visited web-site in the US.
RQB searches titles of popular posts in certain subreddits (smaller communities for specific topics), and comments with relevant quotes. 
 
# The Execution
RQB first creates a dictionary of hitwords - by sampling a popular quotes website, [BrainyQuote](https://www.brainyquote.com/quotes/topics.html).
It scrapes each of these 'topics' pages for quotes - making a list of top quotes for each word.

When the bot is run, it searches the subreddit posts for these hitwords.
If a hitword is found, it randomly selects a quote from the hitword's list, and posts it as a reply.

# RQB has the top comment on the top post of /r/politics, just after 4 hours of deployment!
Currently 1805 upvotes and rising!
![](https://github.com/ameya98/RelevantQuotesBot/blob/master/Screenshot%20(4).png)

This was the profile overview after around 4 hours of deployment:
![](https://github.com/ameya98/RelevantQuotesBot/blob/master/Screenshot%20(5).png)
# This would not have been possible without...
[PRAW](https://praw.readthedocs.io/en/latest/), [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Requests](http://docs.python-requests.org/en/master/), [Python For Engineers](http://pythonforengineers.com) and all of my friends and family.
