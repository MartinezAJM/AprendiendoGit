# Forma de importar 1 -> import example 
# Forma de importar 2 -> from example import words, script2, script3 o *
from example import words 

from addition import suma
from substract import resta
from multiplication import multiplicacion
from division import division

# Proyecto para practicar ramas

"""
Comentario
multilinea en python
"""

"""
Python tiene como buena práctica identar bloques de códigos -stagments- declaracion """

"""
Para ejecutar un script de python 

1. Tener un archivo .py
2. Poner el comando python archivo.py
"""

print("Basic Operation")

# Forma de llamar un arreglo con la forma 1 print(example.words)
print(words)

# Adition Operation
print(f"Resultado de suma: {suma(15,12)}")

# Rest Operation
print(f"Resultado de resta: {resta(10,8)}")

# Multiplication Operation
print(f"Resultado de multiplicación: {multiplicacion(3,5)}")

# Division Operation
print(f"Resultado de division: {division(60,9)}")