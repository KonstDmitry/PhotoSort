from PIL import Image
import os


path_photo = '/Users/dmitry/Desktop/Ricoh'

# img_open = Image.open('0XT53409.JPG')
# img_size = img_open.size
# print(img_size)
# print(os.listdir())
# print(os.path.getsize('PhotoSort.py'))
# print(os.path.getctime('PhotoSort.py'))
# print('Текущая директория:', os.getcwd())

#Соэдание папки os.mkdir('Название папки')


# for i in range(1,5):
#     path_name = str(i)
#     os.mkdir(path_name)
def file_size (file):
    file_open = Image.open(file)
    file_size = file_open.size
    print(file_size)

file_size('IMG_3394.CR2')

lst = [1,2,3,4]
lst.append(6)
print(lst)
def photo_inspect():
    lst_img = []
    for i in range(len(os.listdir(path_photo))):
        file_name, file_extension = os.path.splitext(os.listdir(path_photo)[i])
        # file = str(os.listdir(path_photo)[i])
        # img_open = Image.open(file)
        # img_size = img_open.size
        # print(img_size)
        # image_open = Image.open(str(os.listdir(path_photo)[i]))
        lst_img.append(os.listdir(path_photo)[i])
        # print(element)
        # file_size(f'"{os.listdir(path_photo)[i]}"')
        # print(file_name, file_extension, end='%')
        img_open = Image.open('/Users/dmitry/Desktop/Ricoh/' + lst_img[i])
        img_size = img_open.size
        print(img_size)

photo_inspect()
