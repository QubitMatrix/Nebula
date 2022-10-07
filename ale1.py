#includes screenshot,time,webcam,websitetimer,zoomtimer,playing video yt,sending automated whatsapp direct messages,shutdown restart and open notepad,set reminder
import speech_recognition as sr
import shu
import webcam1
import screenshot1
from time import sleep,strftime
import pywhatkit
import pyttsx3
import website_timer
import reminder
import wha1
import zoom1

true=True
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
command=''
liscou=0
def talk(text):#function to make the computer speak the text
    engine.say(text)
    engine.runAndWait()#not audible without this

def take_command():
      global command
      global liscou
      global true
      with sr.Microphone() as source:#listen to user input as voice
        listener.adjust_for_ambient_noise(source,duration=3)#tune to the surroundings,duration is the time alloted for ambient check before going to listening part
        print(liscou)
        if(liscou<3):
            talk("listening")
        print("listening")
        try:
            print("try")
            command=''
            voice = listener.listen(source,timeout=3.5,phrase_time_limit=5)#timeout -gap after which goes to next iteration if there is no command,phrase_time_limit-max time for phrase
            #when no input there is an error of timeout time reached so it goes to except block
            command = listener.recognize_google(voice)#use google to interpret the voice command
            command = command.lower()
            liscou=0
            if 'nebula' in command and 'thank you' not in command and 'thankyou' not in command:#name of the assistant to activate the process after inactivity
                command=command.replace('nebula','')
                print(command)

            elif 'thank you' in command or 'thankyou' in command:#to end and close the process
                print('you are welcome, bye')
                talk('you are welcome, bye')
                true=False
        except:
            liscou+=1
            pass
      if(liscou<3):
          return command
      else:
          if (liscou == 3):
              talk("Due to inactivity the prompts are paused, say nebula to start again")
          return "no command"

def run_nebula():
    global command
    command=take_command()
    #print(command)

    if 'play' in command:
        song=command.replace('play','')
        talk('playing' +song)
        pywhatkit.playonyt(song)#plays the first video on youtube under the given search
    elif 'the time' in command:
        time=strftime("%I%M %p")
        a=time[0:2]
        aa=int(a)
        b=time[2:4]
        bb=int(b)
        d1={0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine",30:"thirty",31:"thirty one",32:"thirty two",33:"thirty three",34:"thirty four",35:"thirty five",36:"thirty six",37:"thirty seven",38:"thirty eight",39:"thirty nine",40:"forty",41:"forty one",42:"forty two",43:"forty three",44:"forty four",45:"forty five",46:"forty six",47:"forty seven",48:"forty eight",49:"forty nice",50:"fifty",51:"fifty one",52:"fifty two",53:"fifty three",54:"fifty four",55:"fifty five",56:"fifty six",57:"fifty seven",58:"fifty eight",59:"fifty nine"}
        c=time[-2:]
        print(time)
        talk('current time is '+d1[aa]+d1[bb]+c)
    elif 'screenshot' in command:
        screenshot1.takeScreenshot()#invokes the function 'takeScreenshot' in the python file screenshot1
        print('Screenshot taken')
        talk("Screenshot taken")
    elif 'webcam' in command or 'web camera' in command or 'camera' in command:
        webcam1.webcamm()
        print('photo captured')
        talk('photo captured')
    elif 'set webtimer' in command or 'website timer' in command or 'web timer' in command:
        website_timer.web_()
        print("Time to open", website_timer.url)
        talk("The url is opened")
    elif 'zoom timer' in command or 'zoomtimer' in command or 'zoom meeting' in command:
        zoom1.zoom_()
        www_=zoom1.www
        if(www_==1):
            fc="wrong id"
        elif(www_==2):
            sleep(6)
            fc="logged into meeting"
        elif(www_==3):
            fc="wrong password"
        print(fc)
        talk(fc)
    elif "whatsapp" in command or 'send' in command:
        if 'schedule' in command or 'scheduled' in command:#schedule send 'text' to 'person'
            command=command.strip()
            text1=command[command.index("send ")+5:command.index("to ")-1]
            num1=command[command.index("to ")+3:]
            print(text1,num1)
            ttt=wha1.scheduledmes(text1,num1)
        else:#of the format send 'text' to 'person'
            command=command.strip()
            text1 = command[command.index("send ") + 5:command.index("to ") - 1]
            num1 = command[command.index("to ")+3:]
            print(text1, num1)
            ttt=wha1.instantmes(text1,num1)
        if(ttt):
            talk("message sent")
        else:
            talk("message not sent, try again")
    elif 'open note pad'in command or 'notepad' in command:
        shu.openn()
    elif 'reminder' in command or 'remind' in command:#set a reminder to something
        talk("Enter time")
        n=input("Enter time(24hr hh:mm)")
        reminder.setrem(n)
        try:
            s1=command[command.index("reminder to")+12:]
        except:
            s1=command[command.index("remind me to")+13:]
        s1="reminder to "+s1

        talk(s1)
        print(s1)
    elif 'restart' in command:
         shu.restartt()
    elif 'shutdown' in command or 'shut down' in command:
        shu.shutdownn()
def run():
    while true:#keeps running until user decides to terminate (thank you nebula)
     run_nebula()



