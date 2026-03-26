import feedparser
from config import KEYWORD

def fetch_news():
    url = f"https://news.google.com/rss/search?q={KEYWORD}"
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:5]:  # 최신 5개 뉴스
        articles.append({
            "title": entry.title,
            "url": entry.link,
            "content": entry.summary
        })
    return articles
