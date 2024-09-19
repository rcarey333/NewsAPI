import requests
from send_email import send_email

api_key = "5f40975c91644632b2dc7d5000c5d9ea"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-08-19&sortBy=publishedAt&apiKey=5f40975c91644632b2dc7d5000c5d9ea"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"]:
   if article["title"] is not None:
       body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
