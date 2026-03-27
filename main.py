from fetch_news import fetch_news
# from summarize_news import summarize  # 🔴 나중에 다시 쓸 때 주석 해제
from send_email import send_email

articles = fetch_news()

for a in articles:
    content = a.get("content") or a.get("title")

    # 🔴 AI 요약 (현재는 비활성화)
    # summary = summarize(content)

    # 🔴 지금은 요약 대신 제목 + 링크만 보냄
    body = f"{a['title']}\n{a['url']}"

    send_email(a["title"], body)
