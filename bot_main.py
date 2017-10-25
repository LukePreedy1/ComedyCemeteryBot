import praw
import pdb
import re
import os
from utils import *
from responses import *

reddit = praw.Reddit(user_agent='ComedyCemeteryBot',
                     client_id='DJ-UATAbPawGOg',
                     client_secret='mOtMSbPavtUOck9uJm7nWk5BdeY',
                     username='ComedyCemeteryBot',
                     password='Yourface1234')

subreddit = reddit.subreddit('funny')

execute_comedy(subreddit, 100)
