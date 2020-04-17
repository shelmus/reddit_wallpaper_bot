import praw
import config
import os

def main():
    reddit = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = config.user_agent)

    subreddit = reddit.subreddit("wallpaper")1
    for submission in subreddit.stream.submissions(): #frskip_existing=True
        os.system('wget --trust-server-names -P /home/sean/workspace/ripwalls/images/wallpaper/ {}'.format(submission.url))

        # with open('/home/sean/workspace/personal/python/reddit_wallpaper/url.log', 'r+') as f:
        #     for line in f.read():
        #         if submission.url in line:
        #             break
        #         else: # not found
        #             print >>f, submission.url

    subreddit = reddit.subreddit("EarthPorn")
    for submission in subreddit.stream.submissions(skip_existing=True):
        os.system('wget --trust-server-names -P /home/sean/workspace/ripwalls/images/EarthPorn/ {}'.format(submission.url))

if __name__ == "__main__":
    main()
    