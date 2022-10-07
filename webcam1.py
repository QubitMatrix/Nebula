import cv2#opencv-opensourcecomputervision
from time import strftime

def webcamm():
    vid=cv2.VideoCapture(0)#opens webcam(0-default camera)
    while(True):
     a,frame=vid.read()#a-True if a frame can be grabbed else false, frame- array of pictures taken from webcam
     #print(frame)
     cv2.imshow('Camera',frame)#shows the camera screen
     if cv2.waitKey(1) & 0xff==ord('q'):#to take a picture and close the webcam screen
        string=strftime("%d_%m_%H_%M_%S")
        filename="pictures/"+string+".png"#unique filename
        pic=frame.copy()#freezes the video at the instant and stores the picture
        cv2.imwrite(filename,pic)
        vid.release()#release the image captured
        cv2.destroyAllWindows()#destroy and close all screens
        break
#webcamm()
