import os
import collections
import re
import colorama
from importlib_metadata import files
import prettytable
import shutil
import datetime
import stat
from time import sleep
from docx import Document
from docx.shared import Inches, Cm, RGBColor
from docx2pdf import convert
from docx.enum.text import WD_ALIGN_PARAGRAPH
from guessit import guessit
from files_paths import settings


class File():
    '''Carries info of a file and has file management methods'''

    def __init__(self, path, file_type, dir_tag='', size=0, epoch_creation_date=0, surface=False, hard_disk='',):
        self.name = os.path.basename(path)
        self.path = path
        self.dir_tag = dir_tag
        self.file_type = file_type
        self.size = size
        self.surface = surface
        self.hard_disk = hard_disk
        self.epoch_creation_date = epoch_creation_date

    def get_size(self):
        '''returns size(int or float) of file and unit(str) of that size'''
        # size is in bytes
        # 10^3 > KB
        # 10^6 > MB
        if self.size < 10**6:  # converts bytes to KBs
            size = self.size/1024
            unit = 'KB'
            size = int(size)
        elif self.size < 10**9:  # converts bytes to MBs
            # 1048576 is 1024 * 1024
            size = self.size//1_048_576
            unit = 'MB'
        else:  # if size>10^9 converts to GBs
            # 1073741824 is 1024 * 1024 * 1024
            size = self.size/1_073_741_824
            size = round(size, 1)  # rounds to a total of 4 digits
            unit = 'GB'
        if int(size) == 0:
            size = 0
        return size, unit

    def set_index(self, index):
        '''
        sets index for the file so that we can choose it for operations like opening,
        printing tree...etc
        '''
        self.index = index

    def get_creation_date(self):
        '''
        returns a nametuple with the date and the time of the day of the creation of the file
        '''
        datetime_time = datetime.datetime.fromtimestamp(
            float(self.epoch_creation_date))
        datetime_time = str(datetime_time)
        formated_date_in_days, formated_date_in_hm = datetime_time.split(
            ' ')   # hm stands for hours/mins
        #date_formater = collections.namedtuple('creation_date', 'date time')
        return formated_date_in_days, formated_date_in_hm


class HardDisk():
    def __init__(self, serial_number) :
        self.serial_number  = serial_number
        
    def add_dir(self, dirs_path, files_type, dir_tag):
        '''
        Adds dir and some specifications, dirs_path is a list
        '''
        self.dirs_path = dirs_path # is a list
        self.files_type = files_type
        self.dir_tag = dir_tag

    def tree_scan_dir(self):
        for dir_path in self.dirs_path:
            

class FilesManager():
    '''
    '''

    def __init__(self,):
        self.paths = self.read()

    def read():
        '''reads trees of each path and returns a list containing
        the file objects '''
        paths = []
        CURR_DIR = os.getcwd()
        for path, details in settings.get_txts_info().items():
            path = f'{CURR_DIR}/{path}'
            if not os.path.exists(path):
                continue
            with open(path) as file_object:
                lines = file_object.read()
                lines = lines.split('\n')
                del lines[-1]
                surface_path = lines[0].split('|')[0]
                for line in lines:
                    file_path, file_size, file_details = line.split('|')
                    if os.path.dirname(file_path) == surface_path:
                        surface = True
                    else:
                        surface = False
                    paths.append(File(file_path,
                                      details['file type'],
                                      details['dir tag'],
                                      int(file_size),
                                      file_details,
                                      surface,
                                      details['hard disk'],
                                      )
                                 )
        return paths

    def open_file(results, end_cmd):
        '''takes in a File object instance and opens it's directory and the file itself'''
        error = True
        num_match = re.search(r'open(\s\d{1,})?', end_cmd)
        if num_match:
            try:
                num = num_match.group().split()[1]
                num = int(num)
            except:
                num = 1

        for result in results:
            if result.index == num - 1:
                clip = result
                break
        if os.path.exists(clip.path):
            if os.path.isdir(clip.path):  # clips is a folder
                for file_name in os.listdir(clip.path):
                    match = re.search(r'^(?!.*trailer).+(mkv|avi|mp4)$',
                                      file_name,
                                      re.DOTALL | re.I)
                    if match:
                        clip_path = f'{clip.path}/{match.group()}'
                        os.startfile(clip.path)
                        sleep(0.5)
                        os.startfile(clip_path)
                        input(colorama.Fore.LIGHTBLUE_EX +
                              'The file was opened successfuly. Yay man you are awesome.')
                        error = False
                        break
                if error == True:  # opens folder if no video file was found
                    os.startfile(clip.path)
                    error = False
            else:  # if clip is a file
                os.startfile(clip.path)
                error = False
        else:
            print('\n\t\t\t\t***The directory you are trying to access is unavailable')
            sleep(4.5)

        if error:  # if clip wasn't found in folder
            print('''\n\t\t\t\t***An unexpected error occured. It may be because the file
            is compressed.***''')
            sleep(4.5)

    def get_paths(self):
        return self.paths

    def get_cmd(self, inp):
        '''
        returns a dictionary containing the properties corresponding to the inp passed
        '''
        def assign_prop(cmd, cmd_tag):
            '''assigns the properties to the cmd dictionary depedning on the cmd_tag given'''
            if cmd_tag == '-dups':  # to change what function catches as commands
                cmd['func name'] = 'print_duplicates'
            elif cmd_tag == '-all movies':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'movie'
                cmd['hard disk'] = []
            elif cmd_tag == '-all tv':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'tv series'
            elif cmd_tag == '-all animes':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'anime'
            elif cmd_tag == '-pc e':
                cmd['func name'] = 'get_clips'
                cmd['dir tag'] = 'this pc e'
            elif cmd_tag == '-pc f':
                cmd['func name'] = 'get_clips'
                cmd['dir tag'] = 'this pc f'
            elif cmd_tag == '-pc tv':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'tv series'
                cmd['dir tag'] = 'this pc'
            elif cmd_tag == '-pc movies':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'movie'
                cmd['dir tag'] = 'this pc'
            elif cmd_tag == '-2 tera movies':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'movie'
                cmd['dir tag'] = '2 tera movies'
            elif cmd_tag == '-2 tera tv':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'tv series'
                cmd['dir tag'] = '2 tera tv'
            elif cmd_tag == '-2 tera animes':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'anime'
                cmd['dir tag'] = '2 tera animes'
            elif cmd_tag == '-1 tera movies':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'movie'
                cmd['dir tag'] = '1 tera movies'
            elif cmd_tag == '-1 tera tv':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'tv series'
                cmd['dir tag'] = '1 tera tv'
            elif cmd_tag == '-1 tera animes':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'anime'
                cmd['dir tag'] = '1 tera animes'
            elif cmd_tag == '-u' or cmd_tag == '-update':
                cmd['func name'] = 'update'
            elif cmd_tag == '-new':
                cmd['func name'] = 'get_clips'
                cmd['file type'] = 'new'
        match = re.search('-.*', inp)
        cmd = {}
        if match:
            cmd_tag = match.group()
            net_inp = inp.replace(cmd_tag, '')
        else:
            return inp, cmd
        assign_prop(cmd, cmd_tag)
        return net_inp, cmd

    def get_dir_tag(inp):
        '''returns directory tag(if exists) and input line without the tag in it'''
        match = re.search(r'''^         ((this \s pc (\s(e|f))? (?=\s))
                            # this pc followed by e or f opt.,followed by space(not consumed)
                                                            |
                                    ((1|2) \s tera (\s (movies|tv|animes) )? (?=\s)))''',
                          # 1|2 tera followed by movies tv or animes(opt.) followed by space(not consumed)
                          inp,
                          re.VERBOSE | re.I)
        if match:
            dir_tag = match.group()
            to_replace = dir_tag+' '  # because dir_tag doesn't have the space in it
            net_inp = inp.replace(to_replace, '')
        else:
            dir_tag = None
            net_inp = inp
        return net_inp, dir_tag


class Dir():
    
    def __init__(self, dir_path, files_type, dir_tag):
        self.dir_path = dir_path
        self.files_type = files_type
        self.dir_tag = dir_tag

    def read_dir():
        self.txt_path = self.files_type + '_' + os.path.basename(dir_path)
        if not os.path.exists(self.dir_path):
            return None
        with open(self.dir_path) as file_obj:
            lines = file_obj.readlines()
        for line in lines:
            line.split('||')
        with open(dir_path) as file_object:
            lines = file_object.read()
            lines = lines.split('\n')
            del lines[-1]
            surface_path = lines[0].split('|')[0]
            for line in lines:
                file_path, file_size, file_details = line.split('|')
                if os.path.dirname(file_path) == surface_path:
                    surface = True
                else:
                    surface = False


    def dump_data():


def read():
    '''reads trees of each path and returns a list containing
    the file objects '''
    paths = []
    CURR_DIR = os.getcwd()
    for path, details in settings.get_txts_info().items():
        path = f'{CURR_DIR}/{path}'
        if not os.path.exists(path):
            continue
        with open(path) as file_object:
            lines = file_object.read()
            lines = lines.split('\n')
            del lines[-1]
            surface_path = lines[0].split('|')[0]
            for line in lines:
                file_path, file_size, file_details = line.split('|')
                if os.path.dirname(file_path) == surface_path:
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
                                     )
                             )
    return paths
