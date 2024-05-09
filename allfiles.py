import os

img_folder = (input(
    f"Введите начальный путь к папке:").rstrip())

file_result = open(f"{img_folder}file_result.txt", "a")

for dirpath, dirnames, filenames in os.walk(img_folder):  # Обращаемся ко всем файлам в папках
    for filename in filenames:
        path_file = os.path.join(dirpath, filename)
        file_result.write(f"{path_file}" + "\n")