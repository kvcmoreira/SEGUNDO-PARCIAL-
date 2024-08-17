class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f"Producto(ID={self.id}, Nombre={self.nombre}, Cantidad={self.cantidad}, Precio={self.precio})"
class ProductoExistenteError(Exception):
    pass

class ProductoNoEncontradoError(Exception):
    pass

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            raise ProductoExistenteError("El ID ya existe en el inventario.")
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id not in self.productos:
            raise ProductoNoEncontradoError("El ID no existe.")
        del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id not in self.productos:
            raise ProductoNoEncontradoError("El ID no existe.")
        if cantidad is not None:
            self.productos[id].cantidad = cantidad
        if precio is not None:
            self.productos[id].precio = precio

    def buscar_productos_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)
def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar
