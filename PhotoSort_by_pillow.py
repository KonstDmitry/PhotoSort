from PIL import Image, ExifTags
import pprint
import os
img_tags = ExifTags.TAGS
print(img_tags.items())

# with Image.open('Photo/R0250255.JPG') as img:
#     # получаем словарь EXIF-кодов
#     # из изображения 'photo.jpg'
#     exif = img.getexif()
#     for key, val in exif.items():
#         # сопоставляем `EXIF`-коды с известными
#         # значениями из `ExifTags.TAGS`
#         print(img_tags.get(key, key), ':', val)

img_open = Image.open('Photo/IMG_3394.CR2')
img_data = img_open.getdata()
img_info = img_open.format
img_exif = img_open.getexif()
pprint.pprint(dict(img_exif), width = 1)
a = str(img_exif.get(272, None)).rstrip()
b = img_exif.get(306, None)
print(a, b)
