# beauty_soup.py
from bs4 import BeautifulSoup
from urllib.request import urlopen
url ='https://www.google.com/finance/markets/cryptocurrencies'
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
texts1 = soup.find_all("li", {"": ""},)
texts2 = soup.find_all("div", {"class": "SxcTic"})
for text1 in texts1:                                             #while text1 in texts1 and text2 in texts2:
    parse1=str(text1.get_text())
    print(parse1.replace('add_circle_outline',''))                  #for i in range(0, len(parse1)):                                                                    
for text2 in texts2:                                                #array=parse1[i]
    parse2=str(text2.get_text())
    print(parse2.replace('add_circle_outline',''))

#scrape cryto rate 
#with open("world_population_by_region.csv", "wt",newline='',encoding='utf-8') as csv_file:
    #csv_writer = writer(csv_file, delimiter ='|')
    #csv_writer.writerow(header) # write header
    # Write data to csv file
    #for row in tabl.find_all('tr')[1:]:
        #td = row.find_all('td')
        #r = [i.text.replace('\n','') for i in td]
        #csv_writer.writerow(r