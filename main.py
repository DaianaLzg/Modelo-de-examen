#implementacion de funciones
from funciones import carga_de_productos, buscar_producto, ordenar_por_precio, producto_mas_caro, producto_mas_barato


#menu
valor = 0
inventario = []
while valor != 10:
    print("1. Cargar productos")
    print("2. Buscar producto")
    print("3. Ordenar productos por precio")
    print("4. Producto más caro")
    print("5. Producto más barato")
    print("6. Salir")

    valor = int(input("Seleccione una opción: "))

    if valor == 1:
        inventario += carga_de_productos()
        print(f"Los productos cargados son: {inventario}")
        
    elif valor == 2:
        if inventario == []:
            print("No hay productos cargados. ELIJA CARGAR PRODUCTOS PRIMERO")
            continue
        nombre_producto = input("Ingrese el nombre del producto a buscar: ")
        producto = buscar_producto(inventario, nombre_producto)
        if producto:
            print(f"El producto encontrado es: {producto}")
        else:
            print("Producto no encontrado.")
            
    elif valor == 3:
        if inventario == []:
            print("No hay productos cargados. ELIJA CARGAR PRODUCTOS PRIMERO")
            continue
        inventario_ordenado = ordenar_por_precio(inventario)
        print(f"Los productos ordenados por precio son: {inventario_ordenado}")
        
    elif valor == 4:
        if inventario == []:
            print("No hay productos cargados. ELIJA CARGAR PRODUCTOS PRIMERO")
            continue
        producto_caro = producto_mas_caro(inventario)
        print(f"El producto más caro es: {producto_caro}")
        
    elif valor == 5:
        if inventario == []:
            print("No hay productos cargados. ELIJA CARGAR PRODUCTOS PRIMERO")
            continue
        producto_barato = producto_mas_barato(inventario)
        print(f"El producto más barato es: {producto_barato}")
        
    elif valor == 6:
        print("Saliendo del programa...")
        break
    



