import sys
import os
import _io
from collections import namedtuple
from PIL import Image
/Users/lc/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/47d4e17a551ea4400d06c50aa8085ebd/Message/MessageTemp/4b70b29cbbff247a3d4c9827e076e662/File/day10_student_management.py
class Nude(object):
    def __init__(self,path_or_image):
        if isinstance(path_or_image,Image.Image):
            self.image = path_or_image
        elif isinstance(path_or_image,str):
            self.image=Image.open(path_or_image)

        bands=self.image.getbands()
        if len(bands) == 1:
            new_img = Image.new("RGB",self.image.size)
