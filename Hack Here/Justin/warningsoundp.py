from playsound import playsound
import cv2
import numpy
camera=cv2.VideoCapture(0)
success,frame1=camera.read()
success,frame2=camera.read()

while True:
    difference=cv2.absdiff(frame1,frame2)
    frame1=frame2
    success,frame2=camera.read()
    change=numpy.count_nonzero(difference)
    if change>800000:
        print("warning")
        cv2.putText(difference,"WARNING",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
        playsound("mysound.mp3")
    cv2.imshow("out",difference)
    end=cv2.waitKey(1)
    if end==ord('a'):
        camera.release()
        cv2.destroyAllWindows()
        break