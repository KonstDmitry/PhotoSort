import exifread

# Open image file for reading (must be in binary mode)
f = open('../Photo/100F2426.RAF', 'rb')
print(f)

# Return Exif tags
tags = exifread.process_file(f)
print(tags)