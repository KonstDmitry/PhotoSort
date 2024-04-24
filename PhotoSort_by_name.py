import os
import time

start_time = time.time()

img_path = input(f"Введите путь к папке:").rstrip() or 'Photo/'
img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG'}

file_count = 0
img_count = 0
other_count = 0

for file in os.listdir(img_path):
    file_count += 1
    if set(file.split('.')) & img_format:
        img_count += 1
        print(f"{file}: Yes")
    else:
        other_count += 1
        print(f"{file}: No")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")

print(f"Количество всех файлов: {file_count}")
print(f"Количество отобранный файлов: {img_count}")
print(f"Количество исключенных файлов: {other_count}")