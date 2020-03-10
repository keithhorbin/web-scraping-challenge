import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

mars_data = {}
def mars_news_scrape():
    browser = init_browser()
    # visit the NASA Mars News site and scrape headlines
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'lxml')
    title_text = soup.find('div', class_='list_text').find('a').text
    mars_data['title_text'] = title_text
    # Extract Paragraph text
    para_text = soup.find('div', class_='article_teaser_body').text
    mars_data['para_text'] = para_text

    return mars_data

def img_scrape():
    browser = init_browser()
    #Visit Nasa's JPL Mars Space url  using splinter module
    jpl_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    #create HTML object
    html = browser.html
    jplsoup = bs(html, 'lxml')

    #get base Nasa link
    main_url ='https://www.jpl.nasa.gov'
    #get image url from the soup object.
    featured_image_url = jplsoup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    #Create one full image url link
    full_image_url=main_url+featured_image_url
    mars_data['full_image_url']= full_image_url
    print(full_image_url )

    return mars_data

def mars_weather():
    browser = init_browser()
    # visit the mars weather report twitter and scrape the latest tweet
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(tweet_url)
    tweetsoup = bs(response.text, 'lxml')

    tweet_list = tweetsoup.find_all('div', class_='js-tweet-text-container')
    for tweet in tweet_list: 
        tweet_weather = tweet.find('p').text     
        if 'ºF' and 'ºC' in tweet_weather:
            mars_weather = tweet_weather
            break
        else: 
            pass
    mars_data["weather_summary"] = mars_weather
    return mars_data

def mars_facts():
    # visit space facts and scrap the mars facts table
    facts_url = 'https://space-facts.com/mars/'
    table = pd.read_html(facts_url)
    mars_df = table[0]
    mars_df.columns = ['Fact','Value']
    mars_facts_html = mars_df.to_html(header=False, index=False)
    mars_data["mars_facts"] = mars_facts_html
    return mars_data

def mars_hem():
    browser = init_browser()
    # scrape images of Mars' hemispheres from the USGS site
    hemi_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    short_url="https://astrogeology.usgs.gov"

    browser.visit(hemi_url)
    html = browser.html
    hemisoup = bs(html, 'lxml')
    main_url = hemisoup.find_all('div', class_='item')
         
    hemisphere_img_urls=[]      
    for x in main_url:
        title = x.find('h3').text
        url = x.find('a')['href']
        hem_img_url= short_url+url
        #print(hem_img_url)
        browser.visit(hem_img_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        hemisphere_img_original= soup.find('div',class_='downloads')
        hemisphere_img_url=hemisphere_img_original.find('a')['href']
              
        print(hemisphere_img_url)
        img_data=dict({'title':title, 'img_url':hemisphere_img_url})
        hemisphere_img_urls.append(img_data)
    mars_data['hemisphere_img_urls']=hemisphere_img_urls
    return mars_data