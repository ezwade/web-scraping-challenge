
from IPython import get_ipython
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd

url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
response = requests.get(url)



soup = BeautifulSoup(response.text, 'html.parser')



news_title = soup.find('div', class_ = 'content_title').text.lstrip()


news_title



news_p =  soup.find('div', class_ = 'rollover_description_inner').text.lstrip()



news_p



get_ipython().system('which chromedriver')



executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


url_splinter = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_splinter)


html = browser.html
soup_img = BeautifulSoup(html, 'html.parser')


featured_img_url = soup_img.find('div', class_ = 'img').img['src']

featured_img_url


url_table_scrape = 'https://space-facts.com/mars/'



tables = pd.read_html(url_table_scrape)


tables


df = tables[0]

df.columns = ['mars profile', 'data']


df.head()


mars_table = df.to_html()


hemisphere_img_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
]


mars_info = {"News Title": news_title,
            "News Article": news_p,
            "Img url": featured_img_url, 
            "Mars Table": mars_table,
            "Hemisphere Images": hemisphere_img_urls}


mars_info


def scrape():
    return mars_info




