def edad_actual_persona(año):
    edad_actual = 2024-año
    return edad_actual


def mayor_edad(personas, edades):
    max_edad = max(edades)
    lugar = edades.index(max_edad)
    return f"{personas[lugar]} con la edad de {max_edad} es mayor a los demás pacientes."


def menor_edad(personas, edades):
    max_edad = min(edades)
    lugar = edades.index(max_edad)
    return f"{personas[lugar]} con la edad de {max_edad} es menor a los demás pacientes."
