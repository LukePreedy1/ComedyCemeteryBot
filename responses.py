import praw
from utils import *


def execute_comedy(subreddit, num):
    num_posts_replied_to = 0

    posts_replied_to = get_posts_array()

    print("comedy test\n")
    for submission in subreddit.new(limit=num):
        if submission.id not in posts_replied_to:
            submission.reply("/r/comedycemetery")
            posts_replied_to.append(submission.id)
            num_posts_replied_to += 1

        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------------\n")

    print("replied to ", num_posts_replied_to, " posts\n")
    store_posts(posts_replied_to)
