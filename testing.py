import os
from files_paths import settings
import files_manipulation as fm



def read():
    '''reads trees of each path and returns a list containing
    the file objects '''
        txt_path = r''
        with open(path) as file_object:
            lines = file_object.read()
            lines = lines.split('\n')
            del lines[-1]
            for line in lines:
                file_path, file_size, file_details = line.split('|')
                if os.path.dirname(file_path) == details['clips path']:
                    surface = True
                else:
                    surface = False
                paths.append(fm.File(file_path,
                                     details['file type'],
                                     details['dir tag'],
                                     int(file_size),
                                     file_details,
                                     surface,
                                     details['hard disk'],
                                     ))
    return paths