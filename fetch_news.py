import feedparser
from config import KEYWORD

def fetch_news():
    # 🔥 "은행 or 금융 or AI" → "은행+금융+AI"
    query = KEYWORD.replace(" or ", "+").replace(" ", "")

    url = f"https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR:ko"

    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "url": entry.link,
            "content": entry.summary
        })

    return articles
