## Переименование префикса файла
def namematch(camera_name):
    if camera_name == 'X-T5':
        img_prefix = '0XT5'
        return img_prefix
    if camera_name == 'X-T2':
        img_prefix = '0XT2'
        return img_prefix
    if camera_name == 'X100F':
        img_prefix = '100F'
        return img_prefix
    if camera_name == 'X-S10':
        img_prefix = 'XS10'
        return img_prefix
    if camera_name == 'X-T30':
        img_prefix = 'XT30'
        return img_prefix
    if camera_name == 'CanonPowerShotG9':
        img_prefix = 'CPSG9'
        return img_prefix
    if camera_name == 'GRII':
        img_prefix = 'R025'
        return img_prefix
    else:
        img_prefix = str(camera_name)
    return img_prefix
