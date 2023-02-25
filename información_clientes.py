

clientes = [
{"nombre":"juan1", "apellido": "perez1","edad": 25, "id": "1212", "contraseña":" colocolo1"} ,
{"nombre":"juan2", "apellido": "perez2","edad": 26, "id": "1213","contraseña":" colocolo2"} ,
{"nombre":"juan3", "apellido": "perez3","edad": 27, "id": "1214", "contraseña":" colocolo3"} , 
{"nombre":"juan4", "apellido": "perez4","edad": 28, "id": "1215", "contraseña":" colocolo4"}
]

def agregar_cliente(): #Esta funcion permite agregar clientes a la lista de clientes 
    nombre = input("Ingrese el nombre del cliente que desea agregar: ")
    apellido = input("Ingrese el apellido del cliente: ")
    edad = input("Ingrese la edad del cliente: ")
    id = input("Ingrese el ID del cliente: ")
    contraseña = input("Ingrese la contraseña del cliente: ")
    
    cliente = {"nombre": nombre, "apellido": apellido, "edad": edad, "id": id, "contrasena": contraseña}
    clientes.append(cliente)

agregar_cliente() # Ejecuciín para agregar un cliente a la lista de clientes

for cliente in clientes:
    print(cliente.items())


def eliminar_cliente():# Elimina un cliente de la lista de clientes
    id_cliente = input("Ingrese el ID del cliente que desea eliminar: ")
    
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            clientes.remove(cliente)
            print("Cliente eliminado exitosamente.")
            return
        
    print("Cliente no encontrado.")

eliminar_cliente() # Su ejecución para  eliminar un cliente de la lista de clientes

for cliente in clientes:
    print(cliente.items())

    
def mostrar_info_cliente(): #Nos entrega toda la informacion relacionada con un cliente buscandolo por su ID
    id_cliente_info = input("Ingrese el ID del cliente del que desea obtener la información: ")
    for cliente in clientes:
        if cliente["id"] == id_cliente_info:
            print("Nombre:", cliente["nombre"])
            print("Apellido:", cliente["apellido"])
            print("Edad:", cliente["edad"])
            print("ID:", cliente["id"])
            print("contraseña:", cliente["contraseña"])
            return
        
    print("Cliente no encontrado.") # Ejecución para buscar la información de un cliente por su id

mostrar_info_cliente()
    