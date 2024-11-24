# Escriba un programa donde el usuario elija ingresar cualquier cantidad de datos utilizando el ciclo for .

# Crear una lista llamada datos.

# Debe validar el tipo de dato numérico y guardarlo en una lista llamada datos.
# Para ello se debe investigar un método que permita validar, si en los caracteres existen valores numéricos.

# Validar si es decimal y guardar en la lista datos.
# Validar si es string y guardar en la lista datos.

# Imprimir la lista con el siguiente formato:
# f”Su lista es: < datos>”

datos = []
valorArreglo = int(
    input("Ingrese la cantidad datos para la lista:"))


for i in range(valorArreglo):

    valor = input(f"Ingrese datos {i}: ")
    if valor.isdigit():
        print(valor)
        datos.append(valor)
    elif valor.count('.') == 1 and valor.replace('.', '', 1).isdigit():
        print(valor)
        datos.append(valor)
    else:
        datos.append(valor)


print("---------------Finaliza proceso-----------------")
print(f"Su lista es: {datos}")
