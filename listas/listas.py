# Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte",
            "Júpiter", "Saturno", "Urano", "Neptuno"]
# print(planetas[-3])// toma los valores desde el últmo de la lista
# el segundo valor toma el otro valor últmo
# print(planetas[2:8])
# print(len(planetas))
# print(planetas[6])

gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 124054  # Newtons, en la tierra

print(f"En la tierra, un autobus de dos pisos pesa {peso_bus} N")
print(f"En Mercurio, un autobus de dos pisos pesa {
      peso_bus*gravedad_en_planetas[0]} N")

print(f"Lo mas Liviano que sería un autobús en el sistema solar es {
      peso_bus*min(gravedad_en_planetas)} N")
print(f"Lo mas Pesado que sería un autobús en el sistema solar es {
      peso_bus*max(gravedad_en_planetas)} N")
