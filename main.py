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
