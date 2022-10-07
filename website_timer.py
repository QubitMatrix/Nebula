import time
import webbrowser
url=""
def web_():
    global url
    set_time=input("Enter the alarm time in hh:mm:ss(24 hr format)")
    url=input("Enter the url of the site to be opened")
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
     time.sleep(1)

    if(actual_time==set_time):
     webbrowser.open(url)#opens the browser and brings it to the front focus,new=0,autoraise=True are default
