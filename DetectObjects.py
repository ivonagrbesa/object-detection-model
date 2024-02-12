from ultralytics import YOLO
import tensorflow as tf
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Image
import numpy as np


image_paths=['C:/Users/Ivona/Desktop/Codeasy/yolo_test_dataset/10abae5a94fe5368.jpg']

def Detect(paths):
    model = YOLO('C:/Users/Ivona/Desktop/Codeasy/runs/detect/train20/weights/best.pt')
    for p in image_paths:
        results = model(p, conf=0.2, imgsz=640, show=True, show_labels=True, show_conf=True, show_boxes=True)

        for r in results:
            im_array = r.plot()         
            plt.imshow(im_array[..., ::-1])
            plt.axis('off')
            plt.tight_layout(pad=0)
            plt.show()
        

