# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
from  http.server import SimpleHTTPRequestHandler
'''

# timeit statement
print (timeit.timeit(setup = mysetup,
					stmt = mycode,
					number = 10000))
