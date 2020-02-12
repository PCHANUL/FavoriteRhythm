import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

chrome_driver = '/Users/bagchan-ul/Documents/chromedriver'
driver = webdriver.Chrome(chrome_driver)


home_url = 'https://www.genie.co.kr/'
driver.get(home_url)

# 로그인버튼 누르기
album_btn = driver.find_element_by_css_selector('#gnb > div > div > button')
album_btn.click()
album_btn = driver.find_element_by_css_selector('#gnb > div > div > div > div > a')
album_btn.click()

# 새창
driver.switch_to_window(driver.window_handles[1])

# 지니뮤직 로그인
id = driver.find_element_by_name('gnb_uxd')
pwd = driver.find_element_by_name('gnb_uxx')
id.send_keys('ehfrkadhr')
pwd.send_keys('qkr95162')
button = driver.find_element_by_css_selector('#f_login_layer > input.btn-submit')
button.click()

driver.switch_to_window(driver.window_handles[0])


# search = driver.find_element_by_css_selector('#sc-fd.ipt-search placeholder')
# search.send_keys('아이유')
# search.send_keys(Keys.RETURN)

player_btn = driver.find_element_by_css_selector('#gnb > div > div.toggle-button-box.select-button > button')
player_btn.click()



player_btn = driver.find_element_by_css_selector('#wrap-head > div.hd-top.clearfix > div.payment-wrap.player-wrap > a.web_player')
player_btn.click()
time.sleep(2)

driver.switch_to_window(driver.window_handles[1])
mysong_btn = driver.find_element_by_css_selector('#content > div.clearfix > button.btn-tab.btn-my-music')
mysong_btn.click()

src = driver.page_source
soup = BeautifulSoup(src)

print(soup)


# driver.close()

list = soup.select_one('#tabMyListWrap > div > div > ul > li:nth-child(1) > a.btn-detail > strong.title.ellipsis')
print(list)


