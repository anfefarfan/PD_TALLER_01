import socket


class Servidor():

    def __init__(self):
        self.word = ""
        self.word_ocul = ""
        self.word_ocul_temp = ""
        self.temp_var = ""
        self.error_numero = 0
        self.juego_terminado = False
        self.win = False

        self.error = {
        0 : "\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
        1 : "\t ______\n\t |    |\n\t O    |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
        2 : "\t ______\n\t |    |\n\t O    |\n\t |    |\n\t      |\n\t      |\n\t______|_\n\n",
        3 : "\t ______\n\t |    |\n\t O    |\n\t/|    |\n\t      |\n\t      |\n\t______|_\n\n",
        4 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/     |\n\t      |\n\t______|_\n\n",
        5 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/ \   |\n\t      |\n\t______|_\n\n",
        6 : "\t [END]"
        }

        self.mi_socket = socket.socket()
        self.mi_socket.bind(("",9090))
        self.mi_socket.listen(1)
        conetion, direccion = self.mi_socket.accept()

        self.asignar_word()

        while True:
            msj = conetion.recv(1024)
            print("[]: "+msj.decode())

            self.if_juego_terminado()
            if self.juego_terminado == False:
                self.buscar_letra(msj.decode())
                conetion.send(self.imprimir_ahorcado().encode()+self.print_word_ocul().encode())
            if self.win == True:
                conetion.send("\n     [HAS GANADO]".encode())
            if self.juego_terminado == True and self.win == False:
                conetion.send("\n      [JUEGO TERMINADO]".encode())

        print("close")

    def imprimir_ahorcado(self):
        return self.error[self.error_numero]

    def asignar_word(self):

        self.word = "programacion"
        for letra in range(len(self.word)):
            self.word_ocul = self.word_ocul + "_"

    def print_word_ocul(self):
        # global word_ocul_temp
        if self.error_numero <= 5:
            self.word_ocul_temp = ""

            for letra in range(len(self.word)):
                self.word_ocul_temp = self.word_ocul_temp + self.word_ocul[letra] + " "

            return self.word_ocul_temp

    def buscar_letra(self, letra):

        if self.error_numero <= 5:
            self.temp_var = ""
            for pos in range(len(self.word)):
                if self.word[pos] == str(letra):
                    self.temp_var = self.temp_var + str(letra)
                else:
                    self.temp_var = self.temp_var + self.word_ocul[pos]
            if self.word_ocul == self.temp_var and self.error_numero < 6:
                self.error_numero = self.error_numero + 1
            self.word_ocul = self.temp_var

    def if_juego_terminado(self):
        # global error_numero, juego_terminado, win
        if self.error_numero >= 5:
            self.juego_terminado = True
        if self.word == self.word_ocul:
            self.win = True

servidor = Servidor()
