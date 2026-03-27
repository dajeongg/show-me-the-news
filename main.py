from news import fetch_news
from send_email import send_email
from utils import shorten_url  # 있으면 사용

# 🔥 1. 뉴스 가져오기 (이게 없어서 에러난거)
articles = fetch_news()

# 🔥 2. 단축 링크 생성 (선택)
for a in articles:
    a["short_url"] = shorten_url(a["url"])

# 🔥 3. HTML 메일 만들기
subject = "📊 오늘의 금융기술 동향"

html_body = """
<div style="font-family: Arial, sans-serif; max-width:600px; margin:auto;">
    
    <h2 style="text-align:center; color:#2c3e50;">
        📊 오늘의 금융·AI 동향
    </h2>

    <table style="border-collapse: collapse; width:100%; margin-top:20px;">
        <tr style="background-color:#4CAF50; color:white;">
            <th style="padding:10px;">No</th>
            <th style="padding:10px;">기사 제목</th>
            <th style="padding:10px;">바로가기</th>
        </tr>
"""

for i, a in enumerate(articles, 1):
    html_body += f"""
        <tr>
            <td style="padding:10px; text-align:center;">{i}</td>
            <td style="padding:10px;">{a['title']}</td>
            <td style="padding:10px; text-align:center;">
                <a href="{a['short_url']}" 
                   style="background-color:#4CAF50; color:white; padding:6px 12px; text-decoration:none; border-radius:6px;">
                   보기
                </a>
            </td>
        </tr>
    """

html_body += """
    </table>
</div>
"""

# 🔥 4. 메일 보내기
send_email(subject, html_body)
