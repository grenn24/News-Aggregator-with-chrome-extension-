# News Aggregator (with chrome extension)

News Aggregator webpage that displays news articles from various categories, developed using front-end HTML and back-end Python using Flask framework

# Functions
- Extracts various news articles from separate customisable categories and the latest articles from the general category
- Provides a neat summary of every news article for easy reading
- Displays each article in a modern card layout for easy viewing
- Allows users to search for specific news articles based on different key words as filters

# Description

## Python Code
Flask library is imported to create an application.\
Requests library is imported to make HTTP requests to a news api server.

Two main routes are defined:

1. **Home Route '/'**

   Creates a list of different news categories, and fetches a unique list of news articles from the news api, grouping them based on category.\
   A separate request is made for latest_news list under 'general' category.\
   The list of news articles are transferred over to the home.html template as arguments.

2. **News Route '/News/[topic]'**

   Fetches a list of news articles belonging to a specific topic listed under navigation pane.\
   News topic parameter and article list are passed down to the news.html template as arguments.

3. **Search Route '/News/Search/[keyword]'**

   Fetches a list of news articles belonging to a specific keyword based on search input by the user.\
   News keyword parameter and article list are passed down to the search.html template as arguments.

## HTML Code
Uses flexbox design to achieve the desired card layout, etc. single-columns & columns of three respectively.\
In the home page, two nested for-loops are used to iterate over each news category and the corresponding news articles.\
This allows for new categories to be added or deleted from the webpage easily with minimal change in code.\
A search form at the bottom of the webpage sends a HTML Get request to the /news/[topic] URL with the user input as the topic parameter.\
The home page is then rerouted to the news page displaying a list of curated articles belonging to the user-specified category.\
In the news and search page, a similar for-loop function is used to iterate over each news article before displaying them in a single-column card format.

# Requirements
- Python 3.6 or higher
- Flask installation
- Requests library
- Unique NewsAPI key (or any News Endpoint URL)

# Installation
- Download the 'News Aggregator.crx' file in the root folder
- In Google Chrome, type "chrome://extensions" to enter the extensions page
- Toggle the 'Developer Mode' switch on
- Drag and drop the 'News Aggregator.crx' file into the extensions page
- Click 'Add Extension' to begin the installation process

Application Web Host: https://boiled-bubbly-poultry.glitch.me/
