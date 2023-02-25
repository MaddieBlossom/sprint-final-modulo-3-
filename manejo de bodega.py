#guardar informacion de productos en una bodega virtual.


productos = [
    {"nombre": "cucharas", "precio": 100, "id": 2020 , "stock": 300, "descripcion": " set de 4 piezas"} , 
    {"nombre": "cuchillos", "precio": 200, "id": 2021 , "stock": 400, "descripcion": "set de dos cuchillos acero tipo damasco"} , 
    {"nombre": "tenedores", "precio": 300, "id": 2022 , "stock": 500, "descripcion": "set de tenedores recubiertos en oro 4 piezas"},
    {"nombre": "vasos", "precio": 300, "id": 2022 , "stock": 500, "descripcion": "set de vasos recubiertos en diamantes 4 piezas"},
]
#Sumar y disminuir el numero de unidades por producto.


def actualizar_inventario(productos, nm_producto, unidades):
    for producto in productos:
        if producto["nombre"]== nm_producto and unidades >= 0:
            producto["stock"] += unidades
            print(f"se han añadido {unidades} unidades al producto {nm_producto}")
            print("producto actualizado en nuevo stock es el que se indica a continuacion: ")
            print(producto["nombre"], producto["stock"])
            return productos
        if producto["nombre"]== nm_producto and unidades < 0:
            producto["stock"] += unidades
            print(f"se han quitado {unidades} unidades al producto {nm_producto}")
            print("producto actualizado en nuevo stock es el que se indica a continuacion: ")
            print(producto["nombre"], producto["stock"])
            return productos
        break
    return productos
                   

#Agregar nuevos productos 

def agregar_producto():
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    nombre = input("ingrese el nombre del producto ")
    precio = float(input("ingrese el precio del producto "))
    id_codigo = int(input("ingrese el id del producto "))
    cantidad = int(input("ingrese el stock disponible acá "))
    descripcion_act = input("ingrese una descripcion del producto ")
    producto = {"nombre": nombre, "precio": precio, "id": id_codigo, "stock": cantidad, "descripcion": descripcion_act}
    stock_act = productos.append(producto)
    print("el producto se ha ingresado con exito")
    print("-------------------------------------------------")
    print("--------------Stock Actualizado---------------")
    print("-------------------------------------------------")
    return stock_act   


#Quitar productos de la bodega virtual

def eliminar_diccionario(productos):
    for i, diccionario in enumerate(productos):
        print(f"{i+1}. {diccionario}")
    seleccion = int(input("Ingrese el número del producto que desea eliminar: "))
    if seleccion > 0 and seleccion <= len(productos):
        del productos[seleccion-1]
        print(f"El producto {seleccion} ha sido eliminado.")
    else:
        print("La selección ingresada no es válida.")

#Mostrar todos los productos disponibles y su stock, debe de tener un desfase de 1 segundo entre cada producto.

import time
def lista_retorno():
   for producto in productos:
    print(producto["nombre"], producto["stock"], "unidades disponibles")
time.sleep(1)
print("-------------------------------------------------")
print("-------------------------------------------------")

#verificar si el producto tien menos de 400 unidades y enviar una alerta.



def verificar_stock(productos, limite):
    for producto in productos:
        if producto['stock'] < limite:
            print(f"¡Alerta! El producto {producto['nombre']} tiene un stock menor a {limite} unidades.")



verificar_stock(productos, 400)


# eliminar_diccionario(productos)
# lista_retorno()

