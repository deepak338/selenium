from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/deepak/Desktop/chrome driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get( "https://www.python.org/events/python-events/")

events_time = driver.find_elements(by=By.CSS_SELECTOR, value=".list-recent-events  time")
driver.implicitly_wait(10)



event_name=driver.find_elements(by=By.CSS_SELECTOR,value=".list-recent-events li a")

events={}

for n in range(len(events_time)):
    events[n]={
        "time":events_time[n],
        "name":event_name[n]

    }

print(events)


# Close the driver
driver.close()