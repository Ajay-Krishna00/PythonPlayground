"""
This is a simple news app that uses the News API to fetch news articles based on the user's input.
"""
'''
The Structure of received json response is as follows:
{
  "status": "ok",
  "totalResults": 100,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "Example.com"
      },
      "author": "John Doe",
      "title": "Example News Title",
      "description": "This is an example description.",
      "url": "https://example.com/news/example-news-title",
      "urlToImage": "https://example.com/images/example-news-title.jpg",
      "publishedAt": "2024-09-29T12:34:56Z",
      "content": "This is the content of the example news article."
    },
    // More articles...
  ]
}
'''

import requests
import os
from dotenv import load_dotenv
import json
import time
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('NEWS_API_KEY')  # Read API key from environment variable

def displayNews(response):
  news = json.loads(response.text)
  if news['totalResults']!=0:
    print(f"\nTotal results found: {news['totalResults']}")
    print("\nThe news articles are: ")
    print("-"*50)
    for i in range(len(news['articles'])):
      print(f"{i+1}. {news['articles'][i]['title']}\n")
      print(f"Description: {news['articles'][i]['description']}\n")
      print(f"Read more: {news['articles'][i]['url']}\n")
      print("-"*50)
    #print(json.dumps(response.json(), indent=4))
  else:
    print("\nNo articles found in the response.")

  # soup = BeautifulSoup(response.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
  # print(soup.prettify())

print("\nWelcome to the News App")

date=time.strftime("%Y-%m-%d")
print("Today's date is: ",date)
YaM=time.strftime("%Y-%m-") #YaM=Year and Month
Date=int(time.strftime("%d"))
FromDate=YaM+str(Date-14)
print("The News are displayed from: ",FromDate)

inp=input("Enter \n 1 to Search for news articles that mention a specific topic or keyword\n 2 to Get the current top headlines for a country or category :\n ")

headers = {
    'User-Agent': 'NewsApp/1.0',
    'Authorization': f'Bearer {API_KEY}'
}

if inp == '1':
  inp=input("\nEnter the topic you want to search for: ")
  url = ('https://newsapi.org/v2/everything?'
        f'q={inp}&'
        f'from={FromDate}&'
        'language=en&'
        f'apiKey={API_KEY}')

  response = requests.get(url, headers=headers)
  displayNews(response)

elif inp =='2':
  inp=input("Enter the country or category you want to search for: ")
  url = ('https://newsapi.org/v2/top-headlines?'
        f'country={inp}&'
        'language=en&'
        f'apiKey={API_KEY}')
  response = requests.get(url, headers=headers)
  displayNews(response)
