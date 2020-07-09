"""
javascript操作
"""
import time

from selenium import webdriver


def search_12306():
    driver = webdriver.Chrome("/home/axc/drivers/chromedriver")
    driver.implicitly_wait(10)
    driver.get("https://www.12306.cn/index/")
    # driver.maximize_window()
    from_element = driver.find_element_by_id("fromStationText")
    from_element.click()
    time.sleep(2)
    from_element.send_keys("北京")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='citem_2']").click()

    to_element = driver.find_element_by_css_selector("#toStationText")
    to_element.click()
    time.sleep(2)
    to_element.send_keys("天津")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='citem_1']").click()
    js = "$('input[id=train_date]').removeAttr('readonly')"
    driver.execute_script(js)
    date_element = driver.find_element_by_css_selector("#train_date")
    date_element.click()
    date_element.clear()
    date_element.send_keys("2020-7-9")
    time.sleep(2)
    driver.find_element_by_css_selector(".form-label").click()
    driver.find_element_by_css_selector("#search_one").click()
    time.sleep(20)


if __name__ == "__main__":
    search_12306()
