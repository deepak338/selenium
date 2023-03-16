from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/deepak/Desktop/chrome driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# input the test
search = driver.find_element(by=By.NAME, value='search')
search.send_keys("Python")

# Submit the search query
search.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(10)



