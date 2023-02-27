#!/usr/bin/python3 
"""query top 10 posts"""
import request


def top_ten(subreddit):
    """return first 10 post"""
    header = {"User-Agent": "Holberton")
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for i in r.json().get("data", None).get("children", None):
            print(i.get("data", None).get("title", None))
    else:
        print(None)

if __name__=="__main__":
    pass
