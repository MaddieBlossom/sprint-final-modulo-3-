
#sistema de envio debe de preguntar que tipo de envío es necesario (envio rapido o envio largo)

#Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la distancia de 1.000 km es considerado rápido

#En el caso que sea un envío rápido debe enviarse a una Bodega_A, caso contrario debe ser almacenado a una Bodega_B.

#El programa debe verificar que cada bodega no supere las 500 unidades.


def procesar_envio(distancia, unidades):
    # verificar la distancia
    if distancia > 1000:
        tipo_envio = "Largo"
        bodega_destino = "Bodega B"
    else:
        tipo_envio = "Rápido"
        bodega_destino = "Bodega A"

    # verificar la capacidad de las bodegas
    bodega_a = unidades <= 500
    bodega_b = unidades <= 500

    if tipo_envio == "Rápido":
        if bodega_a:
            bodega_destino = "Bodega A"
        elif bodega_b:
            bodega_destino = "Bodega B"
        else:
            print("No hay suficiente capacidad en las bodegas.")
            return None
    else:
        if bodega_b:
            bodega_destino = "Bodega B"
        elif bodega_a:
            bodega_destino = "Bodega A"
        else:
            print("No hay suficiente capacidad en las bodegas.")
            return None
  
    return tipo_envio, bodega_destino

final = procesar_envio(500, 800)
print(final)






