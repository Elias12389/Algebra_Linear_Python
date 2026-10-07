import numpy as np

print("\nDigite os dados da matriz A (2 x 2)")
A = np.array([
    [float(input("A[1,1]: ")), float(input("A[1,2] "))],
    [float(input("A[2,1]]: ")), float(input("A[2,2]: "))]
])

print("\nDigite os dados da matriz B (2 x 1)")
B = np.array([
    [float(input("B[1,1]: "))], 
    [float(input("B[2,1]: "))]
])

print("\nDimensão de A: ", A.shape)
print("Dimensão de B: ", B.shape)

if A.shape[1] == B.shape[0]:
    C = A @ B
    print("A . B =\n", C)
else:
    print("As dimensões são incompatíveis para multuplicação")