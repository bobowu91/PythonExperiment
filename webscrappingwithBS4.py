from bs4 import BeautifulSoup
import requests
import pandas as pd

aritzia = 'https://www.aritzia.com/en/sale'
reponse = requests.get(aritzia)
reponse_html = reponse.text
ar_soup = BeautifulSoup(reponse_html, "html.parser")

container = ar_soup.find_all('a', {"class": "button secondary"})
link = container[0].get('href')


intermediatePage = requests.get(link)
ip_html = intermediatePage.text
newsoup = BeautifulSoup(ip_html, "html.parser")
# print(newsoup.div.div.div.text)
link1 = newsoup.a.get('href')  # print(link1)

salespage = requests.get(link1)
salespage_html = salespage.text
salespage_all = BeautifulSoup(salespage_html, "html.parser")

brands = salespage_all.find_all('div',
                                {"class":
                                 "product-brand js-product-plp-brand mt2"})
brand = [b.text.strip() for b in brands]

products = salespage_all.find_all('div',
                                  {"class":
                                   "product-name js-product-plp-name"})
product = [p.text.strip() for p in products]

regular_p = salespage_all.find_all('span', {"class": "strike dib",
                                            "title": "Regular Price"})
regularprice = [r.text.strip() for r in regular_p]

discount_p = salespage_all.find_all('span',
                                    {"class": "js-product__sales-price red",
                                     "title": "Sale Price"})
discountprice = [d.text.strip() for d in discount_p]


combined = list(zip(brand, product, regularprice, discountprice))
aritzia_sales = pd.DataFrame(combined,
                             columns=['Brands', 'Products', 'Regualr Price',
                                      'Discount Price'])
aritzia_sales.to_csv("/Users/yibowang/Desktop/Aritzia.csv")
