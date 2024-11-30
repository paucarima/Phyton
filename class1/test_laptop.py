from laptop import Laptop
from laptop_gaming import Lapto_Gaming
from laptop_Business import Laptop_Business
# laptop_pepito = Laptop("Lenovo", "i7", 32)
# laptop_maria = Laptop("Lenovo", "i7", 32, 600)
# # lapto_juanito = Lapto_Gaming("MSI", "I7", 64, 900, 20)
# # print(lapto_juanito.costo)

lapto_juanito = Lapto_Gaming("MSI", "I7", 4, "RTX 8GB")
# print(lapto_juanito.realizar_diagnostico_sistema())
# for numero in range(1, 10):
#     asus_lapto = Laptop.asus_laptop(numero)
#     print(asus_lapto.__dict__)
# print(Laptop.comparar_costo(laptop_pepito, laptop_maria))


# print(laptop_pepito.__dict__)  # lleva datos del objeto
# print(laptop_pepito.valor_final())
# print(f"El valor de descuento: {laptop_pepito.valor_descuento(10)}")

lapto_anthony = Laptop_Business("MSI", "I7", 8, "100", "10")


print(lapto_anthony.realizar_diagnostico_sistema())


def imprimir_informe(Laptop):
    informe = Laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"--->{clave}: /{valor}")
    print("\n")


print("JUANITO: ")
imprimir_informe(lapto_juanito)

print("ANTHONY")
imprimir_informe(lapto_anthony)
