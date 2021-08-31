import os
import datetime
import settings
from time import sleep


def calc_size(paths, sizes):
    '''
    calculates size of each path and modifies it inside of size list
    '''
    net_sizes = sizes[:]
    for net_paths_index, net_path in enumerate(paths):
        for net_paths_iterator_index, net_path_iterator in enumerate(paths[net_paths_index+1:]):
            if net_path in net_path_iterator:
                sizes[net_paths_index] += net_sizes[net_paths_index +
                                                    net_paths_iterator_index]
            else:
                break


def generate_txt(**kwargs):
    '''
    generates txt file with format: path|size|epock_creation_date
    requires txt_path, sizes, paths, file_details(just for printing nothing else)
    '''
    txt_path = kwargs['txt_path'].split('\\')[1]  # get correct relative path
    with open(txt_path, 'w') as file_object:
        for path, size, file_detail in zip(kwargs['paths'], kwargs['sizes'], kwargs['file_details']):
            file_object.write(f'{path}|{size}|{file_detail}\n')
        print(f'Updated {kwargs["details"]["clips path"]}')
    # if removed the .txt is going to be overwrriten even if path doesn't exist


def update():
    '''
    Writes to a collections of .txts the trees of files and folders inside
    specific dirs
    '''
    for txt_path, details in settings.txts.items():
        if not os.path.exists(details['clips path']):
            continue
        paths = []
        sizes = []
        file_details = []
        for root, dirs, files in os.walk(details['clips path']):
            paths.append(root)
            sizes.append(os.path.getsize(paths[-1]))
            file_details.append(os.path.getctime(root))
            for f in files:
                paths.append(f'{root}{os.sep}{f}')
                try:
                    sizes.append(os.path.getsize(paths[-1]))
                    file_details.append(os.path.getctime(f'{root}{os.sep}{f}'))
                except Exception:
                    with open('errors.txt', 'a+') as file_obj:
                        file_obj.write(f'{Exception}\n')
        calc_size(paths, sizes)
        # if 'course' in txt_path:
        #     for size, file_detail in zip(sizes,file_details):
        #         print(size, file_detail)
        generate_txt(paths=paths,
                     sizes=sizes,
                     details = details,
                     file_details=file_details,
                     txt_path= txt_path)
    


###Main###
update()
updated_1_tera = False
updated_2_tera = False
while True:
    while True:
        if os.path.exists(settings.dir_name_1_tera) and os.path.exists(settings.dir_name_2_tera):
            path = 'Both'
            updated_1_tera = True
            updated_2_tera = True
            break
        elif os.path.exists(settings.dir_name_2_tera) and updated_2_tera == False:
            print('2 tera')
            path = 'H:/ (2 Tera)'
            updated_2_tera = True
            break
        elif os.path.exists(settings.dir_name_1_tera) and updated_1_tera == False:
            print('1 tera')
            path = 'G:/ (1 tera)'
            updated_1_tera = True
            break
        else:
            sleep(1)
    update()  # remember that it updates everything
    with open('update.txt', 'a') as file_object:
        file_object.write(f'{datetime.datetime.now()}  updated: {path}\n')
    if updated_1_tera == True and updated_2_tera == True:
        exit()
