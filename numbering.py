import os
from exif import Image

def name_sort(img_new_folder):
    for dirpath, dirnames, filenames in os.walk(img_new_folder):
        for dirname in dirnames:
            dir_path = dirpath + dirname
            print(f'{dir_path}')
            for filename in filenames:
                print(f"{filename}")
