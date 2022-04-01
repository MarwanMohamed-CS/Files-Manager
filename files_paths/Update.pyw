import os
from time import sleep
import settings


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

def update_all():
    for txt_path, details in settings.get_txt().items():
        if os.path.exists(details['clips path']):
            update(details['clips path'], txt_path)


def generate_txt(txt_path, paths, sizes, ctimes):
    '''
    generates txt file with format: path|size|epock_creation_date
    requires txt_path, sizes, paths, file_details(just for printing nothing else)
    '''
    with open(txt_path, 'w') as file_object:
        for path, size, ctime in zip(paths, sizes, ctimes):
            try:
                file_object.write(f'{path}|{size}|{ctime}\n')
            except Exception as E:
                pass
        hdd_letter = os.path.splitdrive(path[0])[1]
        print(f'Updated {hdd_letter}:\\')


def update(main_root, txt_path):
    '''
    Writes to a collections of .txts the trees of files and folders inside
    specific dirs
    '''
    paths = []
    sizes = []
    ctimes = []
    for root, dirs, files in os.walk(main_root):
        paths.append(root)
        sizes.append(os.path.getsize(paths[-1]))
        ctimes.append(os.path.getctime(root))
        for f in files:
            paths.append(os.path.join(root, f))
            try:
                sizes.append(os.path.getsize(paths[-1]))
                ctimes.append(os.path.getctime(os.path.join(root, f)))
            except Exception as E:
                with open('errors.txt', 'a+') as file_obj:
                    file_obj.write(f'{E}\n')
    calc_size(paths, sizes)
    rel_txt_path = os.path.basename(txt_path)
    generate_txt(paths=paths,
                 sizes=sizes,
                 ctimes=ctimes,
                 txt_path=rel_txt_path)




def main():
    for txt_path, details in settings.get_txt().items():
        if os.path.exists(details['clips path']):
            update(details['clips path'], txt_path)

    hdds = {
        'My Passport(1)': False,
        'My Passport(2)': False,
        'Toshiba(1)': False,
        'Toshiba(2)': False,
    }
    while False in hdds.values():
        for hdd_name, update_status in hdds.items():
            if os.path.exists(settings.get_hdd_letter(hdd_name)) and not update_status:
                hdds[hdd_name] = True
                for txt_path, details in settings.get_txt().items():
                    if os.path.exists(details['clips path']):
                        update(details['clips path'], txt_path)

        sleep(1)


if __name__ == '__main__':
    # hello this is test branch
    os.chdir('F:\Coding\Scripts\Files Manager\files_paths')
    main() 