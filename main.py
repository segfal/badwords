
from backend import reddit

subreddit = "destiny"
#october 1st 2022
start_date = 1633046400
#today
end_date = 1633046400
limit = 5500
reddit.get_reddit_data(subreddit,start_date,end_date,limit)