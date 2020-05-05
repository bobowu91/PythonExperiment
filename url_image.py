import urllib.request as url
from selenium import webdriver

path = r'/Users/yibowang/Documents/Chromedriver/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(path, options=options)
# driver = webdriver.Chrome(path)

website = 'https://nhentai.net/g/310241/'
driver.get(website)

img = driver.find_elements_by_class_name('gallerythumb')

link = list()
for i in img[1:5]:
    link.append(i.get_attribute('href'))

print(link)

'''
for i in range(1, 10):
    link = '//*[@id="thumbnail-container"]/div['+str(i)+']/a/img'
    img = driver.find_element_by_xpath(link)
    src = img.get_attribute('data-src')

    filename = "/Users/yibowang/Desktop/data/" + str(i) + ".jpg"
    url.urlretrieve(src, filename)
'''
driver.close()
