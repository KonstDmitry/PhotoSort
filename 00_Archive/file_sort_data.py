from PIL import Image
import pprint
import os
from PIL import ExifTags
import exiftool

path_photo = '../Photo/'
img_format = ['.RAW', '.RAF', '.CR2', '.JPR']


for i in range(len(os.listdir(path_photo))):
    img = os.listdir(path_photo)[i]
    img_path = path_photo + img

img_open = Image.open('../Photo/XS109856.JPG')
img_data = img_open.getdata()
img_info = img_open.format
img_exif = img_open.getexif()
pprint.pprint(dict(img_exif), width = 1)
a = img_exif.get(272, None)
b = img_exif.get(306, None)
print(a, b)
# a = exiftool.ExifToolHelper.get_tags()
#
# print(a)