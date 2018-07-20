import pyges
import random

pyges.get_file(input('Enter IGES filename: '))

gene_pool=pyges.get_points()
print(gene_pool)
print(len(gene_pool))
