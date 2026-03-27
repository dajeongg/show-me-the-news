subject = "📊 오늘의 금융기술 동향"

html_body = """
<div style="font-family: Arial, sans-serif; max-width:600px; margin:auto;">
    
    <h2 style="text-align:center; color:#2c3e50;">
        📊 오늘의 금융·AI 동향
    </h2>
    
    <p style="text-align:center; color:gray;">
        오늘의 주요 뉴스를 한눈에 확인하세요
    </p>

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
                   style="
                        background-color:#4CAF50;
                        color:white;
                        padding:6px 12px;
                        text-decoration:none;
                        border-radius:6px;
                        font-size:14px;">
                   보기
                </a>
            </td>
        </tr>
    """

html_body += """
    </table>

    <p style="margin-top:30px; font-size:12px; color:gray; text-align:center;">
        ⏰ 매일 자동 발송되는 뉴스 요약 서비스입니다
    </p>

</div>
"""

send_email(subject, html_body)
