from fetch_news import fetch_news
from send_email import send_email

articles = fetch_news()

# 🔥 메일 제목
subject = "오늘의 금융기술 동향"

# 🔥 메일 본문 만들기
body = "📊 오늘의 금융기술 동향\n\n"

for i, a in enumerate(articles, 1):
    body += f"{i}. {a['title']}\n{a['url']}\n\n"

# 🔥 한 번만 발송
send_email(subject, body)
