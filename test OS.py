import os

print(os.listdir())
print(os.path.getsize('PhotoSort.py'))
print(os.path.getctime('PhotoSort.py'))
print('Текущая директория:', os.getcwd())

#Соэдание папки os.mkdir('Название папки')


# for i in range(1,5):
#     path_name = str(i)
#     os.mkdir(path_name)
for i in range (2):
    os.makedirs('Папка для тестирования/Old')