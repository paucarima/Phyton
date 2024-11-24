import random


print("Escoge con número el país que esta viajando  ")
print("1.Ecuador")
print("2.Colombia")
print("3.Perú")
pais = int(input(f"Ingresa aquí: "))

if pais == 1:
    print("Escoge tu zona con un numero")
    print("1.urbana")
    print("2.rural")
    print("3.perimetral")
    zona = int(input("Ingresa aquí: "))
    velocidad = random.randrange(10, 120)

    if velocidad <= 10 and velocidad > 0 and zona == 1:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Ecuador zona urbana"
        )
    elif velocidad > 50 and zona == 1:
        print(
            f"Tu velocidad es: {
                velocidad}, km/h vas muy rápido En Ecuador zona urbana"
        )
    elif velocidad >= 10 and velocidad <= 50 and zona == 1:
        print(f"Excelente vas bien en zona urbana {velocidad}")

    if velocidad <= 51 and velocidad > 0 and zona == 2:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Ecuador zona rural"
        )

    elif velocidad > 70 and zona == 2:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy rápido En Ecuador zona rural"
        )
    elif velocidad >= 51 and velocidad <= 70 and zona == 2:
        print(f"Excelente vas bien en zona rural {velocidad}")

    if velocidad <= 71 and velocidad > 0 and zona == 3:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Ecuador zona perimetral"
        )

    elif velocidad > 90 and zona == 3:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy rápido En Ecuador zona perimetral"
        )
    elif velocidad >= 71 and velocidad <= 90 and zona == 3:
        print(f"Excelente vas bien en zona perimetral {velocidad}")

# Para Colombia:
elif pais == 2:
    print("Escoge tu zona con un numero")
    print("1.urbana")
    print("2.rural")
    print("3.perimetral")
    zona = int(input("Ingresa aquí: "))
    velocidad = random.randrange(10, 120)

    if velocidad <= 10 and velocidad > 0 and zona == 1:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Colombia zona urbana"
        )
    elif velocidad > 30 and zona == 1:
        print(
            f"Tu velocidad es: {
                velocidad}, km/h vas muy rápido En Colombia zona urbana"
        )
    elif velocidad >= 10 and velocidad <= 30 and zona == 1:
        print(f"Excelente vas bien en zona urbana {velocidad}")

    if velocidad <= 31 and velocidad > 0 and zona == 2:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Colombia zona rural"
        )

    elif velocidad > 80 and zona == 2:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy rápido En Colombia zona rural"
        )
    elif velocidad >= 31 and velocidad <= 80 and zona == 2:
        print(f"Excelente vas bien en zona rural {velocidad}")

    if velocidad <= 81 and velocidad > 0 and zona == 3:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Colombia zona perimetral"
        )

    elif velocidad > 100 and zona == 3:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy rápido En Colombia zona perimetral"
        )
    elif velocidad >= 81 and velocidad <= 100 and zona == 3:
        print(f"Excelente vas bien en zona perimetral {velocidad}")


# Para Perú:
# Zona urbana: Máximo 40 Km/h y mínimo 10 Km/h
# Zona rural: Máximo 60 Km/h y mínimo 41 Km/h
# Zona perimetral: Máximo 120 Km/h y mínimo 61 Km/h
elif pais == 3:
    print("Escoge tu zona con un numero")
    print("1.urbana")
    print("2.rural")
    print("3.perimetral")
    zona = int(input("Ingresa aquí: "))
    velocidad = random.randrange(10, 120)

    if velocidad <= 10 and velocidad > 0 and zona == 1:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Perú zona urbana"
        )
    elif velocidad > 40 and zona == 1:
        print(
            f"Tu velocidad es: {
                velocidad}, km/h vas muy rápido En Perú zona urbana"
        )
    elif velocidad >= 10 and velocidad <= 40 and zona == 1:
        print(f"Excelente vas bien en zona urbana {velocidad}")

    if velocidad <= 41 and velocidad > 0 and zona == 2:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Perú zona rural"
        )

    elif velocidad > 60 and zona == 2:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy rápido En Perú zona rural"
        )
    elif velocidad >= 41 and velocidad <= 60 and zona == 2:
        print(f"Excelente vas bien en zona rural {velocidad}")

    if velocidad <= 61 and velocidad > 0 and zona == 3:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy lento En Perú zona perimetral"
        )

    elif velocidad > 120 and zona == 3:
        print(
            f"Tu velocidad es:{
                velocidad}, km/h vas muy rápido En Perú zona perimetral"
        )
    elif velocidad >= 61 and velocidad <= 120 and zona == 3:
        print(f"Excelente vas bien en zona perimetral {velocidad}")

else:
    print("Ingresa un número válido de país (1, 2 o 3).")

