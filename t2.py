from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

op = webdriver.ChromeOptions()
op.add_argument("--start-maximized")

print(op)
ser = Service('C:\\Users\\Surface Laptop\\Desktop\\chromedriver.exe')


driver = webdriver.Chrome(service=ser, options = op)


driver.get("https://www.uber.com/global/en/price-estimate/")

def enter(element: str, inp: str):
    x = driver.find_element_by_name(element)
    x.click()
    x.send_keys(inp)
    time.sleep(2)
    x.send_keys(Keys.RETURN)

enter("pickup", "Chapel Hill, NC, USA")
y = driver.find_element_by_name("destination")

enter("destination", "Governor's Drive, NC, USA")

time.sleep(5)
#z = driver.find_elements_by_class_name("text-area bv d9 bw fa bn bo v9 nh ru")

x = driver.find_element_by_xpath('//*[@id="main"]/section[2]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]')
#/html/body/div[1]/div/div/div[1]/main/section[2]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]
print("!!!!!!!!!!!!!!!!!!")
print(x.get_attribute("title"))
print("2")

Cov = pd.read_csv("data.csv", 
                  sep='\t', 
                  header=None)
Cov.columns = ["Sequence", "Start", "End", "Coverage"]
