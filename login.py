# import module
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select


# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.

s = Service(r"C:\Users\bnguyen\Documents\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)

#driver = webdriver.Chrome(r"C:\Users\Ben\Documents\drivers\chromedriver.exe")
# get https://www.geeksforgeeks.org/

driver.get("https://clock.payrollservers.us/?wl=payrollhrpros.payrollservers.us#/clock/web/login")

# Maximize the window and let code stall
# for 10s to properly maximise the window.

driver.maximize_window()
time.sleep(10)

# Obtain button by link text and click.
#button = driver.find_element_by_link_text('Sign In')
#element = driver.find_element(By.NAME, "element_name")
driver.find_element(By.ID, "Username").send_keys("bnguyen")
driver.find_element(By.ID, "Password").send_keys("Katco12306")

ID_button = driver.find_element(By.ID, "Login")
ID_button.click()



#driver.get("https://clock.payrollservers.us/?wl=payrollhrpros.payrollservers.us#/clock/web")
#WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='buttonStyle']//input[@id='ClockIn']")));

#//*[@id='ClockIn']
#//*[@id="PromptForm"]/fieldset[1]/div/div/input


clockin = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='ClockIn']")))

clockin.click()

driver.find_element_by_xpath("//*[@id='PromptForm']/fieldset[1]/div/div/input").click()
driver.find_element_by_xpath("//*[@id='PromptForm']/fieldset[1]/div/div/ul/li[2]").click()

driver.find_element_by_xpath("//*[@id='PromptForm']/fieldset[2]/div/div").click()
driver.find_element_by_xpath("//*[@id='PromptForm']/fieldset[2]/div/div/ul/li[3]").click()

driver.find_element_by_xpath("//*[@id='FinishPunch']").click()

#select = Select(driver.find_element(By.XPATH, "//*[@id='PromptForm']/fieldset[1]/div/div/input"))
#select.get_element_by_name('HIT Division-15')
#driver.find_element(By.XPATH, "//*[@id='ClockIn']").click()
#IN_button.click()

#//*[@id="PromptForm"]/fieldset[1]/div/div/ul/li[2]

#//*[@id="PromptForm"]/fieldset[2]/div/div

#//*[@id="PromptForm"]/fieldset[2]/div/div/ul/li[3]

#//*[@id="FinishPunch"]