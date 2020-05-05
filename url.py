import urllib.request as url

src = 'https://i.nhentai.net/galleries/1620988/17.jpg'
print(src)
url.urlretrieve(src, "/Users/yibowang/Desktop/data/captcha.png")
