> # **Google-meeter**
### A simple python script that uses selenium(chrome web driver),pyautogui,time and schedule modules to enter google meets automatically.

> ## **Contributor**
- [Kallil6454](https://github.com/Kallil6454)

**Note-This might not work on linux or mac, i haven't tested the script on linux or mac.I suggest having a fast internet :)**

## Dependencies- <br />
- **python** <br />
- **pip** <br />
- **chrome-driver/webdriver**

**Pip Modules-** <br />
- selenium for python <br />
- pyautogui <br />
- schedule <br />
- time <br />

## Installing the Dependencies

### **Python**
1. First you have to go to [python's downloads page](https://www.python.org/downloads/).
2. After that you have to click the Download button which downloads the setup file for python.
3. You have to check if the option "Add python(version) to path" is ticked.
4. I recommend you do "Install now".
5. After that it will ask you to input the admin password.
6. You have successfully installed Python 😃.

![This is an image of the setup file](https://docs.python.org/3/_images/win_installer.png)

### **Pip**
1. Pip is already preinstalled when you had installed python correctly.
2. Then check if pip is installed by searching command prompt on windows and then type "pip help" and enter if it shows up like this that means it is installed:

![This is an image of the command prompt which ran "pip help"](https://phoenixnap.com/kb/wp-content/uploads/2021/06/pip-help-command.png)

3. Now do "pip install selenium pyautogui schedule time" and enter.
4. This might take some time downloading.
5. If it says "WARNING: You are using pip version (version); however, version (version) is available.
You should consider upgrading via the 'C:\Python310\python.exe -m pip install --upgrade pip' command".You can upgrade if you want but it is not compulsory.
6. You have successfully installed the pip modules 😃.

### **Chrome-driver/webdriver**
1. First you have to know the chrome version of you browser by clicking the three dots at the top right.
2. Then hover to help then click about google chrome.
3. If you did it correctly it will showup like this:
![This is an image of the chrome version tab](https://help.zenplanner.com/hc/article_attachments/360035466734/_a060ae9af573af5904eddb579d47c870__Image_2019-05-22_at_8.03.00_AM.png)
4. Notedown the version.
5. Then go to [chromium.org downloads](https://chromedriver.chromium.org/downloads)
6. Then look for the version you taken note of in step 4 and then select chromedriver_win32.zip.
7. Then i recommend moving chromedriver_win32.zip to documents and extract it **BUT DONT CLICK THE EXE FILE AFTER EXTRACTION**.
8. You have succesfully installed the chrome-driver.

## Configuration
1. Now that all the dependencies are finished you can now download the zip file of this repository.
2. Move it to the documents folder.
3. Then extract the file which has 3 python files named main_google_meeter.py,google_meeter_back_end and Google_meets.py.

### main_google_meeter.py-
- This is the main file,You have to run this in order to run the full 3 files.

### google_meeter_back_end.py
- This is the backend of the programme
- You have to put your gmail and password into the programme by writing user=("your gmail account name") and pass=("the password of the gmail account") it wil be at the top of the file.
- I recommend to not touch anything in this file so it wont break,If you know what you are doing feel free 👍.

### Google_meets.py
- This is where you put the links you want to join.
- It will be in an order from the first link to the last link in corresponding with time.

## Running it
1. Search idle in windows search then open it.
2. After that press file at the top left and click open.
3. Then go to the documents folder where all the google meeter files and chromedriver.exe are.
4. Then open main_google_meeter.py.
5. Repeat 1st,2nd and 3rd step and this time open Google_meets.py and configure the links and save the file.
6. Configure the links in Google_meets.py and run the main_google_meeter.py by clicking run at the top and press run module(f5).
7. Then it will ask you for the time of the 5 meetings **it is in 24 hours time(Example:-"09:00 which means 9am" while "21:00 means 9pm")**
9. After that you just wait and the programme will do the job for you

## **The options after running main_google_meeter.py**
1. ### Fast option-
- This option helps you to manually give the programme the time in 24 hours for which the meeting occurs
- The place to give the time is in the console which it will prompt you
- This asks 5 meeting times from first to last
2. ### Default option-
- This is a feature for school students 
- You can configure part from line 24 to line 28 by just replacing the values(Example:-schedule.every().day.at("08:30").do(meet1) you can just change the "8:30 in this case so it becomes-schedule.every().day.at("09:00").do(meet1) which will tell the programme to open the google meet at that time

3. ###Automatic leaving-
-You can type how many minutes after you want to leave automatically

4. ###Manually leaving-
- You don't have to type any minutes and do it the normal way of just pressing the red leave button

## IF your account has 2FA (2 Factor Authenthication)
- You only need to do this if you have errors
- You might run the program and wait for it to reach the 2FA confirmation page
- Now Stop the program And Add your Account 
- Close the windows or application and restart the program
- (we are bringing an update for this but you should wait D:)
- AGAIN am mentioning, you only need to do this if you have errors after 2fa page

## Issues
### Windows FireWall Issue
- Windows FireWall may give a pop up about "Windows firewall blocked some features of a app :- python" 
- There is no worry about it, its just python (we wont hack you or something)
- No need to allow and close the windows firewall pop up
- And then you can continue the program will run all fine 

### Chromedriver.exe popping up in taskbar
- We have found the solution to this problem but this is more complicated
- If you know what you are doing just follow instruction on this [article](https://stackoverflow.com/questions/33983860/hide-chromedriver-console-in-python#:~:text=Locate%20and%20edit%20this%20file,py%20in%20your%20Python%20folder.&text=This%20should%20also%20work%20for,to%20start%20the%20webdriver%20process.)

# Congratualtions You Did It :) 
Now wait for the programme to start,**Enjoy**
Star the repo :) 🌠

![pepe happy](https://i.kym-cdn.com/photos/images/original/002/122/095/1b8.png)

**I will Update the Programme when Needed :).**

## messages from kallil6454:
- How to get lazier definition
- why did we make this, we are making things more complex like its just click link off cam and mic and join instead of putting stuffs in correct file and adding time and the intense waiting and then joining in- 
- all you need to be able to win is too [read more]
- i have tested this code for the first time is 11:49 in 29th Jan in your local time
