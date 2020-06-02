import json
import os
from PIL import Image
import numpy as np
from config import scale,maxScale,TEXT_LINE_SCORE
from pprint import pprint
import cv2
from dnn.main import text_ocr

img = Image.open(os.environ["OCR_IMAGE_PATH"]).convert('RGB')
image = np.array(img)
image =  cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
data = text_ocr(image,scale,maxScale,TEXT_LINE_SCORE)

print(json.dumps(data))
