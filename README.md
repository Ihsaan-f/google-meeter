> # **Google-meeter**
### A simple python script that uses selenium(chrome web driver),pyautogui,time and schedule modules to enter google meets automatically.

**Note-This might not work on linux or mac, i haven't tested the script on linux or mac.I suggest having a fast internet :)**

## Dependencies- <br />
- **python** <br />
- **pip** <br />
- **chrome-driver**

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
6. You have successfully installed Python 😃

![This is an image of the setup file](https://docs.python.org/3/_images/win_installer.png)

### **Pip**
1. Pip is already preinstalled when you had installed python correctly.
2. Then check if pip is installed by searching command prompt on windows and then type "pip help" and enter if it shows up like this that means it is installed.

![This is an image of the command prompt which ran "pip help"](https://phoenixnap.com/kb/wp-content/uploads/2021/06/pip-help-command.png)

3. Now do "pip install selenium pyautogui schedule time" and enter.
4. This might take some time downloading.
5. If it says "WARNING: You are using pip version (version); however, version (version) is available.
You should consider upgrading via the 'C:\Python310\python.exe -m pip install --upgrade pip' command".You can upgrade if you want but it is not compulsory.
6. You have successfully installed the pip modules 😃

### **Chrome-driver/webdriver**
1. First you have to know the chrome version of you browser by clicking the three dots at the top right
2. Then hover to help then click about google chrome
3. If you did it correctly it will showup like this:
![This is an image of the chrome version tab](https://help.zenplanner.com/hc/article_attachments/360035466734/_a060ae9af573af5904eddb579d47c870__Image_2019-05-22_at_8.03.00_AM.png)
4. Notedown the version
5. Then go to [chromium.org downloads](https://chromedriver.chromium.org/downloads)
6. Then look for the version you taken note of in step 4 and then click and choose chromedriver_win32.zip
7. Then i recommend moving chromedriver_win32.zip to documents and extract it **BUT DONT CLICK THE EXE FILE AFTER EXTRACTION**
8. You have succesfully installed the chrome-driver

## Configuration
1. Now that all the dependencies are finished you can now download the zip file of this repository
2. Move it to the documents folder
3. Then extract the file which has 3 python files named google meeter.py,google_meeter_back_end and Google_meets.py

### google meeter.py-
- This is the main file,You have to run this in order to run the full 3 files
- You can change the time settings according to your wish

### google_meeter_back_end.py
- This is the backend of the programme
- You have to put your gmail and password into the programme by writing user=("your gmail account name") and pass=("the password of the gmail account") it wil be at the top of the file
- I recommend to not touch anything in this file so it wont break,If you know what you are doing feel free 👍

### Google_meets.py
- This is where you put the links you want to join
- It will be in an order from the first link to the last link

## Running it
1. Search idle in windows search then open it
2. After that press file at the top left and click open
3. Then go to the documents folder where all the google meeter files and chromedriver.exe are
4. Then open google meeter.py
5. Repeat 1,2 and 3 step and this time open Google_meets.py and configure the links and save the file
6. After everthing is done like configuring time and saving in google meeter.py run the file by clicking run at the top and press run module(f5)

# Congratualtions You Did It :)
Now wait for the programme to start at the time you kept it 

**I will Update the Programme when Needed :)**
