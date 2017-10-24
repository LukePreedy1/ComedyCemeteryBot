import praw
from utils import *
from responses import *

reddit = praw.Reddit('bot2')

subreddit = reddit.subreddit('moviebottestingarena')

execute_comedy(subreddit, 10)
