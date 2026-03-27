from fetch_news import fetch_news
# from summarize_news import summarize
from send_email import send_email

articles = fetch_news()
for a in articles:
    content = a["content"] or a["title"]
  #  summary = summarize(content)
    send_email(a["title"], summary + "\n" + a["url"])
