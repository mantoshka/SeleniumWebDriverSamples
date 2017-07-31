import os
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set the Chrome browser to fully maximized when launched
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--kiosk")

# launch the Chrome browser
driver = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'chromedriver'), chrome_options = chrome_options)

# navigate the browser to Google image search
driver.get("https://images.google.com")

# search for banana images
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys('banana', Keys.RETURN)

# create directory to save banana images
banana_img_dir = os.path.join(os.getcwd(), 'bananas')
if not os.path.exists(banana_img_dir):
	os.makedirs(banana_img_dir)

# get all the thumbnail images for banana search result and save it to "bananas" directory 
banana_imgsrc_list = driver.find_elements_by_xpath("//a/img[@alt='Image result for banana']")
for idx, val in enumerate(banana_imgsrc_list[:10]):
	urllib.urlretrieve(val.get_attribute('src'), os.path.join(banana_img_dir, "banana_{}.jpg".format(idx)))

# close the browser
driver.close()