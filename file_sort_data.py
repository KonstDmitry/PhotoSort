from PIL import Image
from PIL import ExifTags
import exiftool

img_open = Image.open('0XT53409.JPG')
img_data = img_open.getdata()
img_info = img_open.format

img_exif = ExifTags.Base
print(img_data)
print(img_exif)

# a = exiftool.ExifToolHelper.get_tags()
#
# print(a)