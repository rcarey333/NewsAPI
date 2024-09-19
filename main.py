import requests

api_key = "5f40975c91644632b2dc7d5000c5d9ea"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5f40975c91644632b2dc7d5000c5d9ea"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descritions
for article in content["articles"]:
   print(article["title"])
   print(article["description"])