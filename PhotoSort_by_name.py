import os
import time
from exif import Image
from PIL import Image as pil_image

start_time = time.time()

img_path = input(f"Введите путь к папке:").rstrip() or 'Photo/'
img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG'}

file_count = 0
file_exif_count = 0
file_pil_count = 0
img_count = 0
other_count = 0

for file in os.listdir(img_path):
    file_count += 1
    if set(file.split('.')) & img_format:
        img_count += 1
        try:
            with open(img_path + file, 'rb') as img_file:
                # print(f"{file}: Yes")
                my_img = Image(img_file)
                img_date = my_img.datetime
                print(f"{file} {img_date}")
                file_exif_count += 1
        except:
            try:
                img_open = pil_image.open(img_path + file)
                img_exif = img_open.getexif()
                # a = str(img_exif.get(272, None)).rstrip()
                b = img_exif.get(306, None)
                print(f"{file} {b}")
                file_pil_count += 1
            except:
                continue
                print(f"{file}: No")
            continue
    else:
        other_count += 1
        print(f"{file}: No")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")
print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранный файлов: {img_count}")
print(f"Количество исключенных файлов: {other_count}")
print(f"Количество через библоиотеку exif: {file_exif_count}")
print(f"Количество через библоиотеку PIL: {file_pil_count}")
