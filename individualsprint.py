# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación
# (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).

import random, string, json

usuarios = ({"nombre": "Juan", "apellido": "gallardo"},
            {"nombre": "María", "apellido": "garcia"}, 
            {"nombre": "Pedro", "apellido": "miranda"}, 
            {"nombre": "Sofía", "apellido": "rojas"}, 
            {"nombre": "Carlos", "apellido": "ortiz"}, 
            {"nombre": "Lucía", "apellido": "valdez"}, 
            {"nombre": "David", "apellido": "basaure"}, 
            {"nombre":"Marta","apellido":"herrera"},
            {"nombre":"Alejandro","apellido":"soto"},
            {"nombre":"Daniela","apellido":"zoro"})
# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
# Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.

def crear_cuenta(usuario, contraseña, telefono):
    cuenta = {"usuario": username, "contraseña": contraseña,"telefono": telefono}
    return cuenta

def generar_contrasena(longitud):  # Se agregó el parámetro longitud a la función generar_contrasena. 
    # generar caracteres aleatorios para la contraseña 
    caracteres = string.ascii_letters + string.digits
    # combinar caracteres aleatorios para crear la contraseña
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contrasena

cuentas = []
for usuario in usuarios:
    username = usuario["nombre"][0] + usuario["apellido"] # nombre de usuario inicial
    
    
    contraseña = generar_contrasena(8) # contraseña inicial
    telefono = input(f"Ingrese el número telefónico de {username}: ")
    while len(telefono) != 8 or not telefono.isdigit():
        telefono = input("El número telefónico debe tener 8 dígitos. Ingrese un número válido: ")
    cuenta = crear_cuenta(usuario, contraseña, telefono)
    cuentas.append(cuenta)

# imprimir las cuentas de usuario creadas
for cuenta in cuentas:
    print(cuenta)
    
#Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
#Por cada cuenta debe pedir un número telefónico para contactarse.
datos_usuario = []
for cuenta in cuentas:
    datos_usuario.append((cuenta["usuario"], cuenta["contraseña"], cuenta["telefono"]))

# imprimir los datos de usuario y contraseña
for cuenta in cuentas:
    print("Usuario:", cuenta["usuario"])
    print("Contraseña:", cuenta["contraseña"])
    print("Teléfono:", cuenta["telefono"])
    print()
    
cuentas_str = ""
for cuenta in cuentas:
    cuentas_str += cuenta["usuario"] + "," + cuenta["contraseña"] + "," + cuenta["telefono"] + "\n"

# imprimir las cuentas de usuario creadas como un string

print(f"datos de cuentas almacenados:", cuentas_str) 
