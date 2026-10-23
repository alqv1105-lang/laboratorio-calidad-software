
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def registrar_venta(precio, cantidad):
    importe = precio * cantidad
    return importe


print("Subtotal:", calcular_subtotal(50, 3))
print("Importe:", registrar_venta(50, 3))
  
