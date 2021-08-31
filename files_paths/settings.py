import os
import shutil


dir_name_2_tera = 'H'  # dir_name_2_tera + ':'
dir_name_1_tera = 'G'
dir_name_toshiba = 'I'
possible_names = ['G:', 'I:', 'H:']
# ext_harddrives = {'1 tera': {'size': 1000169533440},
#                   '2 tera': {'size': 2000363188224}
#                   }

# for harddrive_name, details in ext_harddrives.items():
#     for possible_name in possible_names:
#         if os.path.exists(possible_name):
#             possible_name_size = shutil.disk_usage(possible_name)
#             if details['size'] == possible_name_size:
#                  ext_harddrives[possible_name][]
txts = {
    'files_paths\\main_hard_courses.txt':  # 2 tera animes # filetype_harddisk
    {'dir tag': 'this pc courses',
     'clips path': dir_name_toshiba + ':' + '/Movies',
     'file type': 'course',
     'hard disk': 'main'},
    'files_paths\\toshiba_movies.txt':  # 2 tera animes # filetype_harddisk
    {'dir tag': 'toshiba movies',
     'clips path': dir_name_toshiba + ':' + '/Movies',
     'file type': 'movie',
     'hard disk': 'toshiba'},
    'files_paths\\toshiba_tv.txt':  # 2 tera animes
    {'dir tag': 'toshiba tv',
     'clips path': dir_name_toshiba + ':' + '/TV Series',
     'file type': 'tv series',
     'hard disk': 'toshiba'},
    'files_paths\\2_tera_animes_tree.txt':  # 2 tera animes
    {'dir tag': '2 tera animes',
     'clips path': dir_name_2_tera + ':' + '/Anime_2Tera',
     'file type': 'anime',
     'hard disk': '2 tera'},
    'files_paths\\2_tera_movies_tree.txt':  # 2 tera movies
    {'dir tag': '2 tera movies',
     'clips path': dir_name_2_tera + ':' + '/Movies_2Tera',
     'file type': 'movie',
     'hard disk': '2 tera'},
    'files_paths\\2_tera_tv_tree.txt':  # 2 tera tv
    {'dir tag': '2 tera tv',
     'clips path': dir_name_2_tera + ':' + '/TV Series_2Tera',  # G:\TV Series_2Tera
     'file type': 'tv series',
     'hard disk': '2 tera'},
    'files_paths\\main_hard_movies_f_tree.txt':  # main hard movies f
    {'dir tag':    'this pc f',
     'clips path': 'F:/Movies',
     'file type':    'movie',
     'hard disk': 'main'},
    'files_paths\\main hard_f_tv_series_tree.txt':  # main hard tv series f
    {'dir tag': 'this pc f',
     'clips path': 'F:/TV Series',
     'file type': 'tv series',
     'hard disk': 'main'},
    'files_paths\\main_hard_movies_e_tree.txt':  # main hard movies e
    {'dir tag': 'this pc e',
     'clips path': 'E:/Movies(2)',
     'file type': 'movie',
     'hard disk': 'main'},
    'files_paths\\main hard_e_tv_series_tree.txt':  # main hard tv series e
    {'dir tag': 'this pc e',
     'clips path': 'E:/TV Series',
     'file type': 'tv series',
     'hard disk': 'main'},
    'files_paths\\1_tera_animes_tree.txt':  # 1 tera animes
    {'dir tag': '1 tera animes',
     'clips path': dir_name_1_tera + ':' + '/Anime_1Tera',
     'file type': 'anime',
     'hard disk': '1 tera'},
    'files_paths\\1_tera_courses.txt':  # 2 tera animes # filetype_harddisk
    {'dir tag': '1 tera courses',
     'clips path': dir_name_1_tera + ':' + '/Courses',
     'file type': 'course',
     'hard disk': '1 tera'},
    'files_paths\\1_tera_movies_tree.txt':  # 1 tera movies
    {'dir tag': '1 tera movies',
     'clips path': dir_name_1_tera + ':' + '/Movies_1Tera',
     'file type': 'movie',
     'hard disk': '1 tera'},
    'files_paths\\1_tera_tv_tree.txt':  # 1 tera tv
    {'dir tag': '1 tera tv',
     'clips path': dir_name_1_tera + ':' + '/TV Series_1Tera',
     'file type': 'tv series',
     'hard disk': '1 tera'}, }


RESULTS_LIMIT = 200
