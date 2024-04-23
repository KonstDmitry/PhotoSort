from exif import Image
import os
from binascii import hexlify
import pprint

print()

path_photo = 'Photo/'
img_format = ['.RAW', '.RAF', '.CR2', '.JPG']


for i in range(len(os.listdir(path_photo))):
    img = os.listdir(path_photo)[i]
    img_path = path_photo + img
    try:
        img in img_format
        with open(str(img_path), 'rb') as image_file:
            my_image = Image(image_file)
            my_camera_model = str(my_image.model).rstrip()
            print(f"{img} {my_camera_model} : {my_image.datetime} {my_image.has_exif}")
    except:
        print(f"Пропустил файл: {os.listdir(path_photo)[i]} {my_image.has_exif}")
        continue

#     my_camera_model = my_image.model
#     my_camera_lens = str(my_image.lens_model).rstrip()
#     my_camera_lens_focal = my_image.lens_specification
#     my_camera_date = my_image.datetime
#     my_camera_date_original = my_image.datetime_original
#
# print(my_camera_model)
# print(my_camera_lens)
# print(my_camera_lens_focal)
# print(my_camera_date)
# print(my_camera_date_original)
#
# for i in range(len(my_image.list_all())):
#     print(f"{i}: {my_image.list_all()[i]}")
