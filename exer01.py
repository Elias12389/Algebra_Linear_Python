import numpy as np

# ux = float(input("u(x): "))
# uy = float(input("u(y): "))
# uz = float(input("u(z): "))

# vx = float(input("v(x): "))
# vy = float(input("v(y): "))
# vz = float(input("v(z): "))

# u = np.array([ux, uy, uz])
# v = np.array([vx, vy, vz])

# resultado = u + v 

# print("u =", u)
# print("v =", v)
# print("u + v =", resultado)



u = np.array([
    float(input("u(x): ")),
    float(input("u(y): ")),
    float(input("u(z): "))
])

v = np.array([
    float(input("v(x): ")),
    float(input("v(y): ")),
    float(input("v(z): "))
])

print("u - v =", u - v)
print("v - u =", v - u)