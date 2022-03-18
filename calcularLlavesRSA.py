
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


def obtenerMCD(e, sigma):
    while (sigma != 0):
        e, sigma = sigma, e % sigma
    return e


def calcularE(sigma):
    for i in range(1, 1000):
        if (obtenerMCD(i, sigma) == 1):
            e = i
    return e


def euclideanAlgoritmo(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        mcd, s, t = euclideanAlgoritmo(b, a % b)
        s = s - ((a // b) * t)
        return (mcd, t, s)


def calcularValorD(e, sigma):
    mcd, s, _ = euclideanAlgoritmo(e , sigma)
    if(mcd != 1):
        return None
    else:
        return s % sigma


def leerPalabra():
    print("En caso de desencriptar, por favor dijite los numeros separados por coma. Ej: 3,4,5")
    return input("Ingrese la palabra encriptada o desencriptada: ")


def encriptarPalabra(llavePublica, mensaje):
    e, n = llavePublica
    mensajenuevo = []
    m = 0
    for i in mensaje:
        if (i.isupper()):
            m = ord(i) - 65
            c = (m ** e) % n
            mensajenuevo.append(c)
        elif (i.islower()):
            m = ord(i) - 97
            c = (m ** e) % n
            mensajenuevo.append(c)
        elif (i.isspace()):
            spc = 400
            mensajenuevo.append(400)
    return mensajenuevo


def desencriptarPalabra(llavePrivada, mensaje):
    d, n = llavePrivada
    txt = mensaje.split(',')
    nuevoMensaje = ''
    m = 0
    for i in txt:
        if (i == '400'):
            nuevoMensaje += ' '
        else:
            m = (int(i) ** d) % n
            m += 65
            c = chr(m)
            nuevoMensaje += c
    return nuevoMensaje


def realizarOperacion(mensaje, llavePublica, llavePrivada):
    opcion = input("\nIngrese <1> si desea encriptar o <2> para desencriptar el mensaje: ")
    if(opcion=="1"):
        return  encriptarPalabra(llavePublica, mensaje)
    elif(opcion=="2"):
        return desencriptarPalabra(llavePrivada, mensaje) 
    else:
        print("No digito una opción valida.")
        return None


def imprimirValores(x, y, n, sigma, e, d, llavePublica, llavePrivada, mensaje, nuevoMensaje):
    print("\n******************************************************************************************************")
    print("\nLos números primos ingresados fueron: " + str(x) + "," + str(y))
    print("\nEl valor de n es: " + str(n))
    print("\nEl valor de ϕ(n) es: " + str(sigma))
    print("\nEl valor de e es: " + str(e))
    print("\nEl valor de d es: " + str(d))
    print("\nEl valor de la llave publica es: " + str(llavePublica))
    print("\nEl valor de la llave privada es: " + str(llavePrivada))
    print("\nEl mensaje ingresado es: " + mensaje)
    print("\nEl nuevo mensaje es: " + str(nuevoMensaje))
    print("\nEl siguiente demo se logro con la ayuda del algoritmo encontrado en la pagina: https://sites.psu.edu/gottiparthyanirudh/writing-sample-3/")


def main():
    x, y = leerValoresPrimos()
    n = x * y
    sigma = (x - 1) * (y - 1)
    e = calcularE(sigma)
    d = calcularValorD(e, sigma)
    llavePublica = (e, n)
    llavePrivada = (d, n)
    mensaje = leerPalabra()
    nuevoMensaje = realizarOperacion(mensaje, llavePublica, llavePrivada)
    imprimirValores(x,y,n,sigma,e,d,llavePublica,llavePrivada,mensaje,nuevoMensaje)


if __name__ == '__main__':
    main()


# Pasos para poder llevar a cabo algoritmo RSA.
# 1. Escoger dos primos X y Y.
# 2. Calcular n.
# 3. Calcular ϕ(n)
# 4. Calcular e.
# 5. Calcular d.
# 6. Obtener clave publica: (e,n)
# 7. Obtener clave privada: (d,n)