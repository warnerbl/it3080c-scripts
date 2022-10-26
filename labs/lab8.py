import requests, re 
from bs4 import BeautifulSoup

data = requests.get("https://www.nike.com/t/usmnt-2022-23-stadium-home-mens-dri-fit-soccer-jersey-PVB4r8/DN0706-101").text
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1",{"class": "headline-2 css-16cqcdq"}  )
jersey = span.text
span = soup.find("div", {"class" : "product-price css-11s12ax is--current-price css-tpaepq"})
price = span.text


print("Item %s has price %s", (jersey,price))