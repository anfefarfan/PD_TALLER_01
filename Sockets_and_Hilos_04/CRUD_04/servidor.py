import socket
import DataBase

DataBase.CREATE_DATABASE("python_tienda_db")
DataBase.CREATE_TABLE("tienda", "producto", "precio")

class Servidor():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conection, direccion = self.mi_socket.accept()

        while True:
            while True:
                conection.send("\n1.[VER PRODUCTOS]    \n2.[AGREGAR PRODUCTOS] \n3.[EDITAR PRODUCTOS]  \n4.[ELIMINAR PRODUCTOS]    \n\n0.[SALIR]\n".encode())
                try:
                    msj = conection.recv(1024)
                    if int(msj) > 4:
                        msj = "error"
                    msj = int(msj)
                    break
                except ValueError:
                    conection.send("\n\n<<Opción Invalida>>\n\n".encode())

            print("[]: "+str(msj))
            if(msj == 0):
                break

            if(msj == 1):
                products = DataBase.SELECT_DATABASE("tienda")
                conection.send("\n<<Cargando presione ENTER>>\n".encode())
                for product in products:
                    conection.send(("\n  [CODE]: "+str(product[0])).encode())
                    conection.send(("\n  [PRODUCTO]: "+str(product[1])).encode())
                    conection.send(("\n  [PRECIO]: $"+str(product[2])).encode())
                    conection.send("\n-------------------------------".encode())

            if(msj == 2):
                conection.send("[NOMBRE DEL PRODUCTO]: ".encode())
                producto = conection.recv(1024).decode()
                conection.send("[PRECIO DEL PRODUCTO]: ".encode())
                precio = conection.recv(1024).decode()
                DataBase.INSERT_DATABASE("tienda", "producto", str(producto), "precio", str(precio))

            if(msj == 3):
                conection.send("[INGRESE EL CODIGO DEL PRODUCTO QUE DESEA EDITAR]".encode())
                code = conection.recv(1024).decode()
                product = DataBase.SELECT_WHERE_DATABASE("tienda", code)
                print(product)
                if product == []:
                    print("nulo")
                    conection.send("[NO EXISTE ESTE PRODUCTO]".encode())
                else:
                    print("lleno")
                    conection.send("[NOMBRE DEL PRODUCTO]: ".encode())
                    producto = conection.recv(1024).decode()
                    conection.send("[PRECIO DEL PRODUCTO]: ".encode())
                    precio = conection.recv(1024).decode()

                    if producto == ' ':
                        print(product)
                        producto =str(product[0][1])
                    if precio == ' ':
                        precio = str(product[0][2])

                    DataBase.UPDATE_DATABASE("tienda", "producto", str(producto), "precio", str(precio), code)

            if(msj == 4):
                conection.send("[INGRESE EL CODIGO DEL PRODUCTO QUE DESEA ELIMINAR]".encode())
                code = conection.recv(1024).decode()
                DataBase.DELETE_WHERE_DATABASE("tienda", code)

        print("\n\n<<Presione 'ENTER' para salir>>\n\n")
        conection.close()
        self.mi_socket.close()

servidor = Servidor()
