from selenium import webdriver
import time
import pyautogui
from Google_meets import meeting_1,meeting_2,meeting_3,meeting_4,meeting_5

#Enter credentials
username = ""
password = ""

#The Credential login in gmail
def login(driver):
    driver.get('https://apps.google.com/meet/')
    driver.fullscreen_window()
    sign_in  = driver.find_element_by_xpath("/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a")
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
    #Delete the hashtag which is below this message if you want 2 factor authentication on
    #authentication = str(input("If you have 2 factor authentication accept the pop up sent in your phone,if you accepted it type yes here,If you dont have it you can just say yes:"))



#The meeting logins
def meet1():
    driver1 = webdriver.Chrome()
    login(driver1)
    time.sleep(5)
    first_meet = driver1.get(meeting_1)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    mic = driver1.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    mic.click()
    time.sleep(1)
    cam = driver1.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
    cam.click()
    time.sleep(1)
    joinow = driver1.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
    joinow.click()
    
    question = str(input("Do you want to leave manually or automatically,Enter man for manual and auto for automatic read the github for more info: \n"))
    if question == "auto" or question == "automatic":
        min = int(input("After how many minutes do you want to leave the meeting:"))
        # converting it into seconds
        min = min * 60
        time.sleep(min)
        driver1.quit()
    else:
        print("Ok")


def meet2():
    driver2 = webdriver.Chrome()
    login(driver2)
    time.sleep(5)
    first_meet = driver2.get(meeting_2)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    mic = driver2.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    mic.click()
    time.sleep(1)
    cam = driver2.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
    cam.click()
    time.sleep(1)
    joinow = driver2.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
    joinow.click()
    
    question = str(input("Do you want to leave manually or automatically,Enter man for manual and auto for automatic read the github for more info: \n"))
    if question == "auto" or question == "automatic":
        min = int(input("After how many minutes do you want to leave the meeting:"))
        # converting it into seconds
        min = min * 60
        time.sleep(min)
        driver2.quit()
    else:
        print("Ok")



def meet3():
    driver3 = webdriver.Chrome()
    login(driver3)
    time.sleep(5)
    first_meet = driver3.get(meeting_3)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    mic = driver3.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    mic.click()
    time.sleep(1)
    cam = driver3.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
    cam.click()
    time.sleep(1)
    joinow = driver3.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
    joinow.click()
    
    question = str(input("Do you want to leave manually or automatically,Enter man for manual and auto for automatic read the github for more info: \n"))
    if question == "auto" or question == "automatic":
        min = int(input("After how many minutes do you want to leave the meeting:"))
        # converting it into seconds
        min = min * 60
        time.sleep(min)
        driver3.quit()
    else:
        print("Ok")


def meet4():
    driver4 = webdriver.Chrome()
    login(driver4)
    time.sleep(5)
    first_meet = driver4.get(meeting_4)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    mic = driver4.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    mic.click()
    time.sleep(1)
    cam = driver4.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
    cam.click()
    time.sleep(1)
    joinow = driver4.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
    joinow.click()
    
    question = str(input("Do you want to leave manually or automatically,Enter man for manual and auto for automatic read the github for more info: \n"))
    if question == "auto" or question == "automatic":
        min = int(input("After how many minutes do you want to leave the meeting:"))
        # converting it into seconds
        min = min * 60
        time.sleep(min)
        driver4.quit()
    else:
        print("Ok")


def meet5():
    driver5 = webdriver.Chrome()
    login(driver5)
    time.sleep(5)
    first_meet = driver5.get(meeting_5)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    mic = driver5.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div")
    mic.click()
    time.sleep(1)
    cam = driver5.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div")
    cam.click()
    time.sleep(1)
    joinow = driver5.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
    joinow.click()
    
    question = str(input("Do you want to leave manually or automatically,Enter man for manual and auto for automatic read the github for more info: \n"))
    if question == "auto" or question == "automatic":
        min = int(input("After how many minutes do you want to leave the meeting:"))
        # converting it into seconds
        min = min * 60
        time.sleep(min)
        driver5.quit()
    else:
        print("Ok")
