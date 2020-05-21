# web scraping example

# Packages imported for web scraping
# Had to install them all for the project
# also had to upgrade pip

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# Configuring selenium webdriver to use the Chrome Browser
# There are similar commands for other browsers if you wish to use IE, Firefox, Safari, etc.
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


# selenium will open a browser for us to the URL we provide (the newegg url for laptops)
#
products=[] #List to store name of the product
prices=[] #List to store price of the product

driver.get("<a href="https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptops")


# Data to scrape
    # Item Name and Price
    # Used Right Click + Inspect to find the tags of the fields to scrape

