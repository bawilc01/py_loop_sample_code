# web scraping example

# Packages imported for web scraping
# Had to install them all for the project
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd


URLtoScrape = "https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptops"

# Data to scrape
    # Item Name and Price
    # Used Right Click + Inspect to find the tags of the fields to scrape

