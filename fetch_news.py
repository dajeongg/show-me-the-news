import feedparser
from config import KEYWORD
from datetime import datetime, timedelta

def fetch_news():
    # 🔥 OR 검색으로 변경 (핵심)
    query = KEYWORD.replace(" or ", "%20OR%20")

    url = f"https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR:ko"

    feed = feedparser.parse(url)

    # 🔥 한국 시간 기준
    today = (datetime.utcnow() + timedelta(hours=9)).date()

    articles = []
    for entry in feed.entries:
        published = entry.get("published_parsed")

        if published:
            pub_date = datetime(*published[:6]).date()

            # 🔥 오늘 뉴스만 유지 (원하면 이 부분 제거 가능)
            if pub_date == today:
                articles.append({
                    "title": entry.title,
                    "url": entry.link,
                    "content": entry.summary
                })

    # 🔥 중복 제거 (제목 기준)
    seen = set()
    filtered = []

    for a in articles:
        if a["title"] not in seen:
            filtered.append(a)
            seen.add(a["title"])

    return filtered[:5]  # 🔥 최종 5개
