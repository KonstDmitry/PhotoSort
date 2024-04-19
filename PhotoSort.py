from exif import Image

with open('R0250038.JPG', 'rb') as image_file:
    my_image = Image(image_file)
    my_camera_model = my_image.model
    my_camera_lens = my_image.lens_model
    my_camera_lens_focal = my_image.lens_specification

print(my_image)
print(my_camera_model)
print(my_camera_lens)
print(my_camera_lens_focal)





