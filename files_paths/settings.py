import wmi


def get_driver_letter(driver_name):
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
        if driver_name == drive.VolumeName:
            return drive.name
        # print (drive.Name, drive.VolumeSerialNumber)
    return ''


def get_txts_info():
    '''resets the txt'''
    hdd_letter_2_tera = get_driver_letter('My Passport(2)')
    hdd_letter_toshiba_2 = get_driver_letter('Toshiba(2)')
    hdd_letter_1_tera = get_driver_letter('My Passport(1)')
    txts = {}
    # toshiba
    txts[r'files_paths\toshiba_movies.txt'] = {'dir tag': 'toshiba movies',
                                               'clips path': hdd_letter_toshiba_2 + 'Movies',
                                               'file type': 'movie',
                                               'hard disk': 'toshiba'}

    txts[r'files_paths\toshiba_tv.txt'] = {'dir tag': 'toshiba tv',
                                           'clips path': hdd_letter_toshiba_2 + 'TV Series',
                                           'file type': 'tv series',
                                           'hard disk': 'toshiba'}
    # 2 tera
    txts[r'files_paths\2_tera_animes.txt'] = {'dir tag': '2 tera animes',
                                              'clips path': hdd_letter_2_tera + 'Anime_2Tera',
                                              'file type': 'anime',
                                              'hard disk': '2 tera'}

    txts[r'files_paths\2_tera_movies.txt'] = {'dir tag': '2 tera movies',
                                              'clips path': hdd_letter_2_tera + 'Movies_2Tera',
                                              'file type': 'movie',
                                              'hard disk': '2 tera'}

    txts[r'files_paths\2_tera_tv.txt'] = {'dir tag': '2 tera tv',
                                          'clips path': hdd_letter_2_tera + 'TV Series_2Tera',
                                          'file type': 'tv series',
                                          'hard disk': '2 tera'}
    # main hard
    txts[r'files_paths\main_hard_movies_f.txt'] = {'dir tag':    'this pc f',
                                                   'clips path': 'F:/Movies',
                                                   'file type':    'movie',
                                                   'hard disk': 'main'}

    txts[r'files_paths\main hard_f_tv_series.txt'] = {'dir tag': 'this pc f',
                                                      'clips path': 'F:/TV Series',
                                                      'file type': 'tv series',
                                                      'hard disk': 'main'}

    txts[r'files_paths\main_hard_movies_e.txt'] = {'dir tag': 'this pc e',
                                                   'clips path': 'E:/Movies(2)',
                                                   'file type': 'movie',
                                                   'hard disk': 'main'}

    txts[r'files_paths\main hard_e_tv_series.txt'] = {'dir tag': 'this pc e',
                                                      'clips path': 'E:/TV Series',
                                                      'file type': 'tv series',
                                                      'hard disk': 'main'}

    txts[r'files_paths\main_hard_courses_f.txt'] = {'dir tag': 'this pc courses',
                                                    'clips path': 'F:\Courses',
                                                    'file type': 'course',
                                                    'hard disk': 'main'}

    txts[r'files_paths\main hard_f_animes.txt'] = {'dir tag': 'this pc f',
                                                   'clips path': 'F:\Anime',
                                                   'file type': 'anime',
                                                   'hard disk': 'main'}
    # 1 tera
    txts[r'files_paths\1_tera_animes.txt'] = {'dir tag': '1 tera animes',
                                              'clips path': hdd_letter_1_tera + 'Anime_1Tera',
                                              'file type': 'anime',
                                              'hard disk': '1 tera'}

    txts[r'files_paths\1_tera_courses.txt'] = {'dir tag': '1 tera courses',
                                               'clips path': hdd_letter_1_tera + 'Courses',
                                               'file type': 'course',
                                               'hard disk': '1 tera'}

    txts[r'files_paths\1_tera_movies.txt'] = {'dir tag': '1 tera movies',
                                              'clips path': hdd_letter_1_tera + 'Movies_1Tera',
                                              'file type': 'movie',
                                              'hard disk': '1 tera'}

    txts[r'files_paths\1_tera_tv.txt'] = {'dir tag': '1 tera tv',
                                          'clips path': hdd_letter_1_tera + 'TV Series_1Tera',
                                          'file type': 'tv series',
                                          'hard disk': '1 tera'}

    txts[r'files_paths\books.txt'] = {'dir tag': 'this pc books ',
                                      'clips path': r'E:\Books',
                                      'file type': 'book',
                                      'hard disk': 'main'}
    return txts


# CONSTANTS
PRINTING_RESULTS_LIMIT = 200
EMPTY_SIZE = 1024**2 * 200  # means 200MB is the empty size of a folder
DESKTOP_PATH = r'C:\Users\COMPU1\Desktop'
TO_DELETE_TXT_PATH = r'files_paths\to_delete.txt'

RESULTS_LIMIT = 100

1
