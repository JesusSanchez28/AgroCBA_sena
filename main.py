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
    print("")
    print("=============================================")
    
def registrar_producto():
    int(input("Escriba el codigo del producto: "))
    


def todo():
    control = True
    menu()
    input("haz click en cualquier tecla para continuar")
    while(control):
        menuPp()
        op = int(input("selecciona una opcion"))
        match op:
            
            case 1:
                print("registrar producto ha sido seleccionado..")
                input("para regresar presiona cualquier boton")
            case 2:
                print("consultar producto ha sido seleccionado..")
                input("para regresar presiona cualquier boton")
            case 3:
                print("buscar producto ha sido seleccionado..")
                input("para regresar presiona cualquier boton")
            case 4:
                print("actualizar producto ha sido seleccionado..")
                input("para regresar presiona cualquier boton")
            case 5:
                print("eliminar producto ha sido seleccionado..")
                input("para regresar presiona cualquier boton")
            case 6:
                print("mostrar valor total del inventario ha sido seleccionado..")
                input("para regresar presiona cualquier boton")
            case 7:
                print("has salido del programa... ")
                input("para regresar a la terminal presiona cualquier boton")
                control = False





todo()