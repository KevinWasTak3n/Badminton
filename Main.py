import Image
import video
import dir

Image.readVideo("clip.mp4", "Unedited")
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