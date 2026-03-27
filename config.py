import os

# GitHub Secrets에서 가져오도록 환경변수 사용
SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

TO_EMAIL = "kimdj0420@gmail.com, kimdajeong@ibk.co.kr"  # 바꾸고 싶으면 직접 수정
KEYWORD = "은행 or 금융 or AI or 기술"  # 뉴스 검색 키워드
