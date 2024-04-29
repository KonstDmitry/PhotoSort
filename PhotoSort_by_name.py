import os
import time
import datetime
import shutil
import namecreator
from exif import Image
from PIL import Image as pil_image

img_old_folder = input(f"Введите начальный путь к папке:").rstrip() or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/'
img_new_folder = input(f"Введите конечный путь к папке:").rstrip() or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/New/'

a = 15

img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG'}
start_time = time.time()
file_count = 0
file_exif_count = 0
file_pil_count = 0
file_weight = 0
img_count = 0
img_dict = {}
img_folder_list = []
other_count = 0
other_files = []

for dirpath, dirnames, filenames in os.walk(img_old_folder):          # Обращаемся ко всем файлам в папках
    for filename in filenames:
        path_file = os.path.join(dirpath, filename)             # Узнаем общий длинный путь к файлу
        # for file in os.listdir(img_path):
        file_count += 1
        if set(filename.split('.')) & img_format:               # Ищем совпадение формата в названии файла
            # print(f"filename {filename}")
            img_count += 1
            try:
                with open(path_file, 'rb') as img_file_exif:         # Пытаемся вытянуть значения через exif
                    # print(f"{file}: Yes")
                    img_by_exif_file = Image(img_file_exif)
                    img_by_exif_date = img_by_exif_file.datetime
                    img_by_exif_camera = img_by_exif_file.model.replace(' ', '')
                    file_weight += os.path.getsize(path_file)
                    print(f"{filename} {img_by_exif_date} {img_by_exif_camera} (by exif)")
                    file_exif_count += 1
                    img_dict[img_by_exif_date] = [path_file, img_by_exif_camera]
                    img_by_exif_date_time_str = img_by_exif_date
                    img_by_exif_date_time_obj = datetime.datetime.strptime(img_by_exif_date_time_str, '%Y:%m:%d %H:%M:%S')
                    img_folder_list.append(img_by_exif_date_time_obj.strftime('%y%m%d'))
                    if not os.path.exists(img_new_folder + img_by_exif_date_time_obj.strftime('%y%m%d')):
                        os.makedirs(img_new_folder + img_by_exif_date_time_obj.strftime('%y%m%d'))
                        print(f"Папка {img_by_exif_date_time_obj.strftime('%y%m%d')} создана")
                    else:
                        print(f"Папка {img_by_exif_date_time_obj.strftime('%y%m%d')} уже существует")
                    shutil.copy(path_file,
                                img_new_folder + img_by_exif_date_time_obj.strftime('%y%m%d'))
            except:
                try:                                            # Если не вышло 1-го варианта, пытаемся вытянуть данные через PIL
                    img_by_pil_file = pil_image.open(path_file)
                    img_by_pil_open = img_by_pil_file.getexif()
                    img_by_pil_date = img_by_pil_open.get(306, None)
                    img_by_pil_camera = img_by_pil_open.get(272, None).replace(' ', '')
                    print(f"{filename} {img_by_pil_date} {img_by_pil_camera} (by PIL)")
                    file_pil_count += 1
                    img_dict[img_by_exif_date] = [img_old_folder + filename, img_by_pil_date]
                    img_by_pli_date = img_by_exif_date
                    img_by_pil_date_time_obj = datetime.datetime.strptime(img_by_pli_date, '%Y:%m:%d %H:%M:%S')
                    img_folder_list.append(img_by_pil_date_time_obj.strftime('%y%m%d.%f'))
                    if not os.path.exists(img_new_folder + img_by_pil_date_time_obj.strftime('%y%m%d')):
                        os.makedirs(img_new_folder + img_by_pil_date_time_obj.strftime('%y%m%d'))
                        print(f"Папка {img_by_pil_date_time_obj.strftime('%y%m%d')} создана")
                    else:
                        print(f"Папка {img_by_pil_date_time_obj.strftime('%y%m%d')} уже существует")
                    shutil.copy(path_file,
                                img_new_folder + img_by_pil_date_time_obj.strftime('%y%m%d'))
                except:
                    print(f"{path_file}: No")
                    other_files.append(path_file)
                    continue
                continue
        else:
            other_count += 1
            other_files.append(path_file)
            print(f"{path_file}: No")

print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранный файлов: {img_count}")
print(f"Количество через библоиотеку exif: {file_exif_count}")
print(f"Количество через библоиотеку PIL: {file_pil_count}")
print(f"Количество исключенных файлов: {other_count}")
print(f"Обore /Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For Phщий вес всех фотографий: {file_weight/1048576}")

# print(img_folder_list)
# print(img_dict.keys())

unique_folder = list(set(img_folder_list))
print(f"Список уникальных дат: {unique_folder} и их количество - {len(unique_folder)}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд или {execution_time/60} минут")

# for dirpath, dirnames, filenames in os.walk(img_new_folder):          # Обращаемся ко всем файлам в папках
#     for filename in filenames:
#         print(os.path.join(dirpath, filename))

print(img_dict)
print(other_files)
# namecreator.new_path(img_new_folder)
# namecreator.subfolder(img_new_folder)


