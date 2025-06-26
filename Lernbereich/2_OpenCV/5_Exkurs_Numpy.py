import numpy as np

# Ohne NumPy
liste = [[10, 20, 30], [40, 50, 60]]
for i in range(len(liste)):
    for j in range(len(liste[i])):
        liste[i][j] += 10

# Numpy ermöglicht Rechnungen mit größeren Zahlen UND ARRAYS! Nützlich für Bildverarbeitung (z.B. Helligkeit 0...255)
# Mit NumPy
array = np.array([[10, 20, 30], [40, 50, 60]])
print(array)

array += 10
print(array)

# Operationen mit NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print(c)
