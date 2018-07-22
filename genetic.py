import pyges
import random

file=pyges.get_param(input('Enter IGES filename: '))
gene_pool=pyges.get_points()

depth = float(input('Specify Depth of Cut of Tool(mm):\n'))
max_x = float(input('Specify Stock Width (x)(mm): \n'))
max_y = float(input('Specify Stock Length (y)(mm): \n'))

genes=[]
for el in gene_pool:
    counter=0
    while -1*max_x <= (el+(counter*depth)) <=max_x:
        genes.append(el+(counter*depth))
        counter+=1
for el in gene_pool:
    counter=0
    while -1*max_y <= (el+(counter*depth)) <=max_y:
        genes.append(el+(counter*depth))
        counter+=1
gene=sorted(set(genes))
print(gene)
