## Переименование префикса файла
def namematch(camera_name, camera_models):
    if not camera_models:
        img_prefix = ''
        if camera_name == 'X-T5':
            img_prefix = '0XT5'
        if camera_name == 'X-T2':
            img_prefix = '0XT2'
        if camera_name == 'X100F':
            img_prefix = '100F'
        if camera_name == 'X-S10':
            img_prefix = 'XS10'
        if camera_name == 'X-T30':
            img_prefix = 'XT30'
        return img_prefix