# working with gmail.com
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
input_id = 'identifierId'

# opening the browser
browser = webdriver.Firefox()
browser.get('https://gmail.com')

# getting ussername
user_field = browser.find_element(By.ID, 'identifierId')
user_field.send_keys('novikova.novikovadasha2016@gmail.com')

# next button
next_btn = browser.find_element(
    By. XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
next_btn.click()

# password_field = browser.find_element(
#     By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/div')

# password_field.send_keys('24465336Kotiki')
# next_btn.click()
# # time.sleep(2)
