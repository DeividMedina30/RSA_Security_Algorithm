
import math


def validarPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if (numero % i) == 0:
            return False
    return True


def leerValoresPrimos():
    bandera = False
    while (bandera != True):
        x = int(input("Ingrese el primer número primo: "))
        y = int(input("Ingrese el segundo número primo: "))
        print()
        bandera = validarPrimo(x)
        if (bandera == True):
            bandera = validarPrimo(y)
    return x,y


if __name__ == '__main__':
    x, y = leerValoresPrimos()
    n = x * y
    sigma = (x-1) * (y-1)

# Pasos para poder llevar a cabo algoritmo RSA.

# 1. Escoger dos primos X y Y.
# 2. Calcular n.
# 3. Calcular ϕ(n)
# 4. Calcular φ.
# 5. Calcular e.
# 6. Calcular d.
# 7. Obtener clave publica: (e,n)
# 8. Obtener clave privada: (d,n)