import os
from PIL import Image as pil_image
from exif import Image
import namematch

def new_path(img_new_folder):
    for dirpath, dirnames, filenames in os.walk(img_new_folder):
        for dirname in dirnames:
            dir_path = dirpath + dirname
            print(dir_path)
            for img_object in os.listdir(dir_path):
                try:
                    with open(f"{dir_path}/{img_object}", 'rb') as img_exif_file:
                        img_exif_file = Image(img_exif_file)
                        print(f"{dir_path}/{img_object}")
                        img_exif_model = img_exif_file.model
                        os.renames(f"{dir_path}/{img_object}", f"{dir_path}/{namematch.namematch(img_exif_model)}{img_object[4:]}")
                        print(f"    {img_exif_model}")
                except:
                    try:
                        img_pil_file = pil_image.open(dir_path + '/' + img_object)
                        img_pil_exif = img_pil_file.getexif()
                        img_pil_model = str(img_pil_exif.get(272, None)).rstrip()
                        os.renames(f"{dir_path}/{img_object}", f"{dir_path}/{namematch.namematch(img_pil_model)}{img_object[4:]}")
                        print(f"    {img_pil_model}")
                    except:
                        continue
                    print('No')
            print(dir_path)