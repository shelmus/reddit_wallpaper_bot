import praw
import wget
from os import path

reddit = praw.Reddit('wallpaper_bot')
subreddit = reddit.subreddit("wallpaper")
text_file = open("%sin.txt" % "r_wallpaper_", "a+", errors ='ignore')


for submission in subreddit.top(limit=10):
    url = submission.url
    #text_file.write(url + '\n')
    wget.download(url, "/home/sean/documents/code/python/reddit_wallpaper/images")
# lines_seen = set() # holds lines already seen
# outfile = open("r_wallpaper_out.txt", "w")
# for line in open("r_wallpaper_in.txt", "r"):
#     if line not in lines_seen: # not a duplicate
#         outfile.write(line)
#         lines_seen.add(line)
# outfile.close()

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = config.user_agent)

    return r

def grab_url(r):
    for submission in r.subreddit('earthporn').top(limit=10):
        url = submission.url
        title = submission.title
        print (url)

r = bot_login()
grab_url(r)