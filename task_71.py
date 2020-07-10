"""
京东商品信息保存:
- 进入京东商城
- 进入笔记本商品页面，并选择ThinkPad品牌
- 点击评论数，选择第一款电脑
- 将该款电脑的规格与包装信息打印出来
"""

import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


def to_goods_page():
    driver = webdriver.Chrome("/home/axc/drivers/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.jd.com")
    # 转到电脑商品页面
    computer_element = driver.find_element_by_link_text("电脑")
    ActionChains(driver).move_to_element(computer_element).perform()
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()
    # 切换句柄,切换到笔记本页面
    handles = driver.window_handles
    # 首页句柄
    index_handle = driver.current_window_handle
    # 切换句柄的两种写法
    # 第一种利用循环来判断
    for handle in handles:
        if handle != index_handle:
            # 如果当前句柄不等于主页句柄就直接切换
            driver.switch_to.window(handle)
    # 第二中直接调用handles列表中的最后一个handle值
    # driver.switch_to.window(handles[1])
    # 点击thinkpad
    driver.find_element_by_xpath('//*[@id="brand-11518"]/a').click()
    # 点击评论数
    driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[3]').click()
    time.sleep(3)
    # 选择第一款电脑
    driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
    # 切换句柄，切换到thinkpad的第一款商品详情页面
    notebook_handle = driver.current_window_handle
    # 重新获取所有句柄
    handles = driver.window_handles
    for handle in handles:
        # 如果不等于首页句柄和上次切换到笔记本页面的句柄就直接切换
        if handle != index_handle and handle != notebook_handle:
            driver.switch_to.window(handle)
    # driver.switch_to.window(handles[2])
    # 利用js滚动滚动条，第一个参数为左右坐标，第二个参数为上下坐标
    js = "window.scrollTo(0,1000)"
    driver.execute_script(js)
    # 点击规格与包装
    driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[2]').click()
    # 定位表格中的所有数据
    info_elements = driver.find_elements_by_class_name('Ptable-item')
    # info_elements获取了所有标签为div类为Ptable-item的13个元素组成的列表
    # 声明一个变量，用来装所有数据
    result_list = []

    for info_element in info_elements:
        # 解析商品信息数据，获取一个字典格式的数据
        # 一个info_element即为一个class=Ptable-item的div主体
        info_element_dic = get_info_element_dict(info_element)
        result_list.append(info_element_dic)

    # 将信息保存到文件中
    save_goods_info(result_list)


def get_info_element_dict(info_element):
    # 计算机的组成信息，第一列信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机的key，第二列信息，就是dt标签的信息
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # value，第三列信息,不获取问号信息
    computer_info_value = info_element.find_elements_by_xpath('dl//dd[not(contains(@class,"Ptable-tips"))]')
    # 声明一个变量，用来保存计算机信息的key和value
    key_and_value_dict = {}
    # 声明一个空字典，保存计算机组成信息
    parts_dict = {}
    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_value[i].text

    parts_dict[computer_part.text] = key_and_value_dict
    return parts_dict


def save_goods_info(result_list):
    project_path = os.path.abspath(os.path.curdir)
    print("project_path:" + project_path)
    file_path = project_path + "/goods_infos/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open(file_path + "computer_infos", 'a', encoding="utf-8") as f:
        f.write(str(result_list))
        print(str(result_list))


if __name__ == "__main__":
    to_goods_page()
