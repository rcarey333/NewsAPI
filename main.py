import requests
from send_email import send_email

topic = "tesla"

api_key = "5f40975c91644632b2dc7d5000c5d9ea"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&" \
    "apiKey=5f40975c91644632b2dc7d5000c5d9ea&" \
    "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"]:
   if article["title"] is not None:
       body = "Subject: Today's news" \
               + "\n" + body + article["title"] + "\n" \
               + str(article["description"]) \
               + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
