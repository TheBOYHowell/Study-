# beauty_soup.py
from bs4 import BeautifulSoup
from urllib.request import urlopen
m=0
# https://www.tunisianet.com.tn/596-smartphone-mobile-4g-tunisie?page=j
for j in range(1,8):
    url = f'https://www.tunisianet.com.tn/596-smartphone-mobile-4g-tunisie?page={j}'
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    texts = soup.find_all("h2", {"class": "h3 product-title"})
    for text in texts:
         print(text.get_text())
         m=m+1
print("Nombre darticle",m)

#scrape from site all reference information 
