
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

d = {
     indexes[0]: erros
     }

df = pd.DataFrame(d)

df.to_excel("tabela_%s.xlsx"%fname[:-4], index=False)

df.describe().to_excel("tabela_%s_describe.xlsx"%fname[:-4], index=False)
