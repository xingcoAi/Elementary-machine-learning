"""
该工程为仿照task_71打印出京东商城中箱包->双肩包中销量最高双肩包的商品介绍信息
"""
import time

from selenium import webdriver
import os

from selenium.webdriver import ActionChains


def get_bag_infos():
    driver = webdriver.Chrome("/home/axc/drivers/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.jd.com")
    luggage_element = driver.find_element_by_link_text("箱包")
    ActionChains(driver).move_to_element(luggage_element).perform()
    driver.find_element_by_link_text("双肩包").click()
    time.sleep(3)
    # 切换句柄
    handles = driver.window_handles
    # 获取首页句柄，以备以后切回首页
    index_handle = driver.current_window_handle
    # 切到双肩包页面
    driver.switch_to.window(handles[1])
    # 点击稻草人品牌
    driver.find_element_by_xpath('//*[@id="brand-5923"]/a').click()
    # 点击销量
    # driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()
    driver.find_element_by_link_text("销量").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
    # 　切换句柄
    bag_handle = driver.current_window_handle
    new_handles = driver.window_handles
    for handle in new_handles:
        if handle != index_handle and handle != bag_handle:
            driver.switch_to.window(handle)

    # 滚动屏幕
    js = "window.scrollTo(0,1000)"
    driver.execute_script(js)
    # 　点击商品介绍
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[1]').click()
    all_infos = driver.find_elements_by_css_selector(".p-parameter>ul>li")  # 获取１８个元素
    result_list = []

    for elements in all_infos:
        result_list.append(elements.text)

    save_infos(result_list)


def save_infos(result_list):
    project_path = os.path.abspath(os.path.curdir)
    print("project_path：" + project_path)
    with open(project_path + "bag_info", 'a', encoding='utf-8') as f:
        f.write(str(result_list))

    print(str(result_list))


if __name__ == "__main__":
    get_bag_infos()
