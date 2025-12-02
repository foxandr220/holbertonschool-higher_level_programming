#!/usr/bin/python3
"""Functions to fetch posts and save them using the requests module"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print the status code and titles"""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them in a CSV file: posts.csv"""
    response = requests.get(API_URL)

    if response.status_code != 200:
        return

    posts = response.json()

    # convert posts to list of dicts with keys id, title, body
    rows = [
        {"id": post["id"], "title": post["title"], "body": post["body"]}
        for post in posts
    ]

    # Write CSV
    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(rows)
