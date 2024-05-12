import os
import time
import module_exif
import module_pil
import shutil

img_old_folder = (input(
    f"Введите начальный путь к папке:").rstrip()
                  # or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/')
                  or 'D:/test_copy/')
## or 'D:\test_duplicate\'
## '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/')
## '/Users/dmitry/Desktop/PhotoSort/Old/FUJI_203/SubFolder/'
img_new_folder = (input(
    f"Введите конечный путь к папке:").rstrip()
                  or 'D:/test_copy_new/')

img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG','dng', 'jpg', 'jpeg'}
count_double = 0
file_count = 0
img_count = 0
file_exif_count = 0
file_pil_count = 0
file_other_count = 0

module_exif.path_other(img_new_folder)

file_other = open(f"{img_new_folder}00_Other/file_other.txt", "a")
file_exif = open(f"{img_new_folder}file_exif.txt", "a")
file_pil = open(f"{img_new_folder}file_pil.txt", "a")

start_time = time.time()

for dirpath, dirnames, filenames in os.walk(img_old_folder):
    ## Обращаемся ко всем файлам в папках
    for filename in filenames:
        ## Узнаем общий длинный путь к файлу
        path_file = os.path.join(dirpath, filename)
        file_count += 1
        ## Ищем совпадение формата в названии файла
        if set(filename.split('.')) & img_format:
            img_count += 1
            try:
                ## Пытаемся вытянуть значения через exif
                file_exif_count += 1
                # print(f'{path_file}')
                file_data = module_exif.photo_exif(path_file, filename)
                module_exif.path_create(f'{img_new_folder}{file_data[1]}')
                module_exif.file_copy(path_file, img_new_folder, file_data[1], file_data[0])
                file_exif.write(f"{path_file}" + '\n')
                # print(file_data[0], file_data[1], file_data[2], file_data[3], 'EXIF')
            except:
                ## Пытаемся вытянуть значения через PIL
                try:
                    file_pil_count += 1
                    # print(f'{path_file}')
                    file_data = module_exif.photo_pil(path_file, filename)
                    module_exif.path_create(f'{img_new_folder}{file_data[1]}')
                    module_exif.file_copy(path_file, img_new_folder, file_data[1], file_data[0])
                    file_pil.write(f"{path_file}" + '\n')
                    # print(file_data[0], file_data[1], file_data[2], file_data[3], 'PIL')
                except:
                    ## Если и через PIL не получается, кидаем в другие
                    file_other_count += 1
                    shutil.copy2(path_file, f"{img_new_folder}00_Other/")
                    file_other.write(f"{path_file}" + '\n')


print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранных файлов: {img_count}")
print(f"Количество через библоиотеку exif: {file_exif_count}")
print(f"Количество через библоиотеку PIL: {file_pil_count}")
print(f"Количество исключенных файлов: {file_other_count}")
print(f"Общий вес всех фотографий: {module_exif.file_weight_sum}")
print(f"Список уникальных моделей камеры: {module_exif.camera_model_list} и их количество - {len(module_exif.camera_model_list)}")
print(f'Общее кол-во дибликатов: {module_exif.count_double}')

end_time = time.time()
execution_time = end_time - start_time

print(f"Время выполнения программы: {execution_time} секунд или {execution_time / 60} минут")
