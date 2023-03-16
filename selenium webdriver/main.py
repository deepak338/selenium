from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the Chrome driver executable
chrome_driver_path = "C:/Users/deepak/Desktop/chrome driver/chromedriver.exe"

# Create a new Chrome driver instance
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to Amazon.com
driver.get("https://www.python.org/")
# finding element by class name By.CLASS_NAME
#finding element by id name By.ID
#finding element by name is By.NAME
#finding element by css selector is By.CSS_SELECTOR
#find element by xpath is By.XPATH

price = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# Wait for the page to load
driver.implicitly_wait(10)

# Print the title of the page
print(price.text)
# Close the driver
driver.close()
