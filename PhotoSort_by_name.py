import os
import time

start_time = time.time()

img_path = input(f"Введите путь к папке:").rstrip() or 'Photo/'
img_format = {'RAW', 'RAF', 'CR2', 'JPG', 'DNG'}

for file in os.listdir(img_path):
    if set(file.split('.')) & img_format:
        print(f"{file}: Yes")
    else:
        print(f"{file}: No")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")