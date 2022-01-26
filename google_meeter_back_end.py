from selenium import webdriver
import time
import pyautogui
from Google_meets import meeting_1,meeting_2,meeting_3,meeting_4,meeting_5

#Enter credentials
username = ""
password = ""

#The Credential login in gmail
def login(driver):
    driver.get('https://www.google.com/intl/en-GB/gmail/about/')
    driver.fullscreen_window()
    sign_in  = driver.find_element_by_xpath("/html/body/header/div/div/div/a[2]")
    sign_in.click()
    time.sleep(3)
    user = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    user.send_keys(username)
    next = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next.click()
    time.sleep(3)
    pas = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    pas.send_keys(password)
    next2_0 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next2_0.click()
    #2 factor authentication also Idea by kallil6454 because he has 2fa
    authentication = str(input("If you have 2 factor authentication accept the pop up sent in your phone,if you accepted it type yes here,If you dont have it you can just say yes"))



#The meeting logins
def meet1():
    driver1 = webdriver.Chrome()
    login(driver1)
    time.sleep(10)
    first_meet = driver1.get(meeting_1)
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.keyDown("ctrl")
    time.sleep(2)
    pyautogui.press("d")
    time.sleep(2)
    pyautogui.press("e")
    time.sleep(2)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    repeater=0
    full=7
    while repeater!=full:
        pyautogui.press("tab")
        time.sleep(2)
        repeater+=1
    pyautogui.press("enter")


def meet2():
    driver2 = webdriver.Chrome()
    login(driver2)
    time.sleep(10)
    first_meet = driver2.get(meeting_2)
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.keyDown("ctrl")
    time.sleep(2)
    pyautogui.press("d")
    time.sleep(2)
    pyautogui.press("e")
    time.sleep(2)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    repeater =0
    full =7
    while repeater!=full:
        pyautogui.press("tab")
        time.sleep(2)
        repeater+=1
    pyautogui.press("enter")



def meet3():
    driver3 = webdriver.Chrome()
    login(driver3)
    time.sleep(10)
    first_meet = driver3.get(meeting_3)
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.keyDown("ctrl")
    time.sleep(2)
    pyautogui.press("d")
    time.sleep(2)
    pyautogui.press("e")
    time.sleep(2)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    repeater = 0
    full = 7
    while repeater != full:
        pyautogui.press("tab")
        time.sleep(2)
        repeater += 1
    pyautogui.press("enter")


def meet4():
    driver4 = webdriver.Chrome()
    login(driver4)
    time.sleep(10)
    first_meet = driver4.get(meeting_4)
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.keyDown("ctrl")
    time.sleep(2)
    pyautogui.press("d")
    time.sleep(2)
    pyautogui.press("e")
    time.sleep(2)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    repeater=0
    full=7
    while repeater!=full:
        pyautogui.press("tab")
        time.sleep(2)
        repeater+=1
    pyautogui.press("enter")


def meet5():
    driver5 = webdriver.Chrome()
    login(driver5)
    time.sleep(10)
    first_meet = driver5.get(meeting_5)
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.keyDown("ctrl")
    time.sleep(2)
    pyautogui.press("d")
    time.sleep(2)
    pyautogui.press("e")
    time.sleep(2)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    repeater = 0
    full = 7
    while repeater != full:
        pyautogui.press("tab")
        time.sleep(2)
        repeater += 1
    pyautogui.press("enter")
