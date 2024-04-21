import os

path_photo = '/Users/dmitry/Desktop/Old'

print(os.listdir())
print(os.path.getsize('PhotoSort.py'))
print(os.path.getctime('PhotoSort.py'))
print('Текущая директория:', os.getcwd())

#Соэдание папки os.mkdir('Название папки')


# for i in range(1,5):
#     path_name = str(i)
#     os.mkdir(path_name)

# print(os.listdir('/Users/dmitry/Desktop/Ricoh'), end='\n')

for i in range(len(os.listdir(path_photo))):
    print(os.listdir(path_photo)[i])

