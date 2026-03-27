import feedparser
from config import KEYWORD
from urllib.parse import quote

def fetch_news():
    encoded_keyword = quote(KEYWORD)

    url = f"https://news.google.com/rss/search?q={encoded_keyword}&hl=ko&gl=KR&ceid=KR:ko"
    
    feed = feedparser.parse(url)

    articles = []
    seen_titles = set()

    for entry in feed.entries:
        title = entry.title
        link = entry.link

        if title in seen_titles:
            continue
        seen_titles.add(title)

        articles.append({
            "title": title,
            "url": link
        })

        if len(articles) >= 5:
            break

    return articles
