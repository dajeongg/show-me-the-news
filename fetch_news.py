import feedparser
from config import KEYWORD
from datetime import datetime

def fetch_news():
    query = KEYWORD.replace(" or ", "+").replace(" ", "")

    url = f"https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR:ko"

    feed = feedparser.parse(url)

    today = datetime.utcnow().date()  # 🔥 기준: 오늘 날짜

    articles = []
    for entry in feed.entries:
        published = entry.get("published_parsed")

        if published:
            pub_date = datetime(*published[:6]).date()

            # 🔥 오늘 날짜 뉴스만
            if pub_date == today:
                articles.append({
                    "title": entry.title,
                    "url": entry.link,
                    "content": entry.summary
                })

    return articles[:5]  # 🔥 상위 5개만
