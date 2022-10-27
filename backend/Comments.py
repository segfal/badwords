from pmaw import PushshiftAPI
import datetime as dt
import json


class Comments:
    def __init__(self,subreddit,start,end,limit):
        self.subreddit = subreddit
        self.start = start
        self.end = end
        self.limit = limit
        self.api = PushshiftAPI()
        self.comment_keys = ["body","body_sha1","collapsed","collapsed_because_crowd_control","comment_type","controversiality","created_utc","distinguished","id","is_submitter","parent_id","permalink","retrieved_utc","score","score_hidden","subreddit","subreddit_id","subreddit_name_prefixed","subreddit_type"]
    
    def get_comments(self):
        comments = self.api.search_comments(after=self.start,before=self.end,subreddit=self.subreddit,limit=self.limit)
        print(comments)
        
        return comments
    
    def get_table(self):
        comments = self.get_comments()
        table = []
        for comment in comments:
            table.append([comment[key] for key in self.comment_keys if key in comment])
        return table
    
    def get_json(self):
        comments = self.get_comments()
        json_comments = []
        for comment in comments:
            json_comments.append({key:comment[key] for key in self.comment_keys if key in comment})
        #in json comments convert the created_utc to a date string
        for comment in json_comments:
            comment['created_utc'] = dt.datetime.fromtimestamp(comment['created_utc']).strftime("%Y-%m-%d %H:%M:%S")
        

        #create a json file
        x = dt.datetime.now().strftime("%Y_%m_%d_%M %S")
        #remove the spaces from the file name
        x = x.replace(" ","")
        with open(f'comments{x}.json', 'w') as f:
            json.dump(json_comments, f,indent=4)

        return True



#iterative approach
api = PushshiftAPI()
subreddit = "destiny"
start_date = dt.datetime(2022,10,1).timestamp()
end_date = dt.datetime(2022,10,5).timestamp()
limit = 5
comments = api.search_comments(after=start_date,before=end_date,subreddit=subreddit,limit=limit)

print(list(comments))
def get_table(comments):
    comment_keys = ["body","body_sha1","collapsed","collapsed_because_crowd_control","comment_type","controversiality","created_utc","distinguished","id","is_submitter","parent_id","permalink","retrieved_utc","score","score_hidden","subreddit","subreddit_id","subreddit_name_prefixed","subreddit_type"]
    table = []
    for comment in comments:
        table.append([comment[key] for key in comment_keys if key in comment])
    return table
table = get_table(comments)

with open('comments.json', 'w') as f:
    json.dump(table, f,indent=4)
