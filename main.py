productos = []

def menu():

    print("=====================================")
    print("          SISTEMA AGROCBA            ")
    print("=====================================")
    print("Sistema iniciado correctamente")


def menuPp():
    print("=============================================")
    print("                SISTEMA AGROCBA            ")
    print("=============================================")
    print("=     1. Registrar producto                 =")
    print("=     2. Consultar productos                =")
    print("=     3. Buscar producto                    =")
    print("=     4. Actualizar producto                =")
    print("=     5. Eliminar producto                  =")
    print("=     6. Mostrar valor total del inventario =")
    print("=     7. Salir                              =")
    print("=============================================")




def registrar_producto():
    while True:

        codigo = input("Escriba el codigo del producto: ")

        repetido = False
        for producto in productos:
            if producto["codigo"] == codigo:
                repetido = True
                break
        if repetido:
            print("ya se ha registrado un producto con este codigo.")
        else:
            break
    nombre = str(input("Escriba el nombre: "))
    categoria = str(input("Escriba la categoria: "))
    cantidad = int(input("Escriba la cantidad: "))
    precio = int(input("Escriba el precio: "))  

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }
    productos.append(nuevo_producto)

    with open("producto.txt", "a", encoding="utf-8") as orden:
        orden.write(str(nuevo_producto) + "\n")
    return


def consultar_producto():
    print("=============================================")
    print("               CONSULTAR PRODUCTO            ")
    print("=============================================")

    if not productos:
        print("No hay productos registrados en este momento.")
        return
    for prod in productos:
        print(f"Codigo: {prod['codigo']}")
        print(f"Nombre: {prod['nombre']}")
        print(f"Categoria: {prod['categoria']}")
        print(f"Cantidad: {prod['cantidad']}")
        print(f"Precio: {prod['precio']}")
def todo():
    control = True
    menu()
    input("haz click en cualquier tecla para continuar")
    while(control):
        menuPp()
        op = int(input("selecciona una opcion: "))
        match op:
            
            case 1:
                print("registrar producto ha sido seleccionado..")
                primero = True
                while(primero):
                    
                    registrar_producto()
                    while True:
                        
                        try:
                            opcio = str(input("desea añadir otro producto? si / no: ")).strip().lower()
                            
                            if opcio == "no":
                                input("has salido de la opcion 1, click enter para volver al menu")
                                primero = False
                                break
                            elif opcio != "si":
                                print("escribe si o no")
                            elif opcio == "si":
                                break
                            else: 
                                raise ValueError
                        except ValueError:
                            print("debes escribir si o no")
                        except TypeError:
                            print("debes escribir si o no")


                
            case 2:
                print("consultar producto ha sido seleccionado..")
                consultar_producto()

            case 3:
                print("buscar producto ha sido seleccionado..")

            case 4:
                print("actualizar producto ha sido seleccionado..")

            case 5:
                print("eliminar producto ha sido seleccionado..")

            case 6:
                print("mostrar valor total del inventario ha sido seleccionado..")

            case 7:
                print("has salido del programa... ")
                input("para regresar a la terminal presiona cualquier boton")
                control = False





todo()