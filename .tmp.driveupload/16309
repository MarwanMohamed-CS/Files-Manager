import shutil
import sys, os, traceback

def isUserAdmin():
    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print ("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError

import sys
import ctypes

def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True
        
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print ('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None
    

if __name__ == '__main__':
    ret = run_as_admin()
    if ret is True:
        print ('I have admin privilege.')
    elif ret is None:
        print ('I am elevating to admin privilege.')
    else:
        print ('Error(ret=%d): cannot elevate privilege.' % (ret, ))

import os




import pyperclip
import shutil
paths = pyperclip.paste()
paths = paths.split('\n')

for path in paths:
    path = path.strip()
    input(path.strip())
    if os.path.isdir(path):
        for file in os.listdir(path):
            print(os.path.join(path, file))
            os.remove(os.path.join(path, file))
            input()
    else:
        os.remove(path)