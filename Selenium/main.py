from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

cookie = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie.click()

