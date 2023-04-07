import Image
import video
import dir
import os

def changeVideo(fileName):

    Image.readVideo(fileName, "Unedited")
    try:
        Image.drawBox("Unedited", "Edited")
    except Exception as e:
        print(e)

    try:
        video.makeVideo()
    except Exception as e:
        print(e)

    dir.removeDir("Unedited")
    dir.removeDir("Edited")
    os.remove(fileName)

