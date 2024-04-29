import os
from PIL import Image as pil_image
from exif import Image

def new_path(img_new_folder):
    for dirpath, dirnames, filenames in os.walk(img_new_folder):
        for dirname in dirnames:
            dir_path = dirpath + dirname
            print(dir_path)
            for i in os.listdir(dir_path):
                try:
                    with open(dir_path + '/' + i, 'rb') as img_exif_file:
                        img_exif_file = Image(img_exif_file)
                        img_exif_model = img_exif_file.model
                        print(f"    {img_exif_model}")
                except:
                    try:
                        img_pil_file = pil_image.open(dir_path + '/' + i)
                        img_pil_exif = img_pil_file.getexif()
                        img_pil_model = str(img_pil_exif.get(272, None)).rstrip()
                        print(f"    {img_pil_model}")
                    except:
                        print('No')
                        continue

            # img_open = Image.open('../Photo/IMG_3394.CR2')
            # img_data = img_open.getdata()
            # img_info = img_open.format
            # img_pil_exif = img_open.getexif()
            # pprint.pprint(dict(img_pil_exif), width=1)
            # a = str(img_pil_exif.get(272, None)).rstrip()
            # b = img_pil_exif.get(306, None)
            # print(a, b)




            # for dirpath, dirnames, filenames in os.walk(img_new_folder):
    #     for filename in filenames:

    #         print(os.path.join(dirpath, filename))
# def subfolder(folder):
#     print(folder)
