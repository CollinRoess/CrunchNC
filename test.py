import os

def get_file(file_name):
    file = open(os.path.abspath(file_name))
    global x
    x=[_[:65] for _ in file if _[72]=='P']

get_file('test.iges')
print(x)
