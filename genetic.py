import pyges
import random
import pickle

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
    unrounded_gene_pool=sorted(set(genes))
    gene_pool=[]
    for i in unrounded_gene_pool:
        gene_pool.append(round(i, 4))



class indiv:
    def __init__(self):
        self.length=0
        self.codes=[]
    def get_length(self):
        self.length=random.randint(1,100)

    def build_codes(self):
        for i in range(self.length):
            self.codes.append([g_codes[random.randint(0,3)]])
    def add_xy(self):
        for el in self.codes:
            if el[0]=="G00" or el[0]=="G01":
                for i in range(4):
                    el.append(gene_pool[random.randint(0,len(gene_pool)-1)])
            elif el[0]=="G02" or el[0]=="G03":
                for i in range(5):
                    el.append(gene_pool[random.randint(0,len(gene_pool)-1)])

'''fix this'''
def create(output_file):
    x=indiv()
    x.get_length()
    x.build_codes()
    x.add_xy()
    output=open(output_file, 'w+')
    for i in x.codes:
        for el in i:
            output.write(str(el))
            output.write('  ')
        output.write('\n')
    output.close()


init_genes()
for i in range(2):
    create(str(hash(i))+'.txt')

"""TODO:

1) Figure out how to score this mother.
2) Create individuals AND MAKE SURE G CODE PATHS ARE CONTINUOUS (i.e the end
point of the first code is the start point of the next, etc.)

3) Selection and Mutationself.
4) A boatload of JS that makes everything look cool
5) ??? AWS connection
6) Profit

'''one=indiv()
one.get_length()
one.build_codes()
one.add_xy()
output=open('out.txt', 'w+')
for i in one.codes:
    for el in i:
        output.write(str(el))
        output.write('  ')
    output.write('\n')
output.close()'''
