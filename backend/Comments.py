from pmaw import PushshiftAPI
import datetime as dt
import json



#iterative approach
api = PushshiftAPI()

#store the comments into sqlite

comment_keys = ["body","body_sha1","collapsed","collapsed_because_crowd_control","comment_type","controversiality","created_utc","distinguished","id","is_submitter","parent_id","permalink","retrieved_utc","score","score_hidden","subreddit","subreddit_id","subreddit_name_prefixed","subreddit_type"]


start_date = int(dt.datetime(2022,10,1).timestamp())
end_date = int(dt.datetime.now().timestamp())

api = PushshiftAPI()
comments = api.search_comments(after=start_date,before=end_date,subreddit="destiny",limit=55000)

def get_tables(comments):
    table = []

    for comment in comments:
        table.append({key:comment[key] for key in comment_keys if key in comment})
    for comment in table:
        comment['created_utc'] = dt.datetime.fromtimestamp(comment['created_utc']).strftime("%Y-%m-%d %H:%M:%S")
    return table

table = get_tables(comments)
#write to json
x = dt.datetime.now().strftime("%Y_%m_%d_%M %S")
x = x.replace(" ","")
with open(f'datasheets/comments{x}.json', 'w') as f:
    json.dump(table, f,indent=4)
