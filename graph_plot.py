
import numpy as np
import pandas as pd

def process_data(file):
    file = file.split('\n')
    
    indexes = file[1]
    
    file = file[2:]
    
    indexes = indexes.split()
    indexes = indexes[:-2]
    
    for i in range(len(file)):
        file[i] = np.float32(file[i].split())
        
    return indexes, file

def select_data(data, indice):
    _temp = []
    
    for i in range(len(data)):
        _temp.append(data[i][indice])
    
    return _temp

import glob
fnames = glob.glob('./data/*.txt')
erros = []
for fname in fnames:
    with open(fname, 'r') as f:
        file = f.read()
    indexes, data = process_data(file)

    erros.append(select_data(data, 3))
    
import matplotlib.pyplot as plt

for i in range(len(erros)):
    x = np.arange(0, len(erros[i]))
    plt.plot(x, erros[i], label="Erro %s"%(fnames[i][9:-4]))

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Título")
plt.legend()
plt.show()
