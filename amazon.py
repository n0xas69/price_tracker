import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.fr:443/s/ref=nb_sb_noss_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=pc+portable"

payload = ""
headers = {
    "Cookie": "session-id=257-6070873-1901351; session-id-time=2082787201l; i18n-prefs=EUR; csm-hit=tb:V3H1SPWYPS92ZCQ9XYTG+s-V3H1SPWYPS92ZCQ9XYTG|1587854616506&t:1587854617287&adb:adblk_no; ubid-acbfr=261-8691254-3189707; x-wl-uid=1GWR8wuOWcjbP2rk45eEfcsRoSTZ/N/Je6VzR4W69qvZ35qoa15Wd7j3wL7szjOa4TmLS71UnVo4=; session-token=\"gBbDl3bGP0UA7yG+hNBtafTqTNuF+V5k2SLRo7O44Q/UBMtKZHMO4C5q5zQbMfd/BKI+QTOfRKpkgE3cKliaNhuoSW6zMQCZk9ZeXKAjX6iitrTU/oFnyT0RhG5MhxFPfEnm8cEQO2Fgl5Q5+oRi719s05rqhckh44VjH0Mf/a8b/HtOa/eHAhD1Tpevb8zOpdJBFt8Ja3Td+jBbr8tE9g7Wp/Pyo0qrzdIAwFu6MrbTTQMNVIhunxW5qasIePw0OMaQYw7BK80=\"", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0", 
    "Connection": "close", 
    "Referer": "https://www.amazon.fr/", 
    "Host": "www.amazon.fr", 
    "Accept-Encoding": "gzip, deflate", 
    "Upgrade-Insecure-Requests": "1", 
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.request("GET", url, data=payload, headers=headers)



soup = BeautifulSoup(response.text, "html.parser") # On créer un objet beautifulsoup avec le text html de request

for title in soup.findAll("span", {"class": "a-size-medium a-color-base a-text-normal"}):
    print(title)


test = "Bonjour Romain"
keklel = test.replace(" ", "+")
print(keklel)
