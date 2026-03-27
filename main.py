import requests
from fetch_news import fetch_news
from send_email import send_email

def shorten_url(url):
    api = f"http://tinyurl.com/api-create.php?url={url}"
    return requests.get(api).text

articles = fetch_news()

subject = "오늘의 금융기술 동향"
body = "📊 오늘의 금융기술 동향\n\n"

for i, a in enumerate(articles, 1):
    short_url = shorten_url(a["url"])
    body += f"{i}. {a['title']}\n{short_url}\n\n"

send_email(subject, body)
