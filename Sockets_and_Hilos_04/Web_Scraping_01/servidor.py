import requests, bs4, lxml, socket, sys

class Servidor():
    def __init__(self, host="localhost", port=9090):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(1)

        print("Conexion iniciada.")
        conexion, direccion = self.sock.accept()

        msj = conexion.recv(1024)

        while True:
            if msj.decode() == '1':
                resp = self.web('https://www.youtube.com/')
                conexion.send(resp.encode())
            else:
                print("Cerrar")
                self.sock.close()
                sys.exit()

    def web(self, url):
        try:
            array = []
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            for i in soup.select('h3'):
                array.append(i.text)
        except:
            print("Error")
            self.sock.close()

        return str(array)

server = Servidor()
