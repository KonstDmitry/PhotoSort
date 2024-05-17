import os
import datetime
import shutil
from exif import Image
from PIL import Image as pil_image

camera_model_list = []
count_double = 0
file_weight_sum = 0
file_exif_count = 0
file_pil_count = 0

def name_match(camera_name):
    if camera_name == 'X-T5':
        img_prefix = '0XT5'
        return img_prefix
    if camera_name == 'X-T2':
        img_prefix = '0XT2'
        return img_prefix
    if camera_name == 'X100F':
        img_prefix = '100F'
        return img_prefix
    if camera_name == 'X-S10':
        img_prefix = 'XS10'
        return img_prefix
    if camera_name == 'X-T30':
        img_prefix = 'XT30'
        return img_prefix
    if camera_name == 'CanonPowerShotG9':
        img_prefix = 'CPSG9'
        return img_prefix
    if camera_name == 'GRII':
        img_prefix = 'R025'
        return img_prefix
    else:
        img_prefix = str(camera_name)
    return img_prefix

def camera_list(camera_model):
    global camera_model_list
    if camera_model not in camera_model_list:
        camera_model_list.append(camera_model)

def img_weight(weight):
    global file_weight_sum
    file_weight_sum += (weight / (1024 * 1024))
    return file_weight_sum

def photo_exif(path_file, file_name):
    global file_weight_sum, camera_model_list
    file_dict = {}
    with open(path_file, 'rb') as img_file_exif:
        img_by_exif_file = Image(img_file_exif)
        img_by_exif_date = img_by_exif_file.datetime
        img_date_time_obj = datetime.datetime.strptime(img_by_exif_date,
                                                               '%Y:%m:%d %H:%M:%S')
        file_dict['file_name'] = file_name
        file_dict['date'] = img_date_time_obj.strftime('%y%m%d')
        file_dict['time'] = img_date_time_obj.strftime('%H:%M:%S')
        file_dict['camera'] = img_by_exif_file.model.replace(' ', '')
        file_dict['weight'] = os.path.getsize(path_file) / (1024 * 1024)

        camera_list(file_dict['camera'])
        img_weight(file_dict['weight'])

        return file_dict
def photo_pil(path_file, file_name):
    file_dict = {}
    global file_weight_sum, camera_model_list
    img_by_pil_file = pil_image.open(path_file)
    img_by_pil_open = img_by_pil_file.getexif()
    img_by_pil_date = img_by_pil_open.get(306, None)
    img_date_time_obj = datetime.datetime.strptime(img_by_pil_date,
                                                          '%Y:%m:%d %H:%M:%S')

    file_dict['file_name'] = file_name
    file_dict['date'] = img_date_time_obj.strftime('%y%m%d')
    file_dict['time'] = img_date_time_obj.strftime('%H:%M:%S')
    file_dict['camera'] = str(img_by_pil_open.get(272, None).replace(' ', ''))
    file_dict['weight'] = os.path.getsize(path_file) / (1024 * 1024)

    camera_list(file_dict['camera'])
    img_weight(file_dict['weight'])

    return file_dict

def file_rename(img_new_folder, img_date, filename, camera):
    try:
        os.rename(f"{img_new_folder}{img_date}/{filename}",
                  f"{img_new_folder}{img_date}/{name_match(camera)}{filename[4:]}")
    except:
        print(f"{img_new_folder}{img_date}/{filename} невозможно переименовать")
        print(img_new_folder, img_date, filename, camera)
        # shutil.copy2(file_path, f"{img_new_folder}00_Other/")


def path_create(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Папка {path} создана")

def path_other(img_new_folder):
    if not os.path.exists(f"{img_new_folder}00_Other/"):
        os.mkdir(f"{img_new_folder}00_Other/")
        print(f"Папка {img_new_folder}00_Other создана")

def path_copy(img_new_folder):
    if not os.path.exists(f"{img_new_folder}00_Copy/"):
        os.mkdir(f"{img_new_folder}00_Copy/")
        print(f"Папка {img_new_folder}00_Copy создана")

def file_copy(file_path, img_new_folder, filename, file_date):
    global count_double
    if not os.path.exists(f"{img_new_folder}{filename}/{file_date}"):
        shutil.copy2(f"{file_path}", f"{img_new_folder}{filename}")
    else:
        print(f"{file_path} copy")
        count_double += 1
        shutil.copy2(f"{file_path}", f"{img_new_folder}00_Copy/{file_path.split('\\')[1]}")
        file_name_extension = f"{file_path.split('\\')[1]}"
        file_name= f"{file_path.split('\\')[1][:file_path.split('\\')[1].find('.')]}"
        file_extension = f"{file_path.split('\\')[1][file_path.split('\\')[1].find('.'):]}"
        os.rename(f"{img_new_folder}00_Copy/{file_name_extension}",
                  f"{img_new_folder}00_Copy/{file_name}_copy{file_extension}")
        shutil.move(f"{img_new_folder}00_Copy/{file_name}_copy{file_extension}",
                    f"{img_new_folder}{filename}/{file_name}_copy{file_extension}")
