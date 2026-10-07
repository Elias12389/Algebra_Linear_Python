import numpy as np

print("\nDigite os dados da matriz B (2 x 2)")
A = np.array([
    [float(input("A11: ")), float(input("A12: "))],
    [float(input("A21: ")), float(input("A22: "))]
])

print("\nDigite os dados da matriz B (2 x 2)")
B = np.array([
    [float(input("B[1,1]: ")), float(input("B[1,2]: "))], 
    [float(input("B[2,1]: ")), float(input("B[2,2]: "))]
])

C = A + B

print("\nA = \n", A)
print("B =\n", B)
print("Dimensão de A: ", A.shape)
print("Dimensão de B: ", B.shape)
print("Total recebido (A + B) =\n", C)