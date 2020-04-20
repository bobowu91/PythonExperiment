from bs4 import BeautifulSoup
import requests

aritzia = 'https://www.aritzia.com/en/sale'
reponse = requests.get(aritzia)
reponse_html = reponse.text
ar_soup = BeautifulSoup(reponse_html, "html.parser")

container = ar_soup.find_all('a', {"class": "button secondary"})
link = container[0].get('href')


intermediatePage = requests.get(link)
ip_html = intermediatePage.text
newsoup = BeautifulSoup(ip_html, "html.parser")

link1 = newsoup.a.get('href')
print(link1)

# print(newsoup.div.div.div.text)
# [0].get('href')
