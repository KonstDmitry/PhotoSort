from PIL import Image
import pprint
import os

path_photo = 'Photo/'

img_open = Image.open('Photo/XS109856.RAF')
img_data = img_open.getdata()
print(img_data)
img_info = img_open.format
print(img_info)
img_exif = img_open.getexif()
pprint.pprint(dict(img_exif), width = 1)
a = img_exif.get(272, None)
b = img_exif.get(306, None)
print(a, b)
# a = exiftool.ExifToolHelper.get_tags()
#
# print(a)