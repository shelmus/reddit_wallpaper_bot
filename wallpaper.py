import praw
import config
import os

def main():
    reddit = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = config.user_agent)

    subreddit = reddit.subreddit("wallpaper")
    for submission in subreddit.stream.submissions(skip_existing=True): #frskip_existing=True
        os.system('wget --trust-server-names -P /home/sean/documents/workspace/reddit_wallpaper_bot/images/wallpaper/ {}'.format(submission.url))

    subreddit = reddit.subreddit("EarthPorn")
    for submission in subreddit.stream.submissions(skip_existing=True):
        os.system('wget --trust-server-names -P /home/sean/documents/workspace/reddit_wallpaper_bot/images/EarthPorn/ {}'.format(submission.url))

if __name__ == "__main__":
    main()
    