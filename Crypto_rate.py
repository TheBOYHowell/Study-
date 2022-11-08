
# beauty_soup.py
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
url ='https://www.google.com/finance/markets/cryptocurrencies' 
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
texts1 = soup.find_all("div",{"class": "iLEcy"},)
texts2 = soup.find_all("div", {"class": "Bu4oXd"})          
texts3 = soup.find_all("span", {"class": "P2Luy Ebnabc"})
texts4 = soup.find_all("div", {"class": "JwB6zf"})
l =[]
k=[]
o=[]
z=[]
for i in texts1:
    l.append(i.get_text())
for j in texts2:
    k.append(j.get_text())
for p in texts3:
    o.append(p.get_text())
for q in texts4:
    z.append(q.get_text())

list_of_tuples1 = list(zip(l, k,o,z))


for i in list_of_tuples1:
    print(i[0] , i[1] , i[2] , i[3])

#for text1 in texts1:                                             #while text1 in texts1 and text2 in texts2:
#    parse1=str(text1.get_text())             #for i in range(0, len(parse1)):                                                                    
#for text2 in texts1:                                                #array=parse1[i]
#    parse2=str(text2.get_text())
#    print((parse1.replace('add_circle_outline',''))  + (parse2.replace('add_circle_outline','')))

#scrape cryto rate 
#with open("world_population_by_region.csv", "wt",newline='',encoding='utf-8') as csv_file:
    #csv_writer = writer(csv_file, delimiter ='|')
    #csv_writer.writerow(header) # write header
    # Write data to csv file
    #for row in tabl.find_all('tr')[1:]:
        #td = row.find_all('td')
        #r = [i.text.replace('\n','') for i in td]
        #csv_writer.writerow(r)


with open('file4.csv','w') as f:
    for row in list_of_tuples1:
        for x in row:
            f.write(str(x) + '   ')
        f.write('\n')
