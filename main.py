import json
try:
    with open("producto.json", "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
except FileNotFoundError:
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

    with open("producto.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4 )
    return


def consultar_producto():
    print("=============================================")
    print("               CONSULTAR PRODUCTOS           ")
    print("=============================================")

    if not productos:
        print("No hay productos registrados en este momento.")
        return
    for prod in productos:
        print("=============================================")
        print(f"Codigo: {prod['codigo']}")
        print(f"Nombre: {prod['nombre']}")
        print(f"Categoria: {prod['categoria']}")
        print(f"Cantidad: {prod['cantidad']}")
        print(f"Precio: {prod['precio']}")
        print("=============================================")



def buscar_producto():

    if not productos:
        print("=============================================")
        print("               BUSCAR PRODUCTOS              ")
        print("=============================================")
        print("Aun no hay productos registrados. ")
        return
    
    Encontrado = False
    busqueda = input("ingrese el codigo que desea buscar: ")
    for bus in productos:
        
        if bus["codigo"] == busqueda:
            print(f"Codigo: {bus['codigo']}")
            print(f"Nombre: {bus['nombre']}")
            print(f"Categoria: {bus['categoria']}")
            print(f"Cantidad: {bus['cantidad']}")
            print(f"Precio: {bus['precio']}")
            Encontrado = True
        if not Encontrado:
            print("no hay productos con ese codigo")


def actualizar_producto():

    Encontrado = False
    busqueda = input("ingrese el codigo que desea buscar: ")
    for bus in productos:
            
            if bus["codigo"] == busqueda:
                bus['nombre'] = input("escriba el nuevo nombre: ")
                bus['categoria'] = input("escriba la nueva categoria: ")
                bus['cantidad'] = int(input("escriba la nueva cantidad: "))
                bus['precio'] = int(input("escriba el nuevo precio: "))
                Encontrado = True

                with open("producto.json", "w", encoding="utf-8") as archivo:
                    json.dump(productos, archivo, ensure_ascii=False, indent=4 )

                print("producto actualizado correctamente")
                break
            if not Encontrado:
                print("no hay productos con ese codigo")


def eliminar_producto():

    Encontrado = False
    busqueda = input("ingrese el codigo que desea buscar para eliminar: ")
    for bus in productos:
                
        if bus["codigo"] == busqueda:

            productos.remove(bus)
            Encontrado = True
    
            with open("producto.json", "w", encoding="utf-8") as archivo:
                json.dump(productos, archivo, ensure_ascii=False, indent=4 )
    
            print("producto eliminado correctamente")
            break

        if not Encontrado:
                        print("no hay productos con ese codigo")


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
                buscar_producto()
            case 4:
                print("actualizar producto ha sido seleccionado..")
                actualizar_producto()

            case 5:
                print("eliminar producto ha sido seleccionado..")
                eliminar_producto()

            case 6:
                print("mostrar valor total del inventario ha sido seleccionado..")

            case 7:
                print("has salido del programa... ")
                input("para regresar a la terminal presiona cualquier boton")
                control = False





todo()