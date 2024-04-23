from PIL import Image
import pprint
from PIL import ExifTags
import exiftool

img_open = Image.open('0XT53409.JPG')
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