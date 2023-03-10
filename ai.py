import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def findPeople(objectNum, filename):
    
    # Images
    imgs = [filename]  # batch of images

    # Inference
    results = model(imgs)

    return(int(results.pandas().xyxy[0].xmin[objectNum]), int(results.pandas().xyxy[0].xmax[objectNum]), int(results.pandas().xyxy[0].ymin[objectNum]), int(results.pandas().xyxy[0].ymax[objectNum]))