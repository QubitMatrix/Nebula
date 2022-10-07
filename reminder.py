from time import *
def setrem(t):
    t1=strftime("%H:%M")
    while(t1!=t):
        sleep(1)
        t1=strftime("%H:%M")
if (__name__=="__main__" ):
    setrem("10:50")


