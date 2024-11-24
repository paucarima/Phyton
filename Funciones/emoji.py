def encontrar_palabra(frase):
    if "feliz" in frase:
        print(f"El emoji que te representa es: \U0001F600")

    elif "triste" in frase:
        print(f"El emoji que te representa es: \U0001F622")


listas = []


def agregar_frase(frase):
    listas.append(frase)
    print(f"La frase fue guardada correctamente: {listas}")
