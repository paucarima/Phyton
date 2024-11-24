import agregar_edad


def nombre(nombres):
    lineas = nombres.split(',')
    # print("cortando ", lineas)
    personas = []
    años = []
    edades = []

    for linea in lineas:
        datos = linea.split()
        # print("................", datos)
        # print("longitud", len(datos))
        if len(datos) >= 2:
            nombrep = ' '.join(datos[:-1])
            año = datos[-1]
            personas.append(nombrep)
            años.append(año)

            edad = agregar_edad.edad_actual_persona(int(año))
            edades.append(edad)

            resultado_mayor = agregar_edad.mayor_edad(personas, edades)
            resultado_menor = agregar_edad.menor_edad(personas, edades)

    print("Nombre de las personas \n", personas)
    print("Años de las personas \n", años)
    print("Edad de las personas \n", edades)
    print("Edad máxima \n", resultado_mayor)
    print("Edad menor \n", resultado_menor)
