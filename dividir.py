import pandas as pd
import numpy as np

# Carregando o arquivo CSV
data = pd.read_csv('casos_obitos_doencas_preexistentes.csv')

# Definindo o número de partes em que o arquivo será dividido
num_parts = 15

# Dividindo o arquivo em partes
divided_data = np.array_split(data, num_parts)

# Salvando cada parte em um novo arquivo CSV
for i, part in enumerate(divided_data):
    part.to_csv(f'parte_{i}.csv', index=False)
