import feedparser


def fetch_feed(url: str):
    """
    Fetch and parse an RSS feed.
    """
    return feedparser.parse(url)