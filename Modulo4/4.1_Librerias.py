#Importar una biblioteca completa:
import math
resultado = math.sqrt(16)

#Importar un módulo completa:
from math import sqrt
resultado = sqrt(16)

# renombrar una biblioteca completa:
import pandas as pd #para instalar se usa pip install pandas
data = {'Nombre':('Juan','Segio','Luis'),'Edades':(20,23,21)}
df = pd.DataFrame(data)
print(df)

#Ejemplo 2
import numpy as np
array = np.array([1 , 2, 3, 4, 5])
print(array)

import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.ylabel("Algunos Números")
plt.show()



