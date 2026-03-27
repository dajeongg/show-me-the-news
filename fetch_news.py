import feedparser
from config import KEYWORD

def fetch_news():
    url = f"https://news.google.com/rss/search?q={KEYWORD}&hl=ko&gl=KR&ceid=KR:ko"
    
    feed = feedparser.parse(url)

    articles = []
    seen_titles = set()

    for entry in feed.entries:
        title = entry.title
        link = entry.link

        # 🔥 중복 제거
        if title in seen_titles:
            continue
        seen_titles.add(title)

        articles.append({
            "title": title,
            "url": link
        })

        # 🔥 최대 5개
        if len(articles) >= 5:
            break

    return articles
