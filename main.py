from flask import Flask, render_template
import requests

app = Flask(__name__)

# Define Endpoint and API keys for retrieving news articles
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
api_key1 = '9e58ca6414334896bd1793b25bf49103'
api_key2 = 'f54b2d435bd547228c270a373172061f'

# Define home route
@app.route('/')
def home():
    # Define list of different news categories
    categories = ['business', 'technology', 'sports', 'entertainment']
    
    news_columns = []
    latest_news = []
    
    # Retrieve news articles in the 'general' category
    params = {'category': 'general', 'country': 'us', 'apiKey': api_key2, 'language': 'en'}
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    latest_articles = response.json().get('articles', [])[:2]
    
    # Add them into the latest_news list
    latest_news.append({
        'latests': latest_articles
    }}
    
    # Retrieve 3 articles from the other categories respectively and add them into the news_column list    
    for category in categories:
        params = {'category': category, 'apiKey': api_key2, 'language': 'en'}
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        articles = response.json().get('articles', [])[:3]
        news_columns.append({
            'category': category.capitalize(),
            'articles': articles
        })    

    return render_template('home.html', news_columns=news_columns, latest_news=latest_news)

# Define route for a specific news category         
@app.route('/news/<topic>')
def topic(topic):
    # Retrieve articles in the specified news category     
    params = {'category': topic, 'apiKey': api_key1, 'language': 'en'}
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    articles = response.json().get('articles')
        
    # Render the html template with the articles       
    return render_template('news.html', articles=articles, topic=topic.capitalize())

# Define route for a specific news keyword          
@app.route('/news/search/<keyword>')
def keyword(keyword):
    # Retrieve articles in the specified news keyword
    params = {'q': keyword, 'apiKey': api_key1, 'language': 'en'}
    response = requests.get(NEWS_API_ENDPOINT2, params=params)
    articles = response.json().get('articles')
        
    # Render the html template with the articles    
    return render_template('search.html', articles=articles, keyword=keyword.capitalize())        

# Define route to access javascript styling file for footer        
@app.route('/news/static/footer_news.js')
def news_static_footer_news():
    return app.send_static_file('footer_news.js')
        
@app.route('/news/search/static/footer_news.js')
def news_search_static_footer_news():
    return app.send_static_file('footer_news.js')        

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9000, threaded=True)        
