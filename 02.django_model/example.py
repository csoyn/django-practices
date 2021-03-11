import requests

for _ in range(10):
    requests.get('http://127.0.0.1:8000/articles/create/?title=제목&content=내용')

