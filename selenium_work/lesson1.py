from selenium import webdriver
from selenium.webdriver.common.keys import Keys



if __name__ == '__main__':
    driver = webdriver.Chrome("C:\\Program Files\\chromedriver.exe")
    driver.get("https://www.baidu.com/")
    # print(driver.title)
    # assert "百度一下，你就知道" == driver.title
    # elem = driver.find_element_by_name('referrer')
    # input = driver.find_element_by_id("kw")
    # input.send_keys("今天星期几")
    # # elem = driver.find_element_by_class_name('bg s_btn')//*[@id="su"]
    # elem = driver.find_element_by_id('dsadasdssu')
    # t1 = elem.click()
    # driver.close()
    # driver.quit()

    # input = driver.find_element_by_id("kw")
    # input = driver.find_element_by_name("wd")
    # input = driver.find_element_by_xpath("//input[@id='kw']")

    input = driver.find_element_by_id("kw")
    input.send_keys("今天星期几")
    input.clear()
    input.send_keys("and some",Keys.ARROW_DOWN)
    input.send_keys(Keys.RETURN)
    print(driver.page_source)

    driver.forward()
    driver.back()

    cookie = {"cookie":"123456"}
    driver.add_cookie(cookie)
    driver.get_cookies()
    driver.switch_to.window()
    driver.switch_to.alert()
    list