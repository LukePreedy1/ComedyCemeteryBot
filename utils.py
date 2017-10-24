import praw



# returns an array of each string in posts_replied_to.txt, which is all the post id's previously replied to
def get_posts_array():
    #if not os.path.isfile("storage\posts_replied_to.txt"):
    #    posts_replied_to = []
    #else:
    with open("storage\posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to

# takes an array of strings of post id, wirtes them to the posts_replied_to.txt
def store_posts(posts_replied_to):
    with open("storage\posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
