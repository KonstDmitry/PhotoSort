import os
import datetime
from PIL import Image as pil_image

camera_model_list = []
file_weight_sum = 0

def camera_list(camera_model):
    global camera_model_list
    # if not camera_model_list:
    camera_model_list.append(camera_model)

def photo_weight(weight):
    global file_weight_sum
    file_weight_sum += weight
    return file_weight_sum
def photo_pil(path_file, filename):
    global file_weight_sum, camera_model_list
    img_by_pil_file = pil_image.open(path_file)
    img_by_pil_open = img_by_pil_file.getexif()
    img_by_pil_date = img_by_pil_open.get(306, None)
    img_by_pil_camera = str(img_by_pil_open.get(272, None).replace(' ', ''))
    camera_list(img_by_pil_camera)
    file_weight_one = os.path.getsize(path_file) / (1024 * 1024)
    file_weight_sum += os.path.getsize(path_file) / (1024 * 1024)
    photo_weight(os.path.getsize(path_file)) / (1024 * 1024)
    # print(f"{filename} {img_by_pil_date} {img_by_pil_camera} (by PIL)")
    img_by_pli_date = img_by_pil_open.get(36867)
    img_by_pil_date_time_obj = datetime.datetime.strptime(img_by_pli_date,
                                                          '%Y:%m:%d %H:%M:%S')
    img_by_pil_date_time_obj_format = img_by_pil_date_time_obj.strftime('%y%m%d')
    return filename, img_by_pil_date, img_by_pil_camera, file_weight_one