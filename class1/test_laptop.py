from laptop import Laptop
laptop_pepito = Laptop("Lenovo", "i7", 32)
laptop_maria = Laptop("Lenovo", "i7", 32, 600)


for numero in range(1, 10):
    asus_lapto = Laptop.asus_laptop(numero)
    print(asus_lapto.__dict__)
    # print(Laptop.comparar_costo(laptop_pepito, laptop_maria))


# print(laptop_pepito.__dict__)  # lleva datos del objeto
# print(laptop_pepito.valor_final())
# print(f"El valor de descuento: {laptop_pepito.valor_descuento(10)}")
