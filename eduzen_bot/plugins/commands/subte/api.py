from datetime import datetime

import structlog
import tweepy
from emoji import emojize

from keys import TWITTER

logger = structlog.get_logger(filename=__name__)
metro = emojize(":metro:", use_aliases=True)


def get_tweets(api, username, count, date):
    tweets = [
        tweet.text
        for tweet in api.user_timeline(username, count=count)
        if (date - tweet.created_at).days < 1
    ]
    if not tweets:
        return f"No hay novedades de subtes {metro} para hoy"

    return "\n".join(tweets)


def get_subte(count=20):
    if count > 20:
        count = 20
    auth = tweepy.OAuthHandler(TWITTER["CONSUMER_KEY"], TWITTER["CONSUMER_SECRET"])
    auth.set_access_token(TWITTER["ACCESS_TOKEN"], TWITTER["ACCESS_TOKEN_SECRET"])
    api = tweepy.API(auth)
    now = datetime.now()
    today = now.date().isoformat()
    data = get_tweets(api, "subteba", count=count, date=now)
    data = f"Estado Subtes {metro} BA by @subteba ({today}):\n{data}"
    return data
