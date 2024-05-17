import os
import time
import module_exif
import module_photo
import shutil

# for win
img_old_folder = (input(
    f"Введите начальный путь к папке:").rstrip()
                  or 'D:/test_copy/')
img_new_folder = (input(
    f"Введите конечный путь к папке:").rstrip()
                  or 'D:/test_copy_new/')

# # for mac
# img_old_folder = (input(
#     f"Введите начальный путь к папке:").rstrip()
#                   or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/')
# img_new_folder = (input(
#     f"Введите конечный путь к папке:").rstrip()
#                   or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/New/')

img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG', 'dng', 'jpg', 'jpeg'}
count_double = 0
file_count = 0
img_count = 0
file_exif_count = 0
file_pil_count = 0
file_other_count = 0
photo_dict ={}

module_exif.path_other(img_new_folder)
module_exif.path_copy(img_new_folder)

file_other = open(f"{img_new_folder}00_Other/file_other.txt", "a")
file_exif = open(f"{img_new_folder}file_exif.txt", "a")
file_pil = open(f"{img_new_folder}file_pil.txt", "a")


start_time = time.time()

for dirpath, dirnames, filenames in os.walk(img_old_folder):
    # Обращаемся ко всем файлам в папках
    for file_name in filenames:
        # Узнаем общий длинный путь к файлу
        file_path = os.path.join(dirpath, file_name)
        file_count += 1
        # Ищем совпадение формата в названии файла
        if set(file_name.split('.')) & img_format:
            img_count += 1
            try:
                img_info = module_photo.photo_exif(file_path, file_name)
                module_photo.path_create(f'{img_new_folder}{img_info['date']}')
                module_photo.file_copy(file_path, img_new_folder, img_info['date'], file_name)
                module_photo.file_rename(img_new_folder, img_info['date'], file_name, img_info['camera'])
                file_exif.write(f"{file_path}" + '\n')
                file_exif_count += 1
                print(img_info)
            except:
                # Пытаемся вытянуть значения через PIL
                try:
                    img_info = module_photo.photo_pil(file_path, file_name)
                    module_photo.path_create(f'{img_new_folder}{img_info['date']}')
                    module_photo.file_copy(file_path, img_new_folder, img_info['date'], file_name)
                    module_photo.file_rename(img_new_folder, img_info['date'], file_name, img_info['camera'])
                    file_pil.write(f"{file_path}" + '\n')
                    file_pil_count += 1
                    print(img_info)
                except:
                    # Если и через PIL не получается, кидаем в другие
                    print(f"{file_path} не удалось открыть")
                    file_other_count += 1
                    shutil.copy2(file_path, f"{img_new_folder}00_Other/")
                    file_other.write(f"{file_path}" + '\n')
        else:
            print(f"{file_path} не фото")
            file_other_count += 1
            shutil.copy2(file_path, f"{img_new_folder}00_Other/")
            file_other.write(f"{file_path}" + '\n')

print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранных файлов: {img_count}")
print(f"Количество через библиотеку exif: {file_exif_count}")
print(f"Количество через библиотеку PIL: {file_pil_count}")
print(f"Количество исключенных файлов: {file_other_count}")
print(f"Общий вес всех фотографий: {module_photo.file_weight_sum}")
print(f"Список уникальных моделей камеры: {module_photo.camera_model_list} и их количество - "
      f"{len(module_photo.camera_model_list)}")
print(f'Общее кол-во дубликатов: {module_photo.count_double}')

end_time = time.time()
execution_time = end_time - start_time

print(f"Время выполнения программы: {execution_time} секунд или {execution_time / 60} минут")


# sorted_time = dict(sorted())