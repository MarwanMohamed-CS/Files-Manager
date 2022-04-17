import os
import collections
import re
import colorama
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


class FilesManager():
    '''
    '''
    def __init__(self):
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