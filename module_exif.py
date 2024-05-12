import os
import datetime
from exif import Image
from PIL import Image as pil_image

camera_model_list = []
file_weight_sum = 0

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
        img_by_exif_camera = img_by_exif_file.model.replace(' ', '')
        camera_list(img_by_exif_camera)
        file_weight_one = os.path.getsize(path_file) / (1024 * 1024)
        photo_weight(os.path.getsize(path_file))
        img_by_exif_date_time_str = img_by_exif_date
        img_by_exif_date_time_obj = datetime.datetime.strptime(img_by_exif_date_time_str,
                                                               '%Y:%m:%d %H:%M:%S')
        img_by_exif_date_time_obj_format = img_by_exif_date_time_obj.strftime('%y%m%d')
        return filename, img_by_exif_date_time_obj_format, img_by_exif_camera, file_weight_one
def photo_pil(path_file, filename):
    global file_weight_sum, camera_model_list
    img_by_pil_file = pil_image.open(path_file)
    img_by_pil_open = img_by_pil_file.getexif()
    img_by_pil_date = img_by_pil_open.get(306, None)
    img_by_pil_camera = str(img_by_pil_open.get(272, None).replace(' ', ''))
    camera_list(img_by_pil_camera)
    file_weight_one = os.path.getsize(path_file) / (1024 * 1024)
    photo_weight(os.path.getsize(path_file))
    img_by_pil_date_time_obj = datetime.datetime.strptime(img_by_pil_date,
                                                          '%Y:%m:%d %H:%M:%S')
    img_by_pil_date_time_obj_format = img_by_pil_date_time_obj.strftime('%y%m%d')
    return filename, img_by_pil_date_time_obj_format, img_by_pil_camera, file_weight_one

def path_create(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Папка {path} создана")

# def
# def photo_copy(path_file, folder_new):

