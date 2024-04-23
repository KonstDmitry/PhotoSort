from exif import Image

with open('100F6732.RAF', 'rb') as image_file:
    my_image = Image(image_file)
    my_camera_model = my_image.model
    my_camera_lens = my_image.lens_model
    my_camera_lens_focal = my_image.lens_specification
    my_camera_date = my_image.datetime
    my_camera_date_original = my_image.datetime_original

print(my_camera_model)
print(my_camera_lens)
print(my_camera_lens_focal)
print(my_camera_date)
print(my_camera_date_original)