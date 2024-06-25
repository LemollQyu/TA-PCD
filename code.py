!pip install ultralytics -q
!pip install pyyaml -q


from ultralytics import YOLO
import yaml
import cv2
from google.colab.patches import cv2_imshow

model = YOLO("yolov8n.pt")

model.predict("kewan.jpg", save = True, save_txt = True);