import webbrowser
from time import sleep, strftime
import pyautogui as pgg
#pg.sendwhatmsg_instantly("+91 xxxxxxxxxx","abc")#using inbuilt whatsapp library pywhatkit
#this user defined module is defined for sending instant or scheduled individual messages without using inbuilt package pywhatkit
def instantmes(tex,name):
    fil = open("whatsappcontacts.txt")
    list1 = fil.readlines()
    d1 = {}
    try:#in case of blank lines
     for x1 in list1:
        x1 = x1.strip()
        k1 = x1[:x1.index("-")]
        d1[k1] = x1[x1.index("-")+1:]
    except:
     pass

    try:#if name is not found
        num=d1[name]
        mes=tex
        webbrowser.open(f"https://web.whatsapp.com/send?phone={num}&text={mes}")
        sleep(20)#buffer time for page to load
        aaa=pgg.locateCenterOnScreen("arrow.png")#works only if picture taken on that pc(as pixels vary)
        #print(aaa)
        pgg.click(pgg.locateCenterOnScreen("arrow.png"))
        if(aaa==None):
           return False
        else:
           return True
    except:
        print("name not found")
        return False

def scheduledmes(tex,name):
    fil = open("whatsappcontacts.txt")
    list1 = fil.readlines()
    d1 = {}
    try:
      for x1 in list1:
        x1 = x1.strip()
        k1 = x1[:x1.index("+")-1]
        d1[k1] = x1[x1.index("-") + 1:]
    except:
      pass

    try:
        num=d1[name]
        mes=tex
        times=input("Enter the time in hr:min(24hr) format")
        th=int(times[0:2])
        tm=int(times[3:5])
        ctime=strftime("%H:%M")
        cth = int(ctime[0:2])
        ctm = int(ctime[3:5])
        minleft=th*60+tm-(cth*60+ctm)
        if (minleft < 0):
         minleft = 1440+minleft  # if time less than system time timer schedules for the nextday
        h3 = minleft // 60
        m3 = minleft % 60
        print("Time in which the message is to be sent is {} hours,{} minutes".format(h3, m3))

        while(ctime!=times):
         ctime=strftime("%H:%M")
         continue
        webbrowser.open(f"https://web.whatsapp.com/send?phone={num}&text={mes}")
        sleep(20)
        aaa = pgg.locateCenterOnScreen("arrow.png")
        #print(aaa)
        pgg.click(pgg.locateCenterOnScreen("arrow.png"))
        if (aaa == None):
         return False
        else:
         return True
    except:
        return False

#instantmes("abc","me")
