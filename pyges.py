"""
I know this looks like it was written by a toddler.
Maybe it was. Anyway pipe down. I'll fix it.
"""
import os

def get_file(file_name):
    file = open(os.path.abspath(file_name))
    global x
    x=[]
    for line in file:
        if line[72]=='P':
            x.append(line[:65])

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
            xyz.append(int(item))
        except ValueError:
            try:
                xyz.append(float(item))
            except ValueError:
                pass
    return(sorted(xyz))
