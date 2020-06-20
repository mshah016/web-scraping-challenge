#!/usr/bin/env python
# coding: utf-8




import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser 
from selenium import webdriver


# News Title
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup.prettify())
results = soup.find_all('div', class_='content_title')

titles = []
for result in results:
    title = result.a.text
#     print(title)
    titles.append(title)
    
latest_title = titles[0]
print(latest_title)








# News Summary
results = soup.find_all('div', class_="rollover_description_inner")

news_p = []
for result in results:
    p = result.text
#     print(p)
    news_p.append(p)
    
latest_news_p = news_p[0]
print(latest_news_p)  











# Featured Image
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser = Browser('chrome')
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')

carousel_items = soup.find_all('div', class_='carousel_items')
for item in carousel_items:
    a_tag = item.find('a')
    href = a_tag['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov/' + href

print(featured_image_url)














# Mars Weather
weather_url = "https://twitter.com/marswxreport?lang=en"
browser = Browser('chrome')
browser.visit(weather_url)
html = browser.html
soup = bs(html, 'html.parser')

posts = soup.find_all('div', class_='css-1dbjc4n')[0]
print(posts.prettify())

latest_post = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").text
latest_post














# Mars Facts
facts_url = "https://space-facts.com/mars/"
browser = Browser('chrome')
browser.visit(facts_url)
html = browser.html
soup = bs(html, 'html.parser')

facts = soup.find('table')
print(facts.prettify())

table = pd.read_html(facts_url)
# table

facts_df = table[0]
facts_df.columns = [' ', 'Data']
# facts_df

facts_table = facts_df.to_html()
facts_table















# Mars Hemispheres
def hemispheres():
    astropedia_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser= Browser('chrome')
    browser.visit(astropedia_url)
    links = browser.find_by_css("a.product-item h3")
    hemisphere_urls = []
    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[i].click()
        sample = browser.find_link_by_text('Sample').first
        hemisphere['title'] = browser.find_by_css('h2.title').text
        hemisphere['image_url'] = sample['href']
    #     title = browser.find_by_css('h2.title').text
    #     hemisphere[title] = original['href']
        hemisphere_urls.append(hemisphere)
        browser.back()
    return hemisphere_urls















# Load Data
def scrape():
    information = {}

    information['title'] = latest_title
    information['summary'] = latest_news_p
    information['image'] = featured_image_url
    information['post'] = latest_post
    information['facts'] = facts_table
    information['hemispheres'] = hemispheres()

    return information

        

