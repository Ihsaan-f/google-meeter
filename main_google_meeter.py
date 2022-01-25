import schedule
import pyautogui
from google_meeter_back_end import meet1,meet2,meet3,login,meet4,meet5
import time
from selenium import webdriver
time.sleep(5)
#You can change the time of these 5 lines
schedule.every().day.at("08:30").do(meet1)
schedule.every().day.at("09:30").do(meet2)
schedule.every().day.at("10:25").do(meet3)
schedule.every().day.at("11:20").do(meet4)
schedule.every().day.at("12:15").do(meet5)


while 1:
    schedule.run_pending()
    time.sleep(1)
