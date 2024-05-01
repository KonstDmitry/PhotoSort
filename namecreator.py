import os
from PIL import Image as pil_image
from exif import Image
import namematch


# def dict_test(dict_img):
#     print(dict_img)
#
# dict_test()

camera_list_rename = ['0XT5', 'X100F', '0XT2', 'XS10', 'PRO1']

def new_path(img_new_folder):
    for dirpath, dirnames, filenames in os.walk(img_new_folder):
        for dirname in dirnames:
            dir_path = dirpath + dirname
            counter = 0
            for img_object_name in os.listdir(dir_path):
                counter += 1
                # print(img_object_name)
                # print(f"Old name {dir_path}/{img_object_name}")
                # if img_object_name[-4] in camera_list_rename:
                #     print('hg')
                #     os.renames(f"{dir_path}/{img_object_name}",
                #                f"{dir_path}/test{img_object_name[3]}{str(counter).zfill(4)}{img_object_name[-4:]}")
                #     print(f"New name {dir_path}/{img_object_name}")
                # try:
                with open(f"{dir_path}/{img_object_name}", 'rb') as img_exif_file_origin:
                    img_exif_file = Image(img_exif_file_origin)
                    print(img_exif_file)
                    print(f"Old name {dir_path}/{img_object_name}")
                    # img_exif_camera_model = img_exif_file.model
                #     counter += 1
                #     os.renames(f"{dir_path}/{img_object_name}",
                #                f"{dir_path}/111{img_object_name}")
                #     print(f"New name {dir_path}/{img_object_name}")
                # except:
                #     try:
                #         img_pil_file = pil_image.open(dir_path + '/' + img_object_name)
                #         img_pil_exif = img_pil_file.getexif()
                #         # img_pil_model = str(img_pil_exif.get(272, None)).rstrip()
                #         print(f"Old name {dir_path}/{img_object_name}")
                #         os.renames(f"{dir_path}/{img_object_name}",
                #                    f"{dir_path}/222{img_object_name}")
                #         print(f"New name {dir_path}/{img_object_name}")
                #     except:
                #         continue
