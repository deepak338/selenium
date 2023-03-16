from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/deepak/Desktop/chrome driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

cookie_cliker = driver.find_element(by=By.ID, value="cookie")

time = 0
while True:
    time=0
    click=0
    cookie_cliker.click()
    click=click+1
    if time >5:
        store=driver.find_element(by=By.ID,value="store")
