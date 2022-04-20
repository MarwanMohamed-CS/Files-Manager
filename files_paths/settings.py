import wmi
from pprint import pprint


def get_driver_component(driver_name='', driver_id=''):
    # DRIVE_TYPES = {
    # 0 : "Unknown",
    # 1 : "No Root Directory",
    # 2 : "Removable Disk",
    # 3 : "Local Disk",
    # 4 : "Network Drive",
    # 5 : "Compact Disc",
    # 6 : "RAM Disk"
    # }
    c = wmi.WMI()
    for drive in c.Win32_LogicalDisk():
        # prints all the drives details including name, type and size
        if driver_name and driver_name == drive.VolumeName:
            return drive.name
        if driver_id == drive.VolumeSerialNumber:
            return drive.name
        # print (drive.Name, drive.VolumeSerialNumber)
    return ''


def get_txts_info():
    '''resets the txt'''
    hdd_letter_2_tera = get_driver_component('My Passport(2)')
    hdd_letter_toshiba_2 = get_driver_component('Toshiba(2)')
    hdd_letter_1_tera = get_driver_component('My Passport(1)')
    toshiba_letter = get_driver_component(driver_id='03D08A60')
    txts = {'files_paths\\1_tera_animes.txt': {'clips path': hdd_letter_1_tera + 'Anime_1Tera',
                                               'dir tag': '1 tera animes',
                                               'file type': 'anime',
                                               'hard disk': '1 tera',
                                               'serial number': '1AEA6007'},
            'files_paths\\1_tera_courses.txt': {'clips path': hdd_letter_1_tera + 'Courses',
                                                'dir tag': '1 tera course',
                                                'file type': 'course',
                                                'hard disk': '1 tera',
                                                'serial number': '1AEA6007'},
            'files_paths\\1_tera_movies.txt': {'clips path': hdd_letter_1_tera + 'Movies_1Tera',
                                               'dir tag': '1 tera movies',
                                               'file type': 'movie',
                                               'hard disk': '1 tera',
                                               'serial number': '1AEA6007'},
            'files_paths\\1_tera_tv.txt': {'clips path': hdd_letter_1_tera + 'TV Series_1Tera',
                                           'dir tag': '1 tera tv',
                                           'file type': 'tv series',
                                           'hard disk': '1 tera',
                                           'serial number': '1AEA6007'},
            'files_paths\\2_tera_animes.txt': {'clips path': hdd_letter_2_tera + 'Anime_2Tera',
                                               'dir tag': '2 tera animes',
                                               'file type': 'anime',
                                               'hard disk': '2 tera',
                                               'serial number': '6C8E2E75'},
            'files_paths\\2_tera_movies.txt': {'clips path': hdd_letter_2_tera + 'Movies_2Tera',
                                               'dir tag': '2 tera movies',
                                               'file type': 'movie',
                                               'hard disk': '2 tera',
                                               'serial number': '6C8E2E75'},
            'files_paths\\2_tera_tv.txt': {'clips path': hdd_letter_2_tera + 'TV Series_2Tera',
                                           'dir tag': '2 tera tv',
                                           'file type': 'tv series',
                                           'hard disk': '2 tera',
                                           'serial number': '6C8E2E75'},
            'files_paths\\books.txt': {'clips path': 'E:\\Books',
                                       'dir tag': 'this pc books ',
                                       'file type': 'book',
                                       'hard disk': 'main',
                                       'serial number': 'B0193957'},
            'files_paths\\main hard_e_tv_series.txt': {'clips path': 'E:/TV Series',
                                                       'dir tag': 'this pc e',
                                                       'file type': 'tv series',
                                                       'hard disk': 'main',
                                                       'serial number': 'B0193957'},
            'files_paths\\main hard_f_animes.txt': {'clips path': 'F:\\Anime',
                                                    'dir tag': 'this pc f',
                                                    'file type': 'anime',
                                                    'hard disk': 'main',
                                                    'serial number': 'A653ADC9'},
            'files_paths\\main hard_f_tv_series.txt': {'clips path': 'F:/TV Series',
                                                       'dir tag': 'this pc f',
                                                       'file type': 'tv series',
                                                       'hard disk': 'main',
                                                       'serial number': 'A653ADC9'},
            'files_paths\\main_hard_courses_f.txt': {'clips path': 'F:\\Courses',
                                                     'dir tag': 'this pc courses',
                                                     'file type': 'course',
                                                     'hard disk': 'main',
                                                     'serial number': 'A653ADC9'},
            'files_paths\\main_hard_movies_e.txt': {'clips path': 'E:/Movies(2)',
                                                    'dir tag': 'this pc e',
                                                    'file type': 'movie',
                                                    'hard disk': 'main',
                                                    'serial number': 'B0193957', },
            'files_paths\\main_hard_e_courses.txt': {'clips path': 'E:/Courses',
                                                    'dir tag': 'this pc e',
                                                    'file type': 'course',
                                                    'hard disk': 'main',
                                                    'serial number': 'B0193957'},
            'files_paths\\main_hard_movies_f.txt': {'clips path': 'F:/Movies',
                                                    'dir tag': 'this pc f',
                                                    'file type': 'movie',
                                                    'hard disk': 'main',
                                                    'serial number': 'A653ADC9'},

            'files_paths\\toshiba_movies.txt': {'clips path': toshiba_letter + 'Movies',
                                                'dir tag': 'toshiba movies',
                                                'file type': 'movie',
                                                'hard disk': 'toshiba',
                                                'serial number': '03D08A60'},
            'files_paths\\toshiba_tv.txt': {'clips path': toshiba_letter + 'TV Series',
                                            'dir tag': 'toshiba tv',
                                            'file type': 'tv series',
                                            'hard disk': 'toshiba',
                                            'serial number': '03D08A60'}}
    return txts


# CONSTANTS
PRINTING_RESULTS_LIMIT = 200
EMPTY_SIZE = 1024**2 * 200  # means 200MB is the empty size of a folder
DESKTOP_PATH = r'C:\Users\COMPU1\Desktop'
TO_DELETE_TXT_PATH = r'files_paths\to_delete.txt'
RESULTS_LIMIT = 100
