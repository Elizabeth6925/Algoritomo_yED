#Desarrollar una función que permita convertir un número romano en un número decimal.


def romano_a_dec(romano, total=0, valor_prev=0):
    valores = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }

    # Caso base: si la cadena está vacía
    if romano == "":
        return total

    valor = valores[romano[-1]]

    if valor < valor_prev:
        total -= valor
    else:
        total += valor

    return romano_a_dec(romano[:-1], total, valor)


# Programa principal
romano = input("Ingrese un número en romano: ").upper()
resultado = romano_a_dec(romano)

print("Resultado:", resultado)