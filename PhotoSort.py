from PIL import Image as PILImage
import string

img_file = 'Photo/IMG_3394.CR2'
def clean_string(s):
    # Оставляем только печатаемые символы
    printable = set(string.printable)
    return "".join(filter(lambda x: x in printable, s))

# Открытие изображения и получение EXIF-данных
with open(img_file, 'rb') as image_file:
    img = PILImage.open(image_file)
    exif_data = img.getexif()

# Функция для декодирования тегов EXIF (если Pillow не декодирует их автоматически)
def get_exif_data(exif_data, tag):
    for t in exif_data:
        decoded = PILImage.ExifTags.TAGS.get(t, t)
        if decoded == tag:
            return exif_data[t]
    return None

# Получение и очистка данных модели камеры и объектива
camera_model = get_exif_data(exif_data, "Model")
lens_model = get_exif_data(exif_data, "LensModel")
lens_specification = get_exif_data(exif_data, "LensSpecification")

if camera_model is not None:
    clean_camera_model = clean_string(camera_model)
else:
    clean_camera_model = "Model not available"

if lens_model is not None:
    clean_lens_model = clean_string(lens_model)
else:
    clean_lens_model = "Lens model not available"

print(f"Camera Model: {clean_camera_model}")
print(f"Lens Model: {clean_lens_model}")
print(f"Lens Specification: {lens_specification}")

print(img.size)