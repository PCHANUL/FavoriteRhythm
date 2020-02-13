import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup



chrome_driver = '/Users/bagchan-ul/Documents/chromedriver'
driver = webdriver.Chrome(chrome_driver)


home_url = 'https://www.music-flo.com/'
driver.get(home_url)

# Login 버튼누르기
#header > div > div > ul > li:nth-child(2) > a
login_btn = driver.find_element_by_css_selector('#header > div > div > ul > li:nth-child(2) > a')
login_btn.click()

# # 네이버 로그인
# #naverIdLogin_loginButton
# naver_btn = driver.find_element_by_css_selector('a #naverIdLogin_loginButton')
# naver_btn.click()



driver.implicitly_wait(3)
# 로그인
id = 'cksdnfwkd'
pwd = 'qkr95162'

id_tag = driver.find_element_by_css_selector('#emailId')
pwd_tag = driver.find_element_by_css_selector('#password')
id_tag.send_keys(id)
pwd_tag.send_keys(pwd)
# drop down option select
select = Select(driver.find_element_by_name('emailUrl'))
select.select_by_visible_text('naver.com')
# select.select_by_value()
#btnSubmitSignin
driver.find_element_by_css_selector('#btnSubmitSignin').click()


driver.implicitly_wait(2)
sample = driver.find_element_by_css_selector('#header > div > nav > ul > li:nth-child(2) > a')
sample.send_keys('\n')




# driver.get('https://www.music-flo.com/storage')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# mylist = soup.select('#main > div > div.section_content_wrap > ul > li:nth-child(2) > div > div.badge_track_info > div.info_area > p > a')
# print(mylist)




# time.sleep(3)
# driver.close()