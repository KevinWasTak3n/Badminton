import cv2
import os

def makeVideo():
  image_folder = 'Edited'
  video_name = 'video.avi'
  images = []
  z = 0
  while True:
      try:
          images.append(cv2.imread(f'{image_folder}\\aiBox{z}.jpg', cv2.IMREAD_UNCHANGED))
      except:
          break
      z+=1
        
  frame = images[0]
  height, width, layers = frame.shape

  fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
  video = cv2.VideoWriter(video_name, fourcc, 15, (width,height))

  for image in images:
      video.write(image)
  cv2.destroyAllWindows()
  video.release()

# import cv2 
# import dir

# # Create a video capture object, in this case we are reading the video from a file
# def readVideo(path, folderName):
#   vid_capture = cv2.VideoCapture(path)
#   dir.makeDir(folderName)

#   i = 0

#   while(vid_capture.isOpened()):
#     # vid_capture.read() methods returns a tuple, first element is a bool 
#     # and the second is frame
#     ret, frame = vid_capture.read()
#     if ret == True:

#       #cv2.imshow('Frame',frame)
#       # 20 is in milliseconds, try to increase the value, say 50 and observe
#       #key = cv2.waitKey(100)

#       cv2.imwrite(f'{folderName}\\Original{i}.jpg', frame)
#       i += 1

#     else:
#       break
  
#   # Release the video capture object
#   vid_capture.release()
#   #cv2.destroyAllWindows()

# #readVideo("Uncut.mp4", "Unedited")