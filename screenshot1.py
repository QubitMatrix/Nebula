import pyautogui
from time import strftime

def takeScreenshot():
    myScreenshot=pyautogui.screenshot()
    string=strftime("%d_%m_%H_%M_%S")#get current time
    asd="{}/text".format("screenshots")+string+".png"#unique name for the screenshot(\gives an error as it considers it as unicodes so / is used in the path of it
    #just the path screenshot\filename also works as the folder is within the project (absolute path if folder outside the project environment)
    myScreenshot.save(asd)



