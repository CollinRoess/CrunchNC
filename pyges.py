"""
I know this looks like it was written by a toddler.
Maybe it was. Anyway pipe down. I'll fix it.
"""
import os
'''getting only lines of file where parametric data is present
    column 73='P'
'''
def get_param(file_name):
    file = open(os.path.abspath(file_name), 'r')
    lines = file.readlines()
    global x
    x = []
    for i in lines:
        if i[72]=='P':
            x.append(i[:65])


def get_points():
    y=[]
    pointlist=[]
    for item in x:
        item=item.split(';')
        y.append(item[0])
    for item in y:
        pointlist.append(item.strip('\'').split(','))

    '''[x.strip('\'') for x in pointlist]'''
    true_pointlist=[]
    for item in pointlist:
        for i in item:
            true_pointlist.append(i)

    c=[]
    xyz=[]
    for item in set(true_pointlist):
        c.append(item)
    for item in c:
        try:
            _=int(item)
        except ValueError:
            try:
                xyz.append(float(item))
            except ValueError:
                pass
    return(sorted(xyz))
