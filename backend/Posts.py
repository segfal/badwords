from time import time
from pmaw import PushshiftAPI
import datetime as dt
import json
import os


class Posts:
    def __init__(self, subreddit, start_date, end_date,limit):
        self.subreddit = subreddit
        self.start_date = start_date
        self.end_date = end_date
        self.limit = limit
        self.api = PushshiftAPI()
        self.post_keys = ['title','selftext','created_utc','author','id','score','num_comments','permalink','url','subreddit']
    def get_posts(self):
        posts = self.api.search_submissions(subreddit=self.subreddit,after=self.start_date,before=self.end_date,limit=self.limit)
        return posts
    def get_table(self):
        posts = self.get_posts()
        table = []
        for post in posts:
            table.append([post[key] for key in self.post_keys])
        
        
        return table
    def get_json(self):
        posts = self.get_posts()
        json_posts = []
        for post in posts:
            json_posts.append({key:post[key] for key in self.post_keys if key in post})
        #in json posts convert the created_utc to a date string
        for post in json_posts:
            post['created_utc'] = dt.datetime.fromtimestamp(post['created_utc']).strftime("%Y-%m-%d %H:%M:%S")
        #create a json file
        #if json file exists create a new one

        x = dt.datetime.now().strftime("%Y_%m_%d_%M %S")
        x = x.replace(" ","")
        with open(f'posts{x}.json', 'w') as f:
            json.dump(json_posts, f,indent=4)

        return True


