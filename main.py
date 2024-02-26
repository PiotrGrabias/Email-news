import requests
from send_email import send_email

topic = "microsoft"
API_KEY = "a49bd044c9324b4cad1c349dc5a69f78"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2024-01-14&sortBy=publishedAt&" \
      "apiKey=a49bd044c9324b4cad1c349dc5a69f78&language=en"

request = requests.get(url)
content = request.json()
body = "Subject: Today's news"
for article in content["articles"][:20]:
    title = article.get("title", "")
    description = article.get("description", "")
    if title and description:
        body += title + "\n" + description + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(body)