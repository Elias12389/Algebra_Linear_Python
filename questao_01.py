import numpy as np

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
sx = int(input("Digite o valor de SX: "))
sy = int(input("Digite o valor de SY: "))

A = np.array([
    [sx, 0],
    [0, sy]
])

V = np.array([
    [x],
    [y]
])

T = A @ V

print(f"\nPonto original {x},{y},{sx},{sy} \n")
print("Matriz de transformação: \n", A, f"\n {V}\n")
print("Ponto transformado: \n",T, "\n")