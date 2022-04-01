import os
import shutil
import win32api


def get_hdd_letter(hdd_name):
    '''returns hdd letter according to hd name passed'''
    wanted_drive_letter = ''
    drives_letters = [
        x for x in win32api.GetLogicalDriveStrings().split('\00') if x]  # sometimes x is empty str that's why the if is there
    for drive_letter in drives_letters:
        if hdd_name == win32api.GetVolumeInformation(drive_letter)[0]:
            wanted_drive_letter = drive_letter
    return wanted_drive_letter


def get_txt():
    '''resets the txt'''
    hdd_letter_2_tera = get_hdd_letter('My Passport(2)')
    hdd_letter_toshiba_1 = get_hdd_letter('Toshiba(1)')
    hdd_letter_toshiba_2 = get_hdd_letter('Toshiba(2)')
    hdd_letter_1_tera = get_hdd_letter('My Passport(1)')
    txts = {
        'files_paths\\toshiba_movies.txt':  # 2 tera animes # filetype_harddisk
        {'dir tag': 'toshiba movies',
         'clips path': hdd_letter_toshiba_2 + '/Movies',
         'file type': 'movie',
         'hard disk': 'toshiba'},
        'files_paths\\toshiba_tv.txt':  # 2 tera animes
        {'dir tag': 'toshiba tv',
         'clips path': hdd_letter_toshiba_2 + '/TV Series',
         'file type': 'tv series',
         'hard disk': 'toshiba'},
        'files_paths\\2_tera_animes.txt':  # 2 tera animes
        {'dir tag': '2 tera animes',
         'clips path': hdd_letter_2_tera + '/Anime_2Tera',
         'file type': 'anime',
         'hard disk': '2 tera'},
        'files_paths\\2_tera_movies.txt':  # 2 tera movies
        {'dir tag': '2 tera movies',
         'clips path': hdd_letter_2_tera + '/Movies_2Tera',
         'file type': 'movie',
         'hard disk': '2 tera'},
        'files_paths\\2_tera_tv.txt':  # 2 tera tv
        {'dir tag': '2 tera tv',
         'clips path': hdd_letter_2_tera + '/TV Series_2Tera',  # G:\TV Series_2Tera
         'file type': 'tv series',
         'hard disk': '2 tera'},
        'files_paths\\main_hard_movies_f.txt':  # main hard movies f
        {'dir tag':    'this pc f',
         'clips path': 'F:/Movies',
         'file type':    'movie',
         'hard disk': 'main'},
        'files_paths\\main hard_f_tv_series.txt':  # main hard tv series f
        {'dir tag': 'this pc f',
         'clips path': 'F:/TV Series',
         'file type': 'tv series',
         'hard disk': 'main'},
        'files_paths\\main_hard_movies_e.txt':  # main hard movies e
        {'dir tag': 'this pc e',
         'clips path': 'E:/Movies(2)',
         'file type': 'movie',
         'hard disk': 'main'},
        'files_paths\\main hard_e_tv_series.txt':  # main hard tv series e
        {'dir tag': 'this pc e',
         'clips path': 'E:/TV Series',
         'file type': 'tv series',
         'hard disk': 'main'},
        'files_paths\\main_hard_courses_f.txt':  # main hard courses f
        {'dir tag': 'this pc courses',
         'clips path': 'F:\Courses',
         'file type': 'course',
         'hard disk': 'main'},
        'files_paths\\main hard_f_animes.txt':  # main hard tv series e
        {'dir tag': 'this pc f',
        'clips path': 'F:\Anime',
        'file type': 'anime',
        'hard disk': 'main'},
        'files_paths\\1_tera_animes.txt':  # 1 tera animes
        {'dir tag': '1 tera animes',
         'clips path': hdd_letter_1_tera + '/Anime_1Tera',
         'file type': 'anime',
         'hard disk': '1 tera'},
        'files_paths\\1_tera_courses.txt':  # 2 tera animes # filetype_harddisk
        {'dir tag': '1 tera courses',
         'clips path': hdd_letter_1_tera + '/Courses',
         'file type': 'course',
         'hard disk': '1 tera'},
        'files_paths\\1_tera_movies.txt':  # 1 tera movies
        {'dir tag': '1 tera movies',
         'clips path': hdd_letter_1_tera + '/Movies_1Tera',
         'file type': 'movie',
         'hard disk': '1 tera'},
        'files_paths\\1_tera_tv.txt':  # 1 tera tv
        {'dir tag': '1 tera tv',
         'clips path': hdd_letter_1_tera + '/TV Series_1Tera',
         'file type': 'tv series',
         'hard disk': '1 tera'}, }
    return txts


# CONSTANTS
PRINTING_RESULTS_LIMIT = 200
EMPTY_SIZE = 1024**2 * 200  # means 200MB is the empty size of a folder
DESKTOP_PATH = r'C:\Users\COMPU1\Desktop'
TO_DELETE_TXT_PATH = r'files_paths\\to_delete.txt'


txts = get_txt()