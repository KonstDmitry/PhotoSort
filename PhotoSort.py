from PIL import Image
from PIL.ExifTags import TAGS

# путь к изображению или видео
imagename = "0XT53409.jpg"
# читать данные изображения с помощью PIL
image = Image.open(imagename)
# извлечь данные EXIF
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # получить имя тега вместо идентификатора
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # декодировать байты
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")