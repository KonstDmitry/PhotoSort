import ffmpeg
import sys
import pprint

img = '/Users/dmitry/Yandex.Disk.localized/Project/Other/Python/PhotoSort/For PhotoSort/Old/100F0090.MOV'

media_file = sys.argv[1]
# uses ffprobe command to extract all possible metadata from the media file
pprint(ffmpeg.probe(media_file)["streams"])