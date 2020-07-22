#coding=utf-8
import cv2
import re
from PIL import Image
import pytesseract
import argparse
import os
for i in range(1, 18605):
    image = cv2.imread("ocr/a ("+str(i)+").jpg")
    #filename = "temp/{}.png".format(os.getpid())
    filename = "temp/"+str(i)+".png"
    cv2.imwrite(filename,image)
    text = pytesseract.image_to_string(Image.open(filename), lang='eng')
    if re.search('FLAG', text):
        print("["+str(i)+"]\r\n")
        print(text+"]\r\n\r\n")
    else:
        os.remove("ocr/a ("+str(i)+").jpg")
    os.remove(filename)