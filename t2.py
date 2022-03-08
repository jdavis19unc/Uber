from email.quoprimime import header_check
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import date, datetime
import pandas as pd

now = datetime.now()



op = webdriver.ChromeOptions()
op.add_argument("--start-maximized")

print(op)
ser = Service('C:\\Users\\Surface Laptop\\Desktop\\chromedriver.exe')


driver = webdriver.Chrome(service=ser, options = op)


driver.get("https://www.uber.com/global/en/price-estimate/")

time.sleep(3)

def enter(element: str, inp: str):
    x = driver.find_element_by_name(element)
    x.click()
    x.send_keys(inp)
    time.sleep(2)
    x.send_keys(Keys.RETURN)


pickup = "Chapel Hill, NC, USA"
enter("pickup", pickup)
y = driver.find_element_by_name("destination")
destination = "Governor's Drive, NC, USA"
enter("destination", destination)

time.sleep(5)
#z = driver.find_elements_by_class_name("text-area bv d9 bw fa bn bo v9 nh ru")

x = driver.find_element_by_xpath('//*[@id="main"]/section[2]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]')
#/html/body/div[1]/div/div/div[1]/main/section[2]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]
print("!!!!!!!!!!!!!!!!!!")
price = x.get_attribute("title")
print(price)
print("2")

# GET TIME
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")



#d = pd.read_csv("data.csv", index_col=False, header=0)
d = pd.DataFrame()
test = {"Price": price, "Cab_type": "UberX", "Pickup": pickup, "Destination": destination, "Time": current_time, "Date": d1 }
d = d.append(test, ignore_index=True)
d.to_csv('d2.csv', mode='a', header=False)

t = pd.read_csv("d2.csv")

print(t)