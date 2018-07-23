import pyges
import random

random.seed()

file=pyges.get_param(input('Enter IGES filename: '))
raw_points=pyges.get_points()

depth = float(input('Specify Depth of Cut of Tool(mm):\n'))
max_x = float(input('Specify Stock Width (x)(mm): \n'))
max_y = float(input('Specify Stock Length (y)(mm): \n'))

def init_genes():
    global g_codes
    global gene_pool
    global g_codes
    g_codes=['G00','G01','G02','G03']
    genes=[]
    for el in raw_points:
        counter=0
        while -1*max_x <= (el+(counter*depth)) <=max_x:
            genes.append(el+(counter*depth))
            counter+=1
    for el in raw_points:
        counter=0
        while -1*max_y <= (el+(counter*depth)) <=max_y:
            genes.append(el+(counter*depth))
            counter+=1
    gene_pool=sorted(set(genes))



class indiv:
    def __init__(self, length=0, codes=[]):
        self.length=length
        self.codes=codes
    def get_length(self):
        self.length=random.randint(1,100)

    def build_codes(self):
        for i in range(self.length):
            self.codes.append([g_codes[random.randint(0,3)]])
    def add_xy(self):
        for el in self.codes:
            for i in range(4):
                el.append(gene_pool[random.randint(0,len(gene_pool)-1)])

            '''fix this to add correct number of xy points and whatnot'''
init_genes()
one=indiv()
one.get_length()
one.build_codes()
one.add_xy()
output=open('out.txt', 'w+')
for i in one.codes:
    for el in i:
        output.write(str(el))
        output.write('  ')
    output.write('\n')
output.close()
