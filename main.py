from flask import Flask, render_template
import requests

app = Flask(__name__)

#Define Endpoint and API keys for retrieving news articles
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
api_key1 = '9e58ca6414334896bd1793b25bf49103'
api_key2 = 'f54b2d435bd547228c270a373172061f'

#Define home route
@app.route('/')
def home():
    #Define list of different news categories
    categories = ['business', 'technology', 'sports', 'entertainment']
    
    news_columns = []
    latest_news = []
    
    #Retrieve news articles in the 'general' category
    params = {'category': 'general', 'country': 'us', 'apiKey': api_key2, 'language': 'en'}
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    latest_articles = response.json().get('articles', [])[:2]
    
    #Add them into the latest_news list
    latest_news.append({
        'latests': latest_articles
    }}
    
    #Retrieve 3 articles from the other categories respectively and add them into the news_column list    
    for category in categories:
        params = {'category': category, 'apiKey': api_key2, 'language': 'en'}
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        articles = response.json().get('articles', [])[:3]
        news_columns.append({
            'category': category.capitalize(),
            'articles': articles
        })    

    return render_template('home.html', news_columns=news_columns, latest_news=latest_news)
