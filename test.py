from exif import Image
from PIL import Image as pil_image
import rawpy


a = open(f"D:/test_copy/problems/20190518_152702.dng", 'rb')
print(a)


b = rawpy.imread(f"D:/test_copy/problems/20190518_152702.dng")
print(open(a))

with open(f"D:/test_copy/problems/20190518_152702.dng", 'rb') as img_file_exif:
    img_by_exif_file = Image(img_file_exif)
    print(img_by_exif_file)

img_by_pil_file = pil_image.open(a)
img_by_pil_open = img_by_pil_file.getexif()


# path = 'image.nef'
# with rawpy.imread(path) as raw:
#     rgb = raw.postprocess()
