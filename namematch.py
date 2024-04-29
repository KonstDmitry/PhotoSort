def namematch(camera_name):
    if camera_name == 'X-T5'.lower():
        img_prefix = '0XT5'
    if camera_name == 'X-T2'.lower():
        img_prefix = '0XT2'
    if camera_name == 'X100F'.lower():
        img_prefix = '100F'
    if camera_name == 'X-S10'.lower():
        img_prefix = 'XS10'
    if camera_name == 'X-T30'.lower():
        img_prefix = 'XT30'
        print(img_prefix)
    print(img_prefix)