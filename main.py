import colorama
import os
import re
from send2trash import send2trash
from time import sleep
from guessit import guessit
from FilesManager import FilesManager
from files_paths import settings


def update():
    '''
    Writes to a collections of .txts the trees of files and folders inside
    specific dirs
    '''
    def calc_size(paths, sizes):
        '''Calculates the real size of each path directly changing sizes list'''
        net_sizes = sizes[:]
        for index, path_outer in enumerate(paths):
            for path_inner in paths[index:]:
                if path_outer in path_inner:
                    for hooked_index, path_inner_2 in enumerate(paths[index:]):
                        if path_outer == path_inner_2:
                            continue
                        if path_outer in path_inner_2:
                            sizes[index] += net_sizes[hooked_index+index]
                        else:
                            break
                    break

    txts = settings.txts
    CURR_DIR = os.getcwd()
    for txt, details in txts.items():
        if not os.path.exists(details['clips path']):
            continue
        paths = []
        sizes = []
        file_details = []
        txt_path = f'{CURR_DIR}{os.sep}{txt}'
        for root, dirs, files in os.walk(details['clips path']):
            paths.append(root)
            sizes.append(os.path.getsize(paths[-1]))
            file_details.append(os.path.getctime(root))
            for f in files:
                paths.append(f'{root}{os.sep}{f}')
                try:
                    sizes.append(os.path.getsize(paths[-1]))
                    file_details.append(os.path.getctime(f'{root}{os.sep}{f}'))
                except FileNotFoundError:
                    with open('errors.txt', 'a') as file_obj:
                        file_obj.write(f'{Exception}\n')
        calc_size(paths, sizes)
        try:
            with open(txt_path, 'w') as file_object:
                for path, size, file_detail in zip(paths, sizes, file_details):
                    file_object.write(f'{path}|{size}|{file_detail}\n')
                print(f'Updated {details["clips path"]}')
        except:
            pass
    # if removed the .txt is going to be overwrriten even if path doesn't exist


def gen_rars_dups_txt(paths):
    def get_rars_dups(paths):
        rars_dirs = fm.get_rars_dirs(paths)
        to_del_clips_paths = {}
        counter = 0
        for rars_dir, count in rars_dirs.items():
            if count >= 7:
                for path in paths:
                    counter += 1
                    ext = os.path.splitext(path.path)[1]
                    if rars_dir == os.path.dirname(path.path) and (ext == '.mkv' or ext == '.mp4'):
                        to_del_clips_paths[path] = count
                        break
        return to_del_clips_paths

    # the next can be easily changed to suite any use
    to_del_clips_paths = get_rars_dups(paths)
    size = 0
    with open("new.txt", "w") as file_obj:
        for to_del_clip_path, count in to_del_clips_paths.items():
            size += to_del_clip_path.size
            ind_size = fm.to_unit(to_del_clip_path.size, object=True)
            # ans = input(f'want to del: {to_del_clip_path.path}  \n(y/n)?')
            file_obj.write(to_del_clip_path.path + ' ' + str(ind_size.value)
                           + ' ' + ind_size.unit + ' ' + str(count) + '\n')
    input(fm.to_unit(size))  # size of everything


def get_path_dir_ind(paths, file_index):
    '''
    returns index of the dir path in the paths list of the file path 
    passed'''
    dir_path = os.path.dirname(paths[file_index])
    up_index = 0
    for path in paths[file_index::-1]:
        if path.path == dir_path:
            return file_index - up_index
        up_index += 1


def get_rars_dirs(paths):
    '''
    
    '''
    pass


def main():
    os.system('cls')
    print('loading...')
    fm = FilesManager()
    
    paths = fm.read()

    while True:
        os.system('cls')
        inp = input(f'{colorama.Fore.GREEN}Name: {colorama.Fore.WHITE}')
        if not inp:
            continue
        net_inp, cmd = fm.parse_inp(inp)
        results = []
        if not cmd:  # normal search
            results = fm.search(paths, net_inp)
            fm.print_results(results)
        elif cmd['type'] == 'cmd':
            if cmd['func name'] == 'print_duplicates':
                dups = fm.get_duplicates(paths)
                fm.print_results(dups, dups=True)
            elif cmd['func name'] == 'get_clips':
                results = fm.get_clips(paths, cmd)
                fm.print_results(results)
            elif cmd['func name'] == 'update':
                os.system(r'python "F:\Coding\Scripts\Files Manager\files_paths\Update.pyw"')
            elif cmd['func name'] == 'get_stats':
                file_types = fm.get_stats(cmd, paths)
                fm.print_stats(file_types)
        elif cmd['type'] == 'dir tag':
            results = fm.search(paths, net_inp, cmd['dir tag'])
            fm.print_results(results)
        end_cmd = input(colorama.Fore.WHITE)

        if 'open' in end_cmd:
            open_file(results, end_cmd)
        elif 'tree' in end_cmd:
            tree = fm.get_tree(paths, results, end_cmd)
            fm.print_tree(tree)
        elif 'export' in end_cmd:
            fm.create_pdf(results,
                          inp=end_cmd)
        elif end_cmd == 'clean':
            fm.clean()
        elif 'del' in end_cmd:
            root = fm.get_root(results, end_cmd)
            if root:  # root is False if path was never extracted
                fm.delete(root.path)


if __name__ == '__main__':
    main()
