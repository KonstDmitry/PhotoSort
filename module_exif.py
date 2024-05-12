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

def namematch(camera_name):
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

def photo_weight(weight):
    global file_weight_sum
    file_weight_sum += (weight / (1024 * 1024))
    return file_weight_sum

def photo_exif(path_file, filename):
    global file_weight_sum, camera_model_list
    with open(path_file, 'rb') as img_file_exif:
        img_by_exif_file = Image(img_file_exif)
        img_by_exif_date = img_by_exif_file.datetime
        camera = img_by_exif_file.model.replace(' ', '')
        camera_list(camera)
        file_weight_one = os.path.getsize(path_file) / (1024 * 1024)
        photo_weight(os.path.getsize(path_file))
        img_by_exif_date_time_str = img_by_exif_date
        img_by_exif_date_time_obj = datetime.datetime.strptime(img_by_exif_date_time_str,
                                                               '%Y:%m:%d %H:%M:%S')
        img_by_exif_date_time_obj_format = img_by_exif_date_time_obj.strftime('%y%m%d')
        return filename, img_by_exif_date_time_obj_format, camera, file_weight_one
def photo_pil(path_file, filename):
    global file_weight_sum, camera_model_list
    img_by_pil_file = pil_image.open(path_file)
    img_by_pil_open = img_by_pil_file.getexif()
    img_by_pil_date = img_by_pil_open.get(306, None)
    camera = str(img_by_pil_open.get(272, None).replace(' ', ''))
    camera_list(camera)
    file_weight_one = os.path.getsize(path_file) / (1024 * 1024)
    photo_weight(os.path.getsize(path_file))
    img_by_pil_date_time_obj = datetime.datetime.strptime(img_by_pil_date,
                                                          '%Y:%m:%d %H:%M:%S')
    img_by_pil_date_time_obj_format = img_by_pil_date_time_obj.strftime('%y%m%d')
    return filename, img_by_pil_date_time_obj_format, camera, file_weight_one

def file_rename(img_new_folder, img_by_exif_date_time_obj_format, filename, camera):
    try:
        os.rename(f"{img_new_folder}{img_by_exif_date_time_obj_format}/{filename}",
                  f"{img_new_folder}{img_by_exif_date_time_obj_format}/{namematch(camera)}{filename[4:]}")
    except:
        print('no')

def path_create(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Папка {path} создана")

def path_other(img_new_folder):
    if not os.path.exists(f"{img_new_folder}00_Other/"):
        os.mkdir(f"{img_new_folder}00_Other/")
        print(f"Папка {img_new_folder}00_Other создана")

def file_copy(path_file, img_new_folder, filename, file_date):
    global count_double
    if not os.path.exists(f'{img_new_folder}{filename}/{file_date}'):
        shutil.copy2(path_file, img_new_folder + filename)
    else:
        print(f"{path_file} copy")
        count_double += 1
        shutil.copy2(f'{path_file}', f'{img_new_folder}/00_Other')



# def txt_report(img_new_folder):
#     file_other = open(f"{img_new_folder}00_Other/file_other.txt", "a")
#     file_exif = open(f"{img_new_folder}file_exif.txt", "a")
#     file_pil = open(f"{img_new_folder}file_PIL.txt", "a")
#     return file_other, file_exif, file_pil


