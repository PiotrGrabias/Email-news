import requests
from send_email import send_email

API_KEY = "a49bd044c9324b4cad1c349dc5a69f78"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-14&sortBy=publishedAt&" \
      "apiKey=a49bd044c9324b4cad1c349dc5a69f78"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
      title = article.get("title", "")
      description = article.get("description", "")
      if title and description:
            body += title + "\n" + description + "\n\n"

body = body.encode("utf-8")
send_email(body)