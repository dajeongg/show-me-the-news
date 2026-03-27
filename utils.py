import requests

def shorten_url(url):
    try:
        api = f"http://tinyurl.com/api-create.php?url={url}"
        return requests.get(api).text
    except:
        return url  # 실패하면 원본
