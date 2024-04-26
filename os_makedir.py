import piexif

exif_dict = piexif.load("Photo/0XT53408(1).RAW")
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

