import argparse
from lib2to3.pgen2 import driver
import os
from argparse import ArgumentParser
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
    for txt_path, details in settings.get_txts_info().items():
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
    print(f'Updated : {main_root}')


def run_once():
    '''returns the args object'''
    parser = ArgumentParser()
    parser.add_argument(
        '-o', '--once', action='store_true', help='makes the script run once')
    args = parser.parse_args()
    return args.once



working_dir = r'F:\Coding\Scripts\Files Manager\files_paths'
os.chdir(working_dir)

parser = ArgumentParser()
parser.add_argument(
    '-o', '--once', action='store_true', help='makes the script run once')
args = parser.parse_args()

serials = {
    'EC6F4F5A':{'updated' : False, 'volume name' : 'C:'},
    '66E2D7AC':{'updated' : False, 'volume name' : 'D:'},
    'B0193957':{'updated' : False, 'volume name' : 'E:'},
    'A653ADC9':{'updated' : False, 'volume name' : 'F:'},
    '1AEA6007':{'updated' : False, 'volume name' : 'My Passport(1)'},
    '6C8E2E75':{'updated' : False, 'volume name' : 'My Passport(2):'},
    '03D08A60':{'updated' : False, 'volume name' : 'Toshiba(1)'},
}

update_statuses ={}
for serial in serials.keys():
    update_statuses[serial] = False

if not args.once:
    while False in update_statuses.values():
        for hdd_serial, hdd_details in serials.items():
            letter = settings.get_driver_component(driver_id= hdd_serial)
            # in here the letter acts as boolean to check exists
            txts_info = settings.get_txts_info() # if you remove then get letter is called again
            for txt_path, details in txts_info.items():
                if details['serial number'] == hdd_serial:
                    if os.path.exists(details['clips path']) and not update_statuses[hdd_serial]:
                        for txt_path, details in txts_info.items():
                            if os.path.exists(details['clips path']):
                                update(details['clips path'], txt_path)
                        update_statuses[hdd_serial] = True
        sleep(1)
else:
    for txt_path, details in settings.get_txts_info().items():
        if os.path.exists(details['clips path']):
            update(details['clips path'], txt_path)

    # hello this is test branch
