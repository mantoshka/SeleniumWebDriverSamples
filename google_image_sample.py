import os
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'chromedriver'), chrome_options = chrome_options)
driver.get("https://images.google.com")

driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys('banana', Keys.RETURN)

banana_img_dir = os.path.join(os.getcwd(), 'bananas')
if not os.path.exists(banana_img_dir):
	os.makedirs(banana_img_dir)

banana_imgsrc_list = driver.find_elements_by_xpath("//a/img[@alt='Image result for banana']")
for idx, val in enumerate(banana_imgsrc_list[:10]):
	urllib.urlretrieve(val.get_attribute('src'), os.path.join(banana_img_dir, "banana_{}.jpg".format(idx)))

driver.close()