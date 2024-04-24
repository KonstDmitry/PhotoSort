from PIL import Image, ExifTags
import pprint
import os
img_tags = ExifTags.TAGS

with Image.open('Photo/R0250136.JPG') as img:
    # получаем словарь EXIF-кодов
    # из изображения 'photo.jpg'
    exif = img.getexif()
    for key, val in exif.items():
        # сопоставляем `EXIF`-коды с известными
        # значениями из `ExifTags.TAGS`
        print(img_tags.get(key, key), ':', val)

img_open = Image.open('Photo/R0250136.DNG')
img_data = img_open.getdata()
print(img_data)
img_info = img_open.format
print(img_info)
img_exif = img_open.getexif()
pprint.pprint(dict(img_exif), width = 1)
a = str(img_exif.get(272, None)).rstrip()
b = img_exif.get(306, None)
print(a, b)
