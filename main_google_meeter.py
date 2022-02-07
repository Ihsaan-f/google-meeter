import schedule
from google_meeter_back_end import meet1,meet2,meet3,login,meet4,meet5
import time
from ascii_art import logo

print(logo)
time.sleep(2)
option =str(input("Do you want the fast option or the default standard option.Read the github page for more info-\nfast/def or f/d:"))

if option=="fast" or option=="f":
    #Credit Kallil6454
    Time1 = str(input("Enter your Time for 1st meeting. 24 HOUR FORMAT:"))
    Time2 = str(input("Enter your Time for 2th meeting. 24 HOUR FORMAT:"))
    Time3 = str(input("Enter your Time for 3rd meeting. 24 HOUR FORMAT:"))
    Time4 = str(input("Enter your Time for 4th meeting. 24 HOUR FORMAT:"))
    Time5 = str(input("Enter your Time for 5th meeting. 24 HOUR FORMAT:"))
    schedule.every().day.at(Time1).do(meet1)
    schedule.every().day.at(Time2).do(meet2)
    schedule.every().day.at(Time3).do(meet3)
    schedule.every().day.at(Time4).do(meet4)
    schedule.every().day.at(Time5).do(meet5)
    
elif option=="def" or option=="d":    
    #You can change the time of these 5 lines
    schedule.every().day.at("08:30").do(meet1)
    schedule.every().day.at("09:30").do(meet2)
    schedule.every().day.at("10:25").do(meet3)
    schedule.every().day.at("11:20").do(meet4)
    schedule.every().day.at("12:15").do(meet5)
    
else:
    print(":/ also restart the programme you messed up")

while 1:
    schedule.run_pending()
    time.sleep(1)
