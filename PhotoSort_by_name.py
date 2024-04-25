import os
import time
from exif import Image
from PIL import Image as pil_image

img_path = input(f"Введите путь к папке:").rstrip() or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old'
img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG'}
start_time = time.time()
file_count = 0
file_exif_count = 0
file_pil_count = 0
file_weight = 0
img_count = 0
img_dict = {}
other_count = 0

for dirpath, dirnames, filenames in os.walk(img_path):          # Обращаемся ко всем файлам в папках
    for filename in filenames:
        path_file = os.path.join(dirpath, filename)             # Узнаем общий длинный путь к файлу
        # for file in os.listdir(img_path):
        file_count += 1
        if set(filename.split('.')) & img_format:               # Ищем совпадение формата в названии файла
            # print(f"filename {filename}")
            img_count += 1
            try:
                with open(path_file, 'rb') as img_file:         # Пытаемся вытянуть значения через exif
                    # print(f"{file}: Yes")
                    my_img = Image(img_file)
                    img_date = my_img.datetime
                    file_weight += os.path.getsize(path_file)
                    print(f"{filename} {img_date} (by exif)")
                    file_exif_count += 1
                    img_dict[img_date] = path_file
            except:
                try:                                            # Если не вышло 1-го варианта, пытаемся вытянуть данные через PIL
                    img_open = pil_image.open(path_file)
                    img_exif = img_open.getexif()
                    b = img_exif.get(306, None)
                    print(f"{filename} {b} (by PIL)")
                    file_pil_count += 1
                    img_dict[img_date] = img_path + file
                except:
                    continue
                    print(f"{path_file}: No")
                continue
        else:
            other_count += 1
            print(f"{path_file}: No")

print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранный файлов: {img_count}")
print(f"Количество через библоиотеку exif: {file_exif_count}")
print(f"Количество через библоиотеку PIL: {file_pil_count}")
print(f"Количество исключенных файлов: {other_count}")
print(f"Общий вес всех фотографий: {file_weight/1048576}")

print(img_dict)
print(img_dict.keys())

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд или {execution_time/60} минут")
