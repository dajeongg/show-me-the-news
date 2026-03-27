from fetch_news import fetch_news
from send_email import send_email

articles = fetch_news()

subject = "오늘의 금융기술 동향"
body = "📊 오늘의 금융기술 동향\n\n"

for i, a in enumerate(articles, 1):
    short_url = shorten_url(a["url"])  # 🔥 단축 적용
    body += f"{i}. {a['title']}\n{short_url}\n\n"

send_email(subject, body)
