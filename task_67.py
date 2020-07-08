"""
cookies操作：
- 先登录京东账户（login()）
- 然后保存登录后的cookies信息（save_cookies()）
- 利用获取的cookies进行绕过登录（get_url_with_cookies()）
"""
import json
import os
import time

from selenium import webdriver

driver = webdriver.Chrome("/home/axc/drivers/chromedriver")
driver.implicitly_wait(10)

# 登录京东账户获取登录后的cookies
def login():
    # 进入京东首页
    driver.get("https://www.jd.com")
    driver.maximize_window()
    # 点击用户登录
    driver.find_element_by_css_selector(".link-login").click()
    # 点击账户登录
    driver.find_element_by_link_text("账户登录").click()
    # 分别填入账户和密码
    driver.find_element_by_css_selector("#loginname").send_keys("18811073155")
    driver.find_element_by_css_selector("#nloginpwd").send_keys("axc632good")
    # 点击登录按钮就行验证登录
    driver.find_element_by_css_selector("#loginsubmit").click()
    # time.sleep(20)

    save_cookies(driver)


# 保存网页登录后的cookies
def save_cookies(driver):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    # print(file_path)
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    cookies = driver.get_cookies()
    with open(file_path + "jd.cookies", "w") as c:
        json.dump(cookies, c)
    print(cookies)


# 利用获取的cookies进行免登陆访问
def get_url_with_cookies():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    print(file_path)
    cookies_file = file_path + "jd.cookies"

    # 读取cookies信息
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    # 加载cookies信息，转成ｊｓｏｎ格式
    jd_cookies_dict = json.loads(jd_cookies_str)
    print(jd_cookies_dict)

    # 清除掉旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    # 将我们的cookies加入到driver中
    for cookie in jd_cookies_dict:
        print(cookie)
        driver.add_cookie(cookie)

    driver.get("https://order.jd.com/center/list.action")


if __name__ == "__main__":
    # login()
    get_url_with_cookies()