from tkinter import *

class Triqui():
    def __init__(self):
        global ventana, turnoPJ, gameover
        ventana = Tk()
        ventana.title("[JUEGO TRIQUI]")
        ventana.geometry("700x360")
        turnoPJ = 0
        gameover = 0

        self.create_buttons()

        label_turno = Label(ventana, text="[TURNO]", font=('Arial 18 bold'), fg='grey').place(x=460, y= 40)
        label_turno_jugador = Label(ventana, text="[nombre]", font=('Arial 18 bold'), fg='grey').place(x=450, y= 80)

        label_victorias = Label(ventana, text="[VICTORIAS]", font=('Arial 18 bold'), fg='grey').place(x=430, y= 170)
        label_victorias_jugador_1 = Label(ventana, text="[jugador 1]", font=('Arial 18 bold'), fg='grey').place(x=440, y= 210)
        label_victorias_jugador_2 = Label(ventana, text="[jugador 2]", font=('Arial 18 bold'), fg='grey').place(x=440, y= 250)

        # v = StringVar()
        # Label(master, textvariable=v).pack()
        #
        # v.set("New Text!")
        # v.set("New Text!")

        ventana.mainloop()



    def marcar(self, button_click):
        global gameover
        if gameover == 0:
            if button_click["text"] == " " and turnoPJ == 0:
                button_click["text"] = "O"
                self.cambio_turno()
            elif button_click["text"] == " " and turnoPJ == 1:
                button_click["text"] = "X"
                self.cambio_turno()
        self.gameover()

    def cambio_turno(self):
        global turnoPJ
        if turnoPJ == 0:
            turnoPJ = 1
        elif turnoPJ == 1:
            turnoPJ = 0

    def turno(self):
        global turnoPJ
        if turnoPJ == 0:
            label_turno_jugador["text"] = "Jugador O"
        elif turnoPJ == 1:
            label_turno_jugador["text"] = "Jugador X"

    def create_buttons(self):
        # for x in range(3):
        #     for y in range(3):
        #         buttons[button] = Button(ventana, text=button, font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:marcar(buttons, button))
        #         buttons[button].grid(row = x, column = y, sticky = S+N+E+W)
        #         button = button + 1
        self.button_1 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_1))
        self.button_1.grid(row = 0, column = 0, sticky = S+N+E+W)
        self.button_2 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_2))
        self.button_2.grid(row = 0, column = 1, sticky = S+N+E+W)
        self.button_3 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_3))
        self.button_3.grid(row = 0, column = 2, sticky = S+N+E+W)
        self.button_4 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_4))
        self.button_4.grid(row = 1, column = 0, sticky = S+N+E+W)
        self.button_5 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_5))
        self.button_5.grid(row = 1, column = 1, sticky = S+N+E+W)
        self.button_6 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_6))
        self.button_6.grid(row = 1, column = 2, sticky = S+N+E+W)
        self.button_7 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_7))
        self.button_7.grid(row = 2, column = 0, sticky = S+N+E+W)
        self.button_8 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_8))
        self.button_8.grid(row = 2, column = 1, sticky = S+N+E+W)
        self.button_9 = Button(ventana, text=" ", font=('Arial 20 bold'), bg='white', fg='grey', height=3, width=6, command=lambda:self.marcar(self.button_9))
        self.button_9.grid(row = 2, column = 2, sticky = S+N+E+W)

    def gameover(self):
        global gameover
        if self.button_1["text"] != " " and self.button_1["text"] == self.button_2["text"] and self.button_1["text"] == self.button_3["text"]:
            gameover = 1
        if self.button_4["text"] != " " and self.button_4["text"] == self.button_5["text"] and self.button_4["text"] == self.button_6["text"]:
            gameover = 1
        if self.button_7["text"] != " " and self.button_7["text"] == self.button_8["text"] and self.button_7["text"] == self.button_9["text"]:
            gameover = 1

        if self.button_1["text"] != " " and self.button_1["text"] == self.button_4["text"] and self.button_1["text"] == self.button_7["text"]:
            gameover = 1
        if self.button_2["text"] != " " and self.button_2["text"] == self.button_5["text"] and self.button_2["text"] == self.button_8["text"]:
            gameover = 1
        if self.button_3["text"] != " " and self.button_3["text"] == self.button_6["text"] and self.button_3["text"] == self.button_9["text"]:
            gameover = 1

        if self.button_1["text"] != " " and self.button_1["text"] == self.button_5["text"] and self.button_1["text"] == self.button_9["text"]:
            gameover = 1
        if self.button_3["text"] != " " and self.button_3["text"] == self.button_5["text"] and self.button_3["text"] == self.button_7["text"]:
            gameover = 1
        if gameover == 1:
            print("win")

    def winner_pop(self):
        pass

triqui = Triqui()
