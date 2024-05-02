import os
import time
import datetime
import shutil
import namecreator
import dict_test
import numbering
import namematch
from exif import Image
from PIL import Image as pil_image


img_old_folder = (input(
    f"Введите начальный путь к папке:").rstrip()
                  or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/')
img_new_folder = (input(
    f"Введите конечный путь к папке:").rstrip()
                  or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/New/')
## Сразу создаем пустую папку для иных файлов

if not os.path.exists(f"{img_new_folder}00_Other/"):
    os.mkdir(f"{img_new_folder}00_Other/")

## Список переменных, словарей и т.п.

img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG', 'jpg', 'jpeg'}
camera_list_rename = ['0XT5', 'X100F', '0XT2', 'XS10', 'PRO1']
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
camera_model_list = []

for dirpath, dirnames, filenames in os.walk(img_old_folder):  # Обращаемся ко всем файлам в папках
    for filename in filenames:
        ## Узнаем общий длинный путь к файлу
        path_file = os.path.join(dirpath, filename)
        file_count += 1
        ## Ищем совпадение формата в названии файла
        if set(filename.split('.')) & img_format:
            img_count += 1
            try:
                ## Пытаемся вытянуть значения через exif
                with open(path_file, 'rb') as img_file_exif:
                    img_by_exif_file = Image(img_file_exif)
                    img_by_exif_date = img_by_exif_file.datetime
                    img_by_exif_camera = img_by_exif_file.model.replace(' ', '')
                    camera_model_list.append(img_by_exif_camera)
                    file_weight += os.path.getsize(path_file)
                    print(f"{filename} {img_by_exif_date} {img_by_exif_camera} (by exif)")
                    file_exif_count += 1
                    img_dict[img_by_exif_file] = [path_file,
                                                  img_by_exif_date,
                                                  img_by_exif_camera]
                    img_by_exif_date_time_str = img_by_exif_date
                    img_by_exif_date_time_obj = datetime.datetime.strptime(img_by_exif_date_time_str,

                                                                           '%Y:%m:%d %H:%M:%S')
                    img_by_exif_date_time_obj_format = img_by_exif_date_time_obj.strftime('%y%m%d')
                    img_folder_list.append(img_by_exif_date_time_obj_format)

                    if not os.path.exists(img_new_folder + img_by_exif_date_time_obj_format):
                        os.makedirs(img_new_folder + img_by_exif_date_time_obj_format)
                        print(f"Папка {img_by_exif_date_time_obj_format} создана")
                    else:
                        print(f"Папка {img_by_exif_date_time_obj_format} уже существует")
                    shutil.copy2(path_file,
                                 img_new_folder + img_by_exif_date_time_obj_format)
                    os.rename(f"{img_new_folder}{img_by_exif_date_time_obj_format}/{filename}",
                              f"{img_new_folder}{img_by_exif_date_time_obj_format}/{namematch.namematch(img_by_exif_camera)}{filename[4:]}")
            except:
                print(f"{filename} {img_by_exif_date} {img_by_exif_camera} (by exif) не удалось открыть")
                try:
                    ## Если не вышло 1-го варианта, пытаемся вытянуть данные через PIL
                    img_by_pil_file = pil_image.open(path_file)
                    img_by_pil_open = img_by_pil_file.getexif()
                    img_by_pil_date = img_by_pil_open.get(306, None)
                    img_by_pil_camera = str(img_by_pil_open.get(272, None).replace(' ', ''))
                    camera_model_list.append(img_by_pil_camera)
                    print(f"{filename} {img_by_pil_date} {img_by_pil_camera} (by PIL)")
                    file_pil_count += 1
                    img_by_pli_date = img_by_exif_date
                    img_by_pil_date_time_obj = datetime.datetime.strptime(img_by_pli_date, '%Y:%m:%d %H:%M:%S')
                    img_by_pil_date_time_obj_format = img_by_pil_date_time_obj.strftime('%y%m%d')
                    img_folder_list.append(img_by_pil_date_time_obj_format)
                    img_dict[img_by_pil_file] = [img_old_folder + filename,
                                                 img_by_pil_date,
                                                 img_by_pil_camera]
                    if not os.path.exists(img_new_folder + img_by_pil_date_time_obj_format):
                        os.makedirs(img_new_folder + img_by_pil_date_time_obj_format)
                        print(f"Папка {img_by_pil_date_time_obj_format} создана")
                    else:
                        print(f"Папка {img_by_pil_date_time_obj_format} уже существует")
                    shutil.copy2(path_file,
                                 img_new_folder + img_by_pil_date_time_obj_format)
                    os.rename(f"{img_new_folder}{img_by_pil_date_time_obj_format}/{filename}",
                              f"{img_new_folder}{img_by_pil_date_time_obj_format}/{namematch.namematch(img_by_pil_camera)}{filename[4:]}")
                except:
                    continue
                shutil.copy2(path_file, f"{img_new_folder}00_Other/")
                other_files.append(path_file)
                continue
        else:
            other_count += 1
            shutil.copy2(path_file, f"{img_new_folder}00_Other/")
            other_files.append(path_file)
            print(f"{path_file}: не фото")

print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранный файлов: {img_count}")
print(f"Количество через библоиотеку exif: {file_exif_count}")
print(f"Количество через библоиотеку PIL: {file_pil_count}")
print(f"Количество исключенных файлов: {other_count}")
print(f"Общий вес всех фотографий: {file_weight / 1048576}")

# print(img_folder_list)
# print(img_dict.keys())

unique_folder = list(set(img_folder_list))
print(f"Список уникальных дат: {unique_folder} и их количество - {len(unique_folder)}")
unique_camera_model = list(set(camera_model_list))
print(f"Список уникальных моделей камеры: {unique_camera_model} и их количество - {len(set(camera_model_list))}")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд или {execution_time / 60} минут")

for k, v in img_dict.items():
    print(f"{k} --> {v}")

for i in other_files:
    print(i)

# numbering.numbers(img_dict)
numbering.name_sort(img_new_folder)

print('test')
print('trdt')