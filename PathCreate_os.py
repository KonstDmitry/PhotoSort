import os

path_photo = ('/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old')
# path_photo = 'Photo'

files = os.listdir(path_photo)

count = 0

for dirpath, dirnames, filenames in os.walk(path_photo):
    for filename in filenames:
        path_file = os.path.join(dirpath, filename)
        count += 1
        print("Файл:", path_file)
print(count)

print(files)