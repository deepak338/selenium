from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/deepak/Desktop/chrome driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.jotform.com/build/230702844927459")

# entering name to the form
first_name = driver.find_element(by=By.ID, value="first_10")
first_name.send_keys("Deepak")

last_name = driver.find_element(by=By.ID, value="last_10")
last_name.send_keys("Kumar")

email = driver.find_element(by=By.ID, value="input_11")
email.send_keys("devdixit111@gmail.com")

ph_area = driver.find_element(by=By.ID, value="input_12_area")
ph_area.send_keys("+91")

ph = driver.find_element(by=By.ID, value="input_12_phone")
ph.send_keys("9989142539")

info = driver.find_element(by=By.ID, value="input_6")
info.send_keys("first rule of fight clude is you do not talk about fight club")

submit = driver.find_element(by=By.ID, value="input_7")
submit.click()

driver.implicitly_wait(20)
