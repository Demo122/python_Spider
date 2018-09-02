#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/24 17:59
"""

# Selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作，
# 同时还可以获取浏览器当前呈现的页面的源代码，做到可见即可爬
# 。对于一些JavaScript动态渲染的页面来说，此种抓取方式非常有效。本节中，就让我们来感受一下它的强大之处吧

# --------------------------基本使用------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser=webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input=browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait=WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()
# 运行代码后发现，会自动弹出一个Chrome浏览器。浏览器首先会跳转到百度，然后在搜索框中输入Python，接着跳转到搜索结果页
# 搜索结果加载出来后，控制台分别会输出当前的URL、当前的Cookies和网页源代码

# ----------------------声明浏览器对象---------------------
# Selenium支持非常多的浏览器，如Chrome、Firefox、Edge等，还有Android、BlackBerry等手机端的浏览器。
# 另外，也支持无界面浏览器PhantomJS。
# from selenium import webdriver
#
# brower=webdriver.Chrome()
# brower=webdriver.Firefox()
# brower=webdriver.Edge()
# brower=webdriver.PhantomJs()
# brower=webdriver.Safari()

# 这样就完成了浏览器对象的初始化并将其赋值为browser对象


# ----------------------访问页面-----------------------
# from selenium import webdriver
#
# brower=webdriver.Chrome()
# brower.get('https://www.taobao.com')
# print(brower.page_source)
# brower.close()


# ---------------------查找节点---------------------
# 单个节点
# from selenium import webdriver
#
# brower=webdriver.Chrome()
# brower.get('https://www.taobao.com')
# input_frist=brower.find_element_by_name('q')
# input_second=brower.find_element_by_id('q')
# input_third=brower.find_element_by_xpath('//*[@name="q"]')
# input_four=brower.find_element_by_css_selector('#q')
# print(input_frist,input_second,input_third,input_four)
# brower.close()

# 这里我们使用3种方式获取输入框，分别是根据ID、name、XPath获取和CSS选择器，它们返回的结果完全一致，都是WebElement类型

# 这里列出所有获取单个节点的方法：
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector


# Selenium还提供了通用方法find_element()，它需要传入两个参数：查找方式By和值
# 实际上，它就是find_element_by_id()这种方法的通用函数版本，比如find_element_by_id(id)就等价于find_element(By.ID, id)
# from selenium import webdriver
# #from selenium.webdriver.common.by import By
#
# brower=webdriver.Chrome()
# brower.get('https://wwww.taobao.com')
# input_first=brower.find_element(webdriver.common.by.By.ID,'q')
# print(input_first)
# brower.close()


# 多个节点
# 如果查找的目标在网页中只有一个，那么完全可以用find_element()方法。但如果有多个节点，再用find_element()方法查找，就只能得到第一个节点了。
# 如果要查找所有满足条件的节点，需要用find_elements()这样的方法。注意，在这个方法的名称中，element多了一个s，注意区分。
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
#
# brower=webdriver.Chrome()
# brower.get('https://www.taobao.com')
# lis=brower.find_elements_by_css_selector('.service-bd li')
# #我们也可以直接用find_elements()方法来选择
# # lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis)
# brower.close()
# 得到的内容变成了列表类型，列表中的每个节点都是WebElement类型。
# 如果我们用find_element()方法，只能获取匹配的第一个节点，结果是WebElement类型。
# 如果用find_elements()方法，则结果是列表类型，列表中的每个节点是WebElement类型。

# 这里列出所有获取多个节点的方法：
# find_elements_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector


# --------------------节点交互------------------
# Selenium可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作。
# 比较常见的用法有：输入文字时用send_keys()方法，清空文字时用clear()方法，点击按钮时用click()方法。示例如下：
# from selenium import webdriver
# import time
#
# brower=webdriver.Chrome()
# brower.get('https://www.taobao.com')
# input=brower.find_element_by_id('q')
# input.send_keys('iphone')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# button=brower.find_element_by_class_name('btn-search')
# button.click()

# 这里首先驱动浏览器打开淘宝，然后用find_element_by_id()方法获取输入框，然后用send_keys()方法输入iPhone文字，
# 等待一秒后用clear()方法清空输入框，再次调用send_keys()方法输入iPad文字，之后再用find_element_by_class_name()方法获取搜索按钮，
# 最后调用click()方法完成搜索动作。


# ----------------------动作链-------------------------
# 有另外一些操作，它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。
# 实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser=webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 打开网页中的一个拖曳实例，然后依次选中要拖曳的节点和拖曳到的目标节点，接着声明ActionChains对象并将其赋值为actions变量，
# 然后通过调用actions变量的drag_and_drop()方法，再调用perform()方法执行动作，此时就完成了拖曳操作


# ---------------------------- 执行JavaScript--------------------
# 对于某些操作，Selenium API并没有提供。比如，下拉进度条，它可以直接模拟运行JavaScript，此时使用execute_script()方法即可实现
# from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Buttom")')

# --------------------------获取节点信息-------------------------
# 获取属性 使用get_attribute()方法来获取节点的属性
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# url='http://www.zhihu.com/explore'
# browser.get(url)
# logo=browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# 通过get_attribute()方法，然后传入想要获取的属性名，就可以得到它的值

# 获取文本值
# 每个WebElement节点都有text属性，直接调用就可以就可以得到节点内部的文本信息
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# url='https://www.zhihu.com/explore'
# browser.get(url)
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input.text) #提问

# 获取id，位置，标签名和大小
# id属性可以获取节点id，location属性可以获取该节点在页面中的相对位置，tag_name属性可以获取标签名称，size属性可以获取节点的大小，也就是宽高
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# url='https://www.zhihu.com/explore'
# browser.get(url)
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


# ---------------------切换Frame---------------
# 当页面中包含子Frame时，如果想获取子Frame中的节点，需要先调用switch_to.frame()方法切换到对应的Frame，然后再进行操作。
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome()
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No logo')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


# ------------------延时等待---------------------
# 隐式等待
# 当查找节点而节点并没有立即出现的时候，隐式等待将等待一段时间再查找DOM，默认的时间是0。示例如下：
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input)

# 显式等待
# 还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，就返回查找的节点；
# 如果到了规定时间依然没有加载出该节点，则抛出超时异常
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser=webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait=WebDriverWait(browser,10)
# input=wait.until(EC.presence_of_element_located((By.ID,'q')))
# button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input,button)


# ---------------------前进和后退------------------------、
# selenium使用back()方法后退，forward()方法前进
# import time
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.zhihu.com/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


# -----------------------Cookies----------------------
# 使用Selenium，还可以方便地对Cookies进行操作，例如获取、添加、删除Cookies等。示例如下：
# from selenium import  webdriver
#
# browser=webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


# ----------------------选项卡管理-------------------
# import time
# from selenium import webdriver
#
# browser=webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)  #获取当前开启的所有选项卡，返回的是选项卡的代号列表
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')


# ----------------------异常处理-------------------
# NoSuchElementException异常，这通常是节点未找到的异常
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser=webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
