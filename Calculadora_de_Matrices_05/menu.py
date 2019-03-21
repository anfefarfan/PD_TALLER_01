import os, time, threading

clear = lambda: os.system('cls')

def title():
    clear()
    print("[PYTHON CALCULADORA DE MATRICES] \n")

def menu():
    global size, matrix_1, matrix_2
    size = 3

    while True:
        title()
        print("1.[CON UNA MATRIZ]")
        print("2.[CON DOS MATRIZ]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):
                    matrix_1 = create_matrix()

                    title()
                    print("[PRIMERA MATRIZ]\n")
                    print_matrix(matrix_1,"[A]")

                    one_matrix(matrix_1)
                    break
                if case(2):
                    matrix_1 = create_matrix()

                    clear()
                    print("[SEGUNDA MATRIZ]")
                    time.sleep(.500)
                    matrix_2 = create_matrix()

                    title()
                    print("[CON DOS MATRICES]\n")
                    print_matrix(matrix_1,"[A]")
                    print_matrix(matrix_2,"[B]")
                    two_matrix(matrix_1, matrix_2)
                    break
            break
        except ValueError:
            clear()
            print("\n\n¡NO ES UNA OPCION VALIDA!")
            time.sleep(.500)

def create_matrix():
    time.sleep(.500)
    matrix = [[0 for y in range(size)] for x in range(size)]

    for x in range(size):
        for y in range(size):
            while True:
                try:
                    clear()
                    print("[INGRESE LOS VALORES DE LA MATRIZ]\n")
                    matrix[x][y] = input(str(x+1)+","+str(y+1)+": ")
                    matrix[x][y] = int(matrix[x][y])
                    break
                except ValueError:
                    clear()
                    print("\n\n¡No es un numero!\n")
                    time.sleep(.500)
    return matrix

def print_matrix(matrix, letter):
    time.sleep(.500)
    print("[MATRIZ]"+letter+"\n")

    for x in range(size):
        for y in range(size):
            print('['+str(matrix[x][y]), end=']\t')
        print()
    print()

def one_matrix(matrix_1):
    while True:
        print("1.[DETERMINANTE]")
        print("2.[TRANSPUESTA]")
        print("3.[INVERSA]")
        print("4.[MULTIPLICAR POR NUMERO]")
        print("5.[ELEVADA A UNA POTENCIA]")
        print("6.[MATRIZ SIMETRICA]")
        print("7.[MATRIZ IDENTIDAD]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):
                    print("\n [DETERMINANTE]: " + str(determinante(matrix_1)))
                    break
                if case(2):
                    print_matrix(transpuesta(matrix_1), "[TRANSPUESTA]")
                    break
                if case(3): ###################
                    if determinante(matrix_1) == 0:
                        print("\nEl determinante de la matriz es cero, la matriz es no invertible")
                    else:
                        inversa(matrix_1)
                    break
                if case(4):
                    num_multi = input("[ingrese numero]: ")
                    print_matrix(multiplicar(matrix_1, num_multi), "[MULTIPLICADA POR "+ str(num_multi) +"]")
                    break
                if case(5):
                    num_elev = input("[ingrese numero]: ")
                    print_matrix(elevada(matrix_1, num_elev), "[ELEVADA]")
                    break
                if case(6):
                    temp = threading.Thread(target=matriz_simetrica, args=[matrix_1])
                    temp.setDaemon = True
                    temp.start()
                    temp.join()
                    break
                if case(7): ###################
                    matriz_identidad(matrix_1)
                    break
            break
        except ValueError:
            clear()
            print("\n\n¡Opción invalida!")
            time.sleep(.500)

def two_matrix(matrix_1, matrix_2):
    while True:
        print("1.[A x B]")
        print("2.[A - B]")
        print("3.[A + B]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):
                    print_matrix(multiplicar_ab(matrix_1, matrix_2), "[A*B]")
                    break
                if case(2):
                    print_matrix(restar_ab(matrix_1, matrix_2), "[A-B]")
                    break
                if case(3):
                    print_matrix(sumar_ab(matrix_1, matrix_2), "[A+B]")
                    break
            break
        except ValueError:
            clear()
            print("\n\n¡Opción invalida!")
            time.sleep(.500)

def determinante(matrix_1):
    global resultado_det
    resultado_det = 0

    def lado_a(matrix_1, x, y):
        global resultado_det
        resultado_temp = 1
        for pos in range(3):
            if x > 2:
                x = 0
            if y > 2:
                y = 0
            resultado_temp = resultado_temp * matrix_1[x][y]
            x = x+1
            y = y+1
        resultado_det = resultado_det + resultado_temp

    def lado_b(matrix_1, x, y):
        global resultado_det
        resultado_temp = 1
        determinante = 0
        for pos in range(3):
            if x > 2:
                x = 0
            if y < 0:
                y = 2
            resultado_temp = resultado_temp * matrix_1[x][y]
            x = x+1
            y = y-1
        resultado_det = resultado_det - resultado_temp

    temp_1 = threading.Thread(target=lado_a, args=(matrix_1, 0, 0))
    temp_2 = threading.Thread(target=lado_a, args=(matrix_1, 0, 1))
    temp_3 = threading.Thread(target=lado_a, args=(matrix_1, 0, 2))
    temp_4 = threading.Thread(target=lado_b, args=(matrix_1, 0, 2))
    temp_5 = threading.Thread(target=lado_b, args=(matrix_1, 0, 0))
    temp_6 = threading.Thread(target=lado_b, args=(matrix_1, 0, 1))
    temp_1.setDaemon = True
    temp_2.setDaemon = True
    temp_3.setDaemon = True
    temp_4.setDaemon = True
    temp_5.setDaemon = True
    temp_6.setDaemon = True
    temp_1.start()
    temp_2.start()
    temp_3.start()
    temp_4.start()
    temp_5.start()
    temp_6.start()
    temp_1.join()
    temp_2.join()
    temp_3.join()
    temp_4.join()
    temp_5.join()
    temp_6.join()

    return resultado_det

def transpuesta(matrix):

    time.sleep(.500)
    print("[MATRIZ TRANSPUESTA]\n")

    for x in range(size):
        for y in range(size):
            print('['+str(matrix[y][x]), end=']\t')
        print()
    print()

def inversa(matrix_1): #terminado pero algo genera error en los calculos
    global matrix_temp
    matrix_temp = matrix_1

    resultado_det = determinante(matrix_1)

    matrix_temp[0][0] =  1 * ((int(matrix_1[1][1]) * int(matrix_1[2][2])) - (int(matrix_1[1][2]) * int(matrix_1[2][1])))
    matrix_temp[0][1] = -1 * ((int(matrix_1[0][1]) * int(matrix_1[2][2])) - (int(matrix_1[2][1]) * int(matrix_1[0][2])))
    matrix_temp[0][2] =  1 * ((int(matrix_1[0][1]) * int(matrix_1[1][2])) - (int(matrix_1[1][1]) * int(matrix_1[0][2])))
    matrix_temp[1][0] = -1 * ((int(matrix_1[1][0]) * int(matrix_1[2][2])) - (int(matrix_1[2][0]) * int(matrix_1[1][2])))
    matrix_temp[1][1] =  1 * ((int(matrix_1[0][0]) * int(matrix_1[2][2])) - (int(matrix_1[2][0]) * int(matrix_1[0][2])))
    matrix_temp[1][2] = -1 * ((int(matrix_1[0][0]) * int(matrix_1[1][2])) - (int(matrix_1[1][0]) * int(matrix_1[0][2])))
    matrix_temp[2][0] =  1 * ((int(matrix_1[1][0]) * int(matrix_1[2][1])) - (int(matrix_1[2][0]) * int(matrix_1[1][1])))
    matrix_temp[2][1] = -1 * ((int(matrix_1[0][0]) * int(matrix_1[2][1])) - (int(matrix_1[2][0]) * int(matrix_1[0][1])))
    matrix_temp[2][2] =  1 * ((int(matrix_1[0][0]) * int(matrix_1[1][1])) - (int(matrix_1[1][0]) * int(matrix_1[0][1])))

    for x in range(3):
        for y in range(3):
            matrix_temp[x][y] = matrix_temp[x][y] * (1/resultado_det)

    print_matrix(matrix_temp, "[INVERSA]")

def multiplicar(matrix, num_multi):

    def multip(matrix, x, num_multi):
        for pos in range(3):
            matrix[x][pos-1] = int(matrix[x][pos-1]) * int(num_multi)

    temp_1 = threading.Thread(target=multip, args=(matrix_1, 0, num_multi))
    temp_2 = threading.Thread(target=multip, args=(matrix_1, 1, num_multi))
    temp_3 = threading.Thread(target=multip, args=(matrix_1, 2, num_multi))
    temp_1.setDaemon = True
    temp_2.setDaemon = True
    temp_3.setDaemon = True
    temp_1.start()
    temp_2.start()
    temp_3.start()
    temp_1.join()
    temp_2.join()
    temp_3.join()
    return matrix

def elevada(matrix, num_elev): #terminado pero algo genera error en los calculos
    global matrix_temp1, matrix_temp2
    matrix_temp1 = matrix
    matrix_temp2 = matrix

    def elevar_pos(matrix, x, y):
        global matrix_temp1, matrix_temp2, temp
        print(int(matrix[x][y]))
        temp1 = int(matrix_temp1[0][y]) * int(matrix_temp2[x][0])
        temp2 = int(matrix_temp1[1][y]) * int(matrix_temp2[x][1])
        temp3 = int(matrix_temp1[2][y]) * int(matrix_temp2[x][2])

        matrix[x][y] = temp1 + temp2 + temp3
        # matrix[x][y] = (int(matrix_temp1[0][y]) * int(matrix_temp2[x][0])) + (int(matrix_temp1[1][y]) * int(matrix_temp2[x][1])) + (int(matrix_temp1[2][y]) * int(matrix_temp2[x][2]))

    for pos in range(int(num_elev)-1):
        temp_1 = threading.Thread(target=elevar_pos, args=(matrix, 0, 0))
        temp_2 = threading.Thread(target=elevar_pos, args=(matrix, 0, 1))
        temp_3 = threading.Thread(target=elevar_pos, args=(matrix, 0, 2))
        temp_4 = threading.Thread(target=elevar_pos, args=(matrix, 1, 0))
        temp_5 = threading.Thread(target=elevar_pos, args=(matrix, 1, 1))
        temp_6 = threading.Thread(target=elevar_pos, args=(matrix, 1, 2))
        temp_7 = threading.Thread(target=elevar_pos, args=(matrix, 2, 0))
        temp_8 = threading.Thread(target=elevar_pos, args=(matrix, 2, 1))
        temp_9 = threading.Thread(target=elevar_pos, args=(matrix, 2, 2))
        temp_1.setDaemon = True
        temp_2.setDaemon = True
        temp_3.setDaemon = True
        temp_4.setDaemon = True
        temp_5.setDaemon = True
        temp_6.setDaemon = True
        temp_7.setDaemon = True
        temp_8.setDaemon = True
        temp_9.setDaemon = True
        temp_1.start()
        temp_2.start()
        temp_3.start()
        temp_4.start()
        temp_5.start()
        temp_6.start()
        temp_7.start()
        temp_8.start()
        temp_9.start()
        temp_1.join()
        temp_2.join()
        temp_3.join()
        temp_4.join()
        temp_5.join()
        temp_6.join()
        temp_7.join()
        temp_8.join()
        temp_9.join()
        matrix_temp2 = matrix

    return matrix

def matriz_simetrica(matrix):

    simetrica = 0
    for x in range(size):
        for y in range(size):
            if matrix[y][x] != matrix[x][y]:
                simetrica = 1
    if simetrica == 1:
        print("\n\n[NO ES SIMETRICA]")
    else:
        print("\n\n[ES SIMETRICA]")

def matriz_identidad(matrix):
    global identica
    identica = 0

    def identidad(matrix):
        global identica
        for x in range(3):
            for y in range(3):
                if matrix[x-1][y-1] == 0:
                    identica = 1
                else:
                    identica = 0
                if matrix[0][0] == 1 or matrix[1][1] == 1 or matrix[2][2] == 1:
                    identica = 1

    temp = threading.Thread(target=identidad, args=[matrix])
    temp.setDaemon = True
    temp.start()
    temp.join()

    if identica == 1:
        print("[ES IDENTICA]")
    else:
        print("[NO ES IDENTICA]")


def multiplicar_ab(matrix_1, matrix_2): #terminado pero algo genera error en los calculos
    global matrix_3
    matrix_3 = matrix_1

    def multi_00(matrix_1, matrix_2):
        matrix_3[0][0] = (int(matrix_1[0][0]) * int(matrix_2[0][0]))   +   (int(matrix_1[0][1]) * int(matrix_2[1][0]))   +   (int(matrix_1[0][2]) * int(matrix_2[2][0]))
        print(matrix_3[0][0])
    def multi_01(matrix_1, matrix_2):
        matrix_3[0][1] = (int(matrix_1[0][0]) * int(matrix_2[0][1]))   +   (int(matrix_1[0][1]) * int(matrix_2[1][1]))   +   (int(matrix_1[0][2]) * int(matrix_2[2][1]))
        print(matrix_3[0][1])
    def multi_02(matrix_1, matrix_2):
        matrix_3[0][2] = (int(matrix_1[0][0]) * int(matrix_2[0][2]))   +   (int(matrix_1[0][1]) * int(matrix_2[1][2]))   +   (int(matrix_1[0][2]) * int(matrix_2[2][2]))
        print(matrix_3[0][2])

    def multi_10(matrix_1, matrix_2):
        matrix_3[1][0] = (int(matrix_1[1][0]) * int(matrix_2[0][0]))   +   (int(matrix_1[1][1]) * int(matrix_2[1][0]))   +   (int(matrix_1[1][2]) * int(matrix_2[2][0]))
        print(matrix_3[1][0])
    def multi_11(matrix_1, matrix_2):
        matrix_3[1][1] = (int(matrix_1[1][0]) * int(matrix_2[0][1]))   +   (int(matrix_1[1][1]) * int(matrix_2[1][1]))   +   (int(matrix_1[1][2]) * int(matrix_2[2][1]))
        print(matrix_3[1][1])
    def multi_12(matrix_1, matrix_2):
        matrix_3[1][2] = (int(matrix_1[1][0]) * int(matrix_2[0][2]))   +   (int(matrix_1[1][1]) * int(matrix_2[1][2]))   +   (int(matrix_1[1][2]) * int(matrix_2[2][2]))
        print(matrix_3[1][2])

    def multi_20(matrix_1, matrix_2):
        matrix_3[2][0] = (int(matrix_1[2][0]) * int(matrix_2[0][0]))   +   (int(matrix_1[2][1]) * int(matrix_2[1][0]))   +   (int(matrix_1[2][2]) * int(matrix_2[2][0]))
        print(matrix_3[2][0])
    def multi_21(matrix_1, matrix_2):
        matrix_3[2][1] = (int(matrix_1[2][0]) * int(matrix_2[0][1]))   +   (int(matrix_1[2][1]) * int(matrix_2[1][1]))   +   (int(matrix_1[2][2]) * int(matrix_2[2][1]))
        print(matrix_3[2][1])
    def multi_22(matrix_1, matrix_2):
        matrix_3[2][2] = (int(matrix_1[2][0]) * int(matrix_2[0][2]))   +   (int(matrix_1[2][1]) * int(matrix_2[1][2]))   +   (int(matrix_1[2][2]) * int(matrix_2[2][2]))
        print(matrix_3[2][2])

    multi_00(matrix_1, matrix_2)
    multi_01(matrix_1, matrix_2)
    multi_02(matrix_1, matrix_2)
    multi_10(matrix_1, matrix_2)
    multi_11(matrix_1, matrix_2)
    multi_12(matrix_1, matrix_2)
    multi_20(matrix_1, matrix_2)
    multi_21(matrix_1, matrix_2)
    multi_22(matrix_1, matrix_2)

    return matrix_3

def restar_ab(matrix_1, matrix_2):

    def restar(matrix_1, matrix_2, x):
        for pos in range(3):
            matrix_1[x][pos-1] = int(matrix_1[x][pos-1]) - int(matrix_2[x][pos-1])

    temp_1 = threading.Thread(target=restar, args=(matrix_1, matrix_2, 0))
    temp_2 = threading.Thread(target=restar, args=(matrix_1, matrix_2, 1))
    temp_3 = threading.Thread(target=restar, args=(matrix_1, matrix_2, 2))
    temp_1.setDaemon = True
    temp_2.setDaemon = True
    temp_3.setDaemon = True
    temp_1.start()
    temp_2.start()
    temp_3.start()
    temp_1.join()
    temp_2.join()
    temp_3.join()
    return matrix_1

def sumar_ab(matrix_1, matrix_2):

    def restar(matrix_1, matrix_2, x):
        for pos in range(3):
            matrix_1[x][pos-1] = int(matrix_1[x][pos-1]) + int(matrix_2[x][pos-1])

    temp_1 = threading.Thread(target=restar, args=(matrix_1, matrix_2, 0))
    temp_2 = threading.Thread(target=restar, args=(matrix_1, matrix_2, 1))
    temp_3 = threading.Thread(target=restar, args=(matrix_1, matrix_2, 2))
    temp_1.setDaemon = True
    temp_2.setDaemon = True
    temp_3.setDaemon = True
    temp_1.start()
    temp_2.start()
    temp_3.start()
    temp_1.join()
    temp_2.join()
    temp_3.join()
    return matrix_1


#SWITCH
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))
