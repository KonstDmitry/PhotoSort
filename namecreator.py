import os
def new_path(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            print(os.path.join(dirpath, filename))

def subfolder(folders):
    for folder in folders:
        print(folder)