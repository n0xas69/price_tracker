import requests
import os
import json
import random
import time
from bs4 import BeautifulSoup

class Amazon:
    def __init__(self, product):
        self.product = product
        self.price = []
        self.duplicate = []

    def sendRequest(self):
        headers = json.load(open(os.getcwd()+r"\lib\user_agent.json", "r"))
        header = {"User-agent" : random.choice(headers)}
        url = "https://www.amazon.fr:443/s/ref=nb_sb_noss_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords="+self.product.replace(" ", "+")
        response = requests.request("GET", url, headers=header)
        return response

    def searchProduct(self):
        retry = 0 # permet de faire 10 tentatives de scrapping
        while retry < 10:
            soup = BeautifulSoup(self.sendRequest().text, "html.parser")

            contentDiv = soup.find_all("div", {"class" :  "sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"})
            for div in contentDiv:
                contentName = div.find("span", {"class" : "a-size-medium a-color-base a-text-normal"})
                contentPrice = div.find("span", {"class" : "a-price-whole"})
                contentURL = div.a["href"]
                try:
                    name = contentName.getText().replace(u"\xa0", u" ")
                    price = contentPrice.getText().replace(u"\xa0", u" ")
                    price = price.replace(" ", "")
                    price = price.replace(",", ".")
                    URL = contentURL
                except:
                    pass
                
                self.duplicate.append(price)
                if self.duplicate.count(price) >= 2:
                    pass
                else:
                     # On vérifie si c'est pas une pub amazon
                    if not "advertising.amazon.fr" in URL:
                        self.price.append({"Nom" : name, "Prix" : float(price), "URL" : "https://www.amazon.fr"+URL})

            
            if contentDiv == []:
                retry += 1
                print("failed")

        self.price.sort(key=lambda x: x["Prix"])    
        return self.price

    