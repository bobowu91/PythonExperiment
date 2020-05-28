from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import login  # a python file that contains my login information
import time

# reponse = requests.get(hbr)
# reponse_html = reponse.text

path = r'/Users/yibowang/Documents/Chromedriver/chromedriver'
hbr = ('https://www.lib.uwo.ca/cgi-bin/ezpauthn.cgi?url='
       'http://search.ebscohost.com/direct.asp?db=bth&jid=HBR&scope=site')
username = login.username
password = login.password

# Initiate a web browser and go to the url in the browser
options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(path, options=options)
driver.get(hbr)

# log in to the website to create one session
user = driver.find_element_by_name('user')
user.send_keys(username)
pin = driver.find_element_by_name('pass')
pin.send_keys(password)
login_button = driver.find_element_by_xpath(
    '/html/body/center[2]/div/form/p[4]/input')
login_button.click()

# Land in a new page and locate the 'All issues' table
issue = driver.maximize_window()
time.sleep(3)  # this is crucial for the web browser to load and react

issues = driver.find_elements_by_class_name("authVolIssue_volume_cell")
issue = driver.find_element_by_xpath('//*[@id="VolumeTable"]/tbody/tr[1]/td/a')
issue.click()
time.sleep(3)

# locate the most recent volume in the issue
vol = driver.find_element_by_link_text("Vol. 98 Issue 3 - May/Jun2020")
vol.click()
time.sleep(3)

hbrlist = []
hbr_article_link = driver.find_elements_by_link_text('HTML Full Text')
for i, item in enumerate(hbr_article_link):
    time.sleep(3)
    hbr_article_link = driver.find_elements_by_link_text('HTML Full Text')
    hbr_article_link[i].click()
    time.sleep(3)
    article_html = driver.page_source
    article = BeautifulSoup(article_html, "html.parser")
    hbr_article_text = article.find_all("p", {'class': "body-paragraph"})
    hbrlist.append(hbr_article_text)
    driver.execute_script("window.history.go(-1)")  # Return to the previous
