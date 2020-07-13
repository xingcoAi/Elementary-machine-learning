# 等待
from selenium import webdriver

driver = webdriver.Chrome("/home/axc/drivers/chromedriver")
# 隐形等待。最大等待时间位10秒
# driver.implicitly_wait(10)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver.get("https://list.jd.com/list.html?cat=670,671,672")
# 首先声明等待条件
locator = (By.CSS_SELECTOR, "#J_goodsList > ul > li:nth-child(1) > div > div.p-img > a > img")
element = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located(locator))
element.click()
