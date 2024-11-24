def datos(nombre, apellidso, edad, mensaje="Hola"):
    if edad < 18:
        print(f"{mensaje}{nombre}{apellidso} es menor de edad")
    else:
        print(f"{mensaje}{nombre}{apellidso} es mayor de edad")
