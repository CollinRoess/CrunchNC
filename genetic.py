import pyges
import random

file=pyges.get_param(input('Enter IGES filename: '))
raw_points=pyges.get_points()

depth = float(input('Specify Depth of Cut of Tool(mm):\n'))
max_x = float(input('Specify Stock Width (x)(mm): \n'))
max_y = float(input('Specify Stock Length (y)(mm): \n'))

def init_genes():
    global g_codes
    global gene_pool
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
    print(gene_pool)

init_genes()
