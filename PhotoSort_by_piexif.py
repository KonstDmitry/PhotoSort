import piexif

exif_dict = piexif.load("Photo/R0250136.DNG")
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

exif_dict = piexif.load("Photo/R0250136.DNG")
