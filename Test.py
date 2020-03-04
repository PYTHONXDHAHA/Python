from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
url = "https://youtube.com/"
driver.get(url)

sleep(5)

h1 = driver.find_element_by_xpath("//h1[@itemprop='name']").text
print(h1)