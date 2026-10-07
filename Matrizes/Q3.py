import numpy as np

print("Digite os dados da matriz de produção A (2 x 2): ")

A = np.array([
    [float(input("A[1,1]: ")), float(input("A[1,2]: "))],[float(input("A[2,1]: ")), float(input("A[2,2]: "))]
])
# Não é mais preciso fazer um for para que a percorrer uma matriz e aplicar em todos os elementos
k = float(input("Digite o fator de reajuste k (ex: 1.20): "))

B = k * A
diferenca = B - A

print("\nProdução original =\n", A)
print("Produçaõ reajustada =\n", B)
print("Diferença (B - A) =\n", diferenca)