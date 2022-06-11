from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://music.com/story/search")
search= driver.find_element_by_name("search-input")
search.send_keys("test")
search.send_keys(Keys.RETURN)
print(driver.page_source)
time.sleep(5)
driver.close()