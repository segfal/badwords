import datetime as dt 
import time
import json
import os
import Posts as post
import Comments as comment
#print datetime as string

def get_reddit_data(subreddit,start_date,end_date,limit):
    #get the posts
    posts = post.Posts(subreddit,start_date,end_date,limit)
    posts.get_json()
    #after getting the posts get the comments
    time.sleep(10)
    #get the comments
    comments = comment.Comments(subreddit,start_date,end_date,limit)
    comments.get_json()

    return True

subreddit = "destiny"
#october 1st 2022
start_date = dt.datetime(2022,10,1).timestamp()
#today
end_date = dt.datetime.now().timestamp()
limit = 1000
get_reddit_data(subreddit,start_date,end_date,limit)