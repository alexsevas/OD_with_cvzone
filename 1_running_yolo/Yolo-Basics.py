from ultralytics import YOLO
import cv2

# C:\PROJECTS\_Weights_\Yolo8\Yolo8Detection  C:\\PROJECTS\\_Weights_\\Yolo8\\Yolo8Detection\\
model = YOLO('yolov8l.pt')
'''
При запуске Yolo без пути к файлу с весами - они грузятся с Github с таким сообщением:

WARNING  Ultralytics settings reset to defaults. 
This is normal and may be due to a recent ultralytics package update, but may have overwritten previous settings. 
You may view and update settings directly in 'C:\Users\A43X\AppData\Roaming\Ultralytics\settings.yaml'
Downloading https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt to yolov8l.pt...

'''
results = model("Images/3.png", show=True)

cv2.waitKey(0)