import os

SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

# 🔥 여러 명 (BCC용)
TO_EMAILS = [
    "kimdj0420@gmail.com"
]

# 🔥 검색 키워드
KEYWORD = "은행 OR 금융 OR AI OR 기술"
