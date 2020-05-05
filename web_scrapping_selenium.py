from selenium import webdriver
from selenium.webdriver import ActionChains
import urllib.request as url
from selenium.webdriver.common.keys import Keys


path = r'/Users/yibowang/Documents/Chromedriver/chromedriver'

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome(path, options=options)
driver = webdriver.Chrome(path)

aritzia = 'https://www.aritzia.com/en/sale'
driver.get(aritzia)

driver.implicitly_wait(5)
# make sure the website is Canadian version
x = driver.find_element_by_xpath(
    '//*[@id="region-match-banner"]/div/div/a[2]')
x.click()

'''
brands = driver.find_elements_by_css_selector(
    '.product-brand.js-product-plp-brand.mt2')
for brand in brands:
    print(brand.text)

# items = driver.find_elements_by_xpath('//*[@id="search-result-items"]')
# for item in items:
#    print(item.text)

b = driver.find_elements_by_class_name("product-pricing")

for brand in b:
    regular_p = brand.text
    discount_p = brand.text



driver.execute_script("window.scrollBy(0,5000)", "")

loadmore = driver.find_element_by_xpath('//*[@id="primary"]/div/div[2]/div/a')
driver.execute_script("arguments[0].scrollIntoView()", loadmore)

driver.close()
.send_keys(Keys.ARROW_DOWN).send_keys(
    Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
    Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
    Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)

'''
driver.execute_script("window.scrollBy(0,600)", "")

img = driver.find_element_by_xpath(
    '//*[@id="c3c1c5de207f13ccf5e7c47f64"]/div[1]/a[1]/img')


action = ActionChains(driver)
action.context_click(img).send_keys(
    Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
    Keys.RETURN).perform()

# driver.close()
