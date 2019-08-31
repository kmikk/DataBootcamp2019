#!/usr/bin/env python
# coding: utf-8

# # Unit 12 - Homework 10: Mission to Mars with Web Scraping

# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
# 
# Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
# 
# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
# 
# Store the return value in Mongo as a Python dictionary.
# 
# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
# 
# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

# ## Setup

# In[8]:


# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd


# In[9]:


# Splinter Setup
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[10]:


def scrape():
    final = {}
    output = mars_news()
    final["mars_headline"] = output[0]
    final["mars_teaser"] = output[1]
    final["mars_image"] = marsimg()
    final["mars_weather"] = marsweather()
    final["mars_table"] = marsfacts()
    final["mars_astro"] = marsastro()

    return final


# ## NASA Mars News
# 
# ### Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[11]:


def mars_news():
    mars_news_url = 'https://mars.nasa.gov/news'
    browser.visit(mars_news_url)
    response = requests.get(mars_news_url)
    soup = bs(response.text, 'html.parser')
    news_title = soup.find('div', class_="content_title").text.strip()
    news_p = soup.find('div', class_="rollover_description_inner").text.strip()
    output = [news_title, news_p]
    return output


# ## JPL Mars Space Images - Featured Image
# 
# ### Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

# In[12]:


def marsimg():
    # URL of page to be scraped
    jpl_url = "https://www.jpl.nasa.gov"
    mars_search = "/spaceimages/?search=&category=Mars"
    # Retrieve page with the requests module
    response = requests.get(jpl_url + mars_search)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')
    # Find the featured image
    featured_image = soup.find('article')['style']
    # Slice off unneeded bits
    start = featured_image.find("url('")
    end = featured_image.find("');")
    relative_image_path = featured_image[start+len("url('"):end]
    relative_image_path
    # Create full path to featured image
    mars_img = jpl_url + relative_image_path
    return mars_img


# ## Mars Weather
# 
# ### Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

# In[13]:


def marsweather():
    # URL of page to be scraped
    mars_wx = "https://twitter.com/marswxreport?lang=en"
    # Retrieve page with the requests module
    response = requests.get(mars_wx)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')
    # Get tweet and clean up
    mars_weather = soup.find('div', class_="js-tweet-text-container").text.strip()
    mars_weather = mars_weather.replace('\n', '')
    return mars_weather


# ## Mars Facts
# 
# ### Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. https://space-facts.com/mars/
# 
# ### Use Pandas to convert the data to a HTML table string.

# In[14]:


def marsfacts():
   # Set URL for scraping
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    # Use read_html to read tabular data
    tables=pd.read_html(facts_url)
    # Select and format the correct table
    mars_facts = tables[0]
    mars_facts.columns = ['Mars - Earth Comparison', 'Mars', 'Earth']
    # Set index
    mars_facts.set_index('Mars - Earth Comparison', inplace=True)
    # Save dataframe as an HTML table
    mars_table = mars_facts.to_html(index=True, header=True)
    return mars_table


# ## Mars Hemispheres
# 
# ### Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# 
# ### You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# ### Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# 
# ### Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 

# In[15]:


def marsastro():
  # Set URL for Splinter
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)  
    # HTML object
    hemispheres_html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(hemispheres_html, 'html.parser')
    # Retrieve all elements that contain relevant information
    items = soup.find_all('div', class_='item')
    # Create Empty List
    hem_img_urls = []
    # Store Main URL
    astro_url = 'https://astrogeology.usgs.gov'
    # Loop through the stored items
    for i in items: 
        # Store title
        title = i.find('h3').text
    
        # Store full image link
        partial_url = i.find('a', class_='itemLink product-item')['href']
    
        # Visit full image link 
        browser.visit(astro_url + partial_url)
    
        # HTML Object of  hemisphere information website 
        partial_url = browser.html
    
        # Parse HTML with Beautiful Soup 
        soup = bs(partial_url, 'html.parser')
    
        # Retrieve full image source 
        img_url = astro_url + soup.find('img', class_='wide-image')['src']
    
        # Append the retreived information into a list of dictionaries 
        hem_img_urls.append({"title" : title, "img_url" : img_url})
    return hem_img_urls


# In[ ]:





# In[ ]:




