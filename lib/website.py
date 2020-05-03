import requests
import os
import json
import random
from bs4 import BeautifulSoup

class Amazon:
    def __init__(self, product):
        self.product = product

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
            content = soup.findAll("span", {"class" : "a-size-medium a-color-base a-text-normal"})
            if content == []:
                retry += 1
            else:
                for t in content:
                    print(t.getText())
                break

    