from exif import Image
from PIL import Image as PILImage
import os
import time

start_time = time.time()

path_photo = '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/FUJI_203/SubFolder/'
img_format = ['.RAW', '.RAF', '.CR2', '.JPG', 'DNG']

img_all_count = 0
img_in_count = 0
img_out_count = 0

# for i in os.listdir(path_photo):
#     print(i)

for img in os.listdir(path_photo):
    img_path = path_photo + img
    print(img_path)
    img_all_count += 1
    with open(img_path, 'rb') as image_file:
        my_image = Image(image_file)
        image_file = image_file
        print(image_file)
    try:
        # for i in image_file:
        #     image_file[-6:-2] in i
        #     print('YES')
            # if '.CR2' in img:
            #     print('YES')
            #     img_open = Image.open(img_path)
            #     img_exif = img_open.getexif()
            #     a = img_exif.get(272, None)
            #     b = img_exif.get(306, None)
            #     print(a, b)

            # else:
            #     continue
            with open(img_path, 'rb') as image_file:
                my_image = Image(image_file)
                my_camera_model = my_image.model
                print(f"{img} {my_camera_model} : {my_image.datetime}")
                img_in_count += 1
    except:
        img_out_count += 1
        print(f"Пропустил файл: {img}")
        continue
print()
print(f"Количество всех файлов: {img_all_count}")
print(f"Количество отобранный файлов: {img_in_count}")
print(f"Количество исключенных файлов: {img_out_count}")

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

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")