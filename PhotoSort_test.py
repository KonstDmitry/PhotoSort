import os
import time
import module_exif
import module_pil

img_old_folder = (input(
    f"Введите начальный путь к папке:").rstrip()
                  or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/')
## or 'D:\test_duplicate\'
## '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/')
## '/Users/dmitry/Desktop/PhotoSort/Old/FUJI_203/SubFolder/'
img_new_folder = (input(
    f"Введите конечный путь к папке:").rstrip()
                  or '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/New/')

img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG','dng', 'jpg', 'jpeg'}

start_time = time.time()

for dirpath, dirnames, filenames in os.walk(img_old_folder):
    ## Обращаемся ко всем файлам в папках
    for filename in filenames:
        ## Узнаем общий длинный путь к файлу
        path_file = os.path.join(dirpath, filename)
        ## Ищем совпадение формата в названии файла
        if set(filename.split('.')) & img_format:
            try:
                file_data = module_exif.photo_exif(path_file, filename)
                print(file_data[0], file_data[1], file_data[2], file_data[3], 'EXIF')
            except:
                file_data = module_exif.photo_pil(path_file, filename)
                print(file_data[0], file_data[1], file_data[2], file_data[3], 'PIL')
print(module_exif.file_weight_sum)
print(module_exif.camera_model_list)

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд или {execution_time / 60} минут")
