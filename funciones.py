# Esta función carga productos en una matriz
def carga_de_productos():
    cantidad_ingresados = int(input("Cuantos productos desea ingresar?: "))
    productos_cargados = 0
    matriz = []
    while productos_cargados < cantidad_ingresados:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos_cargados += 1
        producto = [nombre, precio, cantidad]
        matriz += [producto]
    return matriz

#Buscar producto.
def buscar_producto(matriz, nombre_producto):
    producto = []
    for i in range(len(matriz)):
        if matriz[i][0] == nombre_producto:
            producto = matriz[i]
            break
    return producto

# Ordenar productos por precio.
def ordenar_por_precio(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[j][1] > matriz[j+1][1]:
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]
    return matriz

# Esta función devuelve el producto más caro de la matriz
def producto_mas_caro(matriz):
    producto_caro = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][1] > producto_caro[1]:
            producto_caro = matriz[i]
    return producto_caro

# Esta función devuelve el producto más barato de la matriz
def producto_mas_barato(matriz):
    producto_barato = matriz[0]
    for i in range(1, len(matriz)):
        if matriz[i][1] < producto_barato[1]:
            producto_barato = matriz[i]
    return producto_barato