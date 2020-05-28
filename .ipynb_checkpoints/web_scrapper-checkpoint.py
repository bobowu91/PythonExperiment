from bs4 import BeautifulSoup
import requests
import pandas as pd

aritzia = 'https://www.aritzia.com/en/sale'
reponse = requests.get(aritzia)
reponse_html = reponse.text
ar_soup = BeautifulSoup(reponse_html, "html.parser")
#  print(ar_soup)

#  sales = ar_soup.prettify()
#  print(sales)

#  alink = ar_soup.find_all('a')  # find all link attributes
#  print(alink)

#  aparagraph = ar_soup.find_all('p')  # find all aparagraph attributes
#  print(aparagraph)

#  adiv = ar_soup.find_all('div', {"class": "search-result-content"})
#  print(adiv)


# ali = ar_soup.find_all('ul', {"class": "search-result-items tiles-container",
#                              "id": "search-result-items"})[0]
# print(type(ali))

totalitem = ar_soup.find('div', {"id": "pagebar-total-value"})
itemsPerpage = ar_soup.find('div', {"id": "pagebar-end-value"})
print(totalitem.text)
print(itemsPerpage.text)

brand = ar_soup.find_all('div',
                         {"class": "product-brand js-product-plp-brand mt2"})
producName = ar_soup.find_all('div',
                              {"class": "product-name js-product-plp-name"})
price = ar_soup.find_all('div', {"class": "product-pricing"})
regular_p = ar_soup.find_all('span', {"class": "strike dib",
                                      "title": "Regular Price"})

discount_p = ar_soup.find_all('span', {"class": "js-product__sales-price red",
                                       "title": "Sale Price"})

print(len(brand))
print(len(producName))
print(len(price))

brands = [b.text.strip() for b in brand]
products = [p.text.strip() for p in producName]
regular_price = [i.text.strip() for i in regular_p]
discount_price = [i.text.strip() for i in discount_p]

# print(len(regular_price))
# print(len(discount_price))
#
# print(regular_price)
# print(discount_price)
# print(brands)
# print(products)

combined = list(zip(brands, products, regular_price, discount_price))
aritzia_sales = pd.DataFrame(
    combined, columns=["Brand", "Product", "Regular Price", "Discount Price"])
