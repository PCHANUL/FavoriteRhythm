import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup



chrome_driver = '/Users/bagchan-ul/Documents/chromedriver'
driver = webdriver.Chrome(chrome_driver)


home_url = 'https://www.music-flo.com/storage'
driver.get(home_url)


driver.implicitly_wait(5)
# Login 버튼누르기
#header > div > div > ul > li:nth-child(2) > a


sample = driver.find_element_by_css_selector('#main > div > div.full-msg > div > div > a')
sample.send_keys('\n')


# login_btn = driver.find_element_by_css_selector('#main > div > div.full-msg > div > div > a')
# login_btn.click()

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
driver.find_element_by_css_selector('#btnSubmitSignin').click()
driver.find_element_by_css_selector('#main > div > div.tab.storage_tab > div > ul > li:nth-child(2) > button.btn_tab_normal').click()


print(driver)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

mylist = soup.select_one('#main > div > div.ct_chart > div.chart_lst > table > tbody > tr:nth-child(1) > td.info > div > div.txt_area > button > p > strong').text
# print(mylist)




# time.sleep(3)
# driver.close()