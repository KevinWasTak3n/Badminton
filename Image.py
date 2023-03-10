import cv2
from ai import findPeople
import dir
import video
from Court import drawCourt
import numpy as np

def readVideo(path, folderName):
  vid_capture = cv2.VideoCapture(path)
  dir.makeDir(folderName)

  i = 0

  while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool 
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:

      #cv2.imshow('Frame',frame)
      # 20 is in milliseconds, try to increase the value, say 50 and observe
      #key = cv2.waitKey(100)

      cv2.imwrite(f'{folderName}\\Original{i}.jpg', frame)
      i += 1

    else:
      break
  
  # Release the video capture object
  vid_capture.release()

def drawBox(pastFolder, newFolder):
    dir.makeDir(newFolder)
    z = 0
    while True:
        try:
            image = cv2.imread(f'{pastFolder}\\Original{z}.jpg', cv2.IMREAD_UNCHANGED)
        except:
            return

        image, otherImage = drawCourt(image)
        
        for i in range (0,2):
            a,b,c,d = findPeople(i, f'{pastFolder}\\Original{z}.jpg')

            pointA = (a,c)
            pointB = (b,d)
            cv2.rectangle(image, pointA, pointB, (255,255,0), thickness = 3, lineType = cv2.LINE_AA)
            otherImage = cv2.circle(otherImage, ((a+b)//2, d), 20, (225,0,0), -1)

        height, width, channels = image.shape
        newImage = np.zeros((2*height,width,channels), np.uint8)
        newImage[0:otherImage.shape[0], 0:otherImage.shape[1]] = otherImage
        newImage[otherImage.shape[0]:, 0:otherImage.shape[1]] = image

        cv2.imwrite(f'{newFolder}\\aiBox{z}.jpg', newImage)

        z += 1

def displayVideo(pastFolder):
    z = 0
    while True:
        try:
            image = cv2.imread(f'{pastFolder}\\aiBox{z}.jpg', cv2.IMREAD_UNCHANGED)
        except:
            return
        cv2.imshow('Image', image)

        z += 1

        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()