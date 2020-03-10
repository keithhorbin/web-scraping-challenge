# Mission to Mars

In this project the intent was to build a landing page that upon the end users request would scrape useful data regarding Mars from five different sources. Those sources scraped are as follows:

### NASA Mars News, to grab the latest headline and exerpt
### JPL Mars Space Images, to grab a featured image
### Mars Weather, to grab the most recent temperature readings
### Mars Facts, random facts and figures about Mars
### Mars Hemispheres, for images and names of the Mars hemispheres

## Files Included:
### chromedriver which is neccessary for scraping the activites above.
### mission_to_mars Jupyter Notebook containing code for all scraping activites above. 
### scrape_mars.py which is a conversion on the Jupyter notebook into a Python script which will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.
### app.py file which runs flask, calls the index and pulls in the scrape_mars.py file.
### a folder called templates which houses the index.html template for the landing page. 
### a screen shot of the output of a successful scrape.