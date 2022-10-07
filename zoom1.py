import pyautogui as pg
import webbrowser
import time
cor=(0,0)
www=9
def zoom_():
    global cor
    global www
    set_time = input("Enter the time when the meeting is to be logged in(hh:mm:ss) format")
    id_ = input("Enter the meeting id")
    pas_ = input("Enter the password")
    actual_time=time.strftime("%H:%M:%S")# get current time in the 24 hour format
    h1=int(set_time[0:2])
    m1=int(set_time[3:5])
    s1=int(set_time[6:8])
    h2=int(actual_time[0:2])
    m2=int(actual_time[3:5])
    s2=int(actual_time[6:8])
    seconds1=h1*60*60+m1*60+s1
    seconds2=h2*60*60+m2*60+s2
    seconds=seconds1-seconds2
    if(seconds<0):
     seconds=86400-(seconds2-seconds1)#if time less than system time timer schedules for the nextday
    m3=seconds//60
    s3=seconds%60
    h3=m3//60
    m3=m3%60
    print("Time in which the browser is to be opened is {} hours,{} minutes and {} seconds".format(h3,m3,s3))
    while(actual_time!=set_time):
     actual_time=time.strftime("%H:%M:%S")
     print(actual_time,set_time)#prints the current time and the time at which it shuould open
     time.sleep(1)

    if(actual_time==set_time):
     webbrowser.open("https://zoom.us/join")#opens zoom in the browser and brings it to the front focus,new=0,autoraise=True are default
    time.sleep(6)
    cor1=pg.locateCenterOnScreen('zoomid.png',confidence=0.5)#confidence needs opencv installed
    pg.click(cor1)#clicks on the given coordinates on the current focused screen
    #print(cor1)
    pg.typewrite(id_)#writes the given text in the space clicked
    pg.press("enter")
    time.sleep(6)#buffer time to load and go to next screen
    cor2=pg.locateCenterOnScreen('password.png',confidence=0.5)
    if(cor2==None):
        www=1#wrong id
    else:
        pg.click(cor2)
        pg.typewrite(pas_)
        pg.press("enter")#equivalent to enter on keyboard
    time.sleep(5)
    cor3=pg.locateCenterOnScreen('wrongpassword.png',confidence=0.5)
    #print(cor3)
    if(cor3==None and www!=1):#wrong password windoww not seen and id entered
        www=2#logged in
    elif(cor3!=None):
        www=3#wrong password

#zoom_()
