import random

aletaorio = random.randint(1, 9)
aletaorio_dos = random.randint(1, 9)

if aletaorio == 4:
    print("Te ganaste un chupete")
elif aletaorio == 8:
    print("Te ganaste un bal+on")
elif aletaorio == 3 and aletaorio_dos == 7:
    print("Te ganaste un televisor")
else:
    print("Perdiste!!!")
 