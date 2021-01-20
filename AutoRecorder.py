import datetime, time, webbrowser, os, functions
from pynput.keyboard import Key, Controller

keyboard = Controller()

link, meeting_hour, meeting_minute, meeting_length, passcode = functions.get_information()

while True:
    # set time for start of meeting hour here
    if datetime.datetime.now().time().hour == meeting_hour and datetime.datetime.now().time().minute == meeting_minute:
        webbrowser.open(link)
        break
    else:
        time.sleep(60)
# sleep time here is based on how long it takes to load, change as necessary
if passcode != "":
    time.sleep(10)
    keyboard.type(passcode)
    time.sleep(0.5)
    keyboard.press(Key.enter)

# launches recording for an hour and then kills the obs, saving the zoom recording
bashCommand = 'start /d "C:/Program Files/obs-studio/bin/64bit" obs64.exe --startrecording'
os.system(bashCommand)

# set the length of meeting in seconds
time.sleep(meeting_length)
os.system("taskkill /F /IM Zoom.exe")
time.sleep(1)
os.system("taskkill /F /IM obs64.exe")
