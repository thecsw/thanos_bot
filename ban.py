import praw
import sqlite3
import random

import config
import database

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

subreddit = reddit.subreddit('thanosdidnothingwrong')

conn = sqlite3.connect("thanos.db")

def find_users():
    print("Starting searching...")
    for comment in subreddit.comments(limit=100):
        print(f"Doing {comment.id}")
        author = comment.author
        if (not database.is_logged(conn, author)):
            database.add_user(conn, author, comment.id)
            print(f"Added {author}")

def ban_users():
    all_users = database.get_all()
    banned = [x for x in all_users if random.randint(1, 100) % 2 == 0]
    # list banned will contain everyone that needs to get banned
    
database.init_database(conn)
find_users()
conn.close()
