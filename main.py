import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
massive = []
for i in range(0,38):
	if i == 1:
		i = ""
	url = 'https://anekdotovstreet.com/nacionalnosti/evrei/'+str(i)+"/"
	response = requests.get(url,  headers={'User-Agent': UserAgent().chrome})
	soup = BeautifulSoup(response.content, 'lxml')
	quotes = soup.find_all('p')
	for anek in quotes:
		if "span" in str(anek) or "Все анекдоты вымышлены." in str(anek):
			pass
		else:
			massive.append(str(anek).replace("<p>","").replace("</p>","").replace("<br/>",""))
anektod = random.choice(massive)
print(anektod)
