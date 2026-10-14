import numpy as np

n = 2
A = np.zeros((n, n), dtype=float)
b = np.zeros(n, dtype=float)

print("Digite os coeficientes e os termos independentes:")

for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Coeficiente A[{i+1},{j+1}]: "))
    # Corrigido: b[i] deve ficar fora do laço do 'j', mas dentro do laço do 'i'
    b[i] = float(input(f"Termo independente b[{i+1}]: "))

print("\nMatriz dos coeficientes A:\n", A)
print("\nVetor dos termos independentes b:\n", b)
print("\nMatriz aumentada [A | b]:\n", np.column_stack((A, b)))

posto_A = np.linalg.matrix_rank(A)
posto_ampliada = np.linalg.matrix_rank(np.column_stack((A, b)))

print(f"\nPosto(A): {posto_A}")
print(f"Posto([A|b]): {posto_ampliada}")

if posto_A < posto_ampliada:
    print("\nSI: sistema impossível (sem solução).")
elif posto_A < n:
    print("\nSPI: sistema possível e indeterminado (infinitas soluções).")
else:
    solucao = np.linalg.solve(A, b)
    print("\nSPD: sistema possível e determinado.")
    print(f"Incógnitas (solução): {solucao}")
    print("Verificação A @ x =", A @ solucao)
