"""
关于虚拟环境的几个常用命令：
- 创建虚拟环境：ｍkvirtualenv  虚拟环境名
- 退出虚拟环境：deactivate　虚拟环境名
- 进入虚拟环境：workon   虚拟环境名
- 删除虚拟环境：rmvirtualenv 虚拟环境名
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/axc/drivers/chromedriver")
driver.get("https://www.jd.com")
# search_element = driver.find_element_by_id("key")
# search_element.send_keys("电脑")
# search_element.send_keys(Keys.RETURN)
# driver.find_element_by_class_name("cate_menu_lk").click()
# driver.find_element_by_link_text("手机").click()
# driver.find_element_by_xpath("//*[@id=\"J_cate\"]/ul/li[4]/a[1]").click()

# time.sleep(3)
# driver.quit()

from selenium.webdriver.common.action_chains import ActionChains
# elem = driver.find_element_by_link_text("手机")
# ActionChains(driver).move_to_element(elem).perform()
# time.sleep(5)
# old_phone = driver.find_element_by_link_text("老人机")
# old_phone.click()

#截图方法
elem = driver.find_element_by_link_text("手机")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(5)
old_phone = driver.find_element_by_link_text("老人机")
old_phone.click()

#获取当前窗口的所有句柄
handles = driver.window_handles
#获取当前窗口的句柄
current_handle = driver.current_window_handle
for handle in handles:
    if handle != current_handle:
        driver.close()#关闭当前浏览器句柄
        driver.switch_to.window(handle)
        driver.save_screenshot("laorenji.png")