import requests, re
from bs4 import BeautifulSoup



data  =requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok").text
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("div", {"class":"product-card__title"})
title = span.text
span = soup.find("div", {"class":"product-card__product-count font-override__body1"})
colors = span.text
span = soup.find("div", {"class":"product-price is--current-price css-1ydfahe"})
price = span.text
print("Item %s has %s and price of %s" % (title, colors, price))