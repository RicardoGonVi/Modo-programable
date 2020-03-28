##def buscar_archivo():
##        nombre = get()
##        if ".txt" not in nombre:
##            tk.messagebox.showerror("Error", "Error: Archivo no válido ingréselo nuevamente")

def mP():                                                           # main del modo programable   
    listaComandos = ["ejerota", "altura", "simultaneo", "pausa", "buscar", "reposo", "shot", "vertical", "n","s","e","o"]

    #inicializando la variable ejes, consta de grados en el eje horizontal y en el vertical
    ejes = []
    horiz= 0
    vert = 0
    ejes.append(horiz)
    ejes.append(vert)
    
    try :
        archivo= open("instrucciones.txt", "r")                     # abre el archivo
        comandos = archivo.readlines()                              # c/u lineas en una lista
        comandosCorrectos = []
        quitarEspacio = ""

        for i in comandos:
            quitarEspacio = i.strip("\n")                           # Quita el espacio
            comandosCorrectos.append(quitarEspacio)
        comandosCorrectos.append("reposo")                          # Obliga ir a reposo al finalizar

        for i in comandosCorrectos:
            existe = buscarEnComandos(i, listaComandos)             # valida que sea comando correcto comando
            if existe == False:
                return "No se reconoce algún comando"

        for i in comandosCorrectos:                                 # recorre los comandos uno a uno
            if "ejerota" in i:                                      # realiza el comando rotar eje
                ejes[0] = eje (i, ejes[0])
                if ejes[0] == False:
                    return "El comando de rotación presenta error en su sintaxis"
                else:
                    print("Rotando a: ", ejes[0], "grados")

            elif "altura" in i:                                     # realiza el comando dar altura
                ejes[1] = altura (i, ejes[1])
                if ejes[1] == False:
                    return "El comando de elevación presenta error en su sintaxis"
                else:
                    print("Subiendo a: ",ejes[1], "grados")

            elif "simultaneo" in i:                                 # rota el eje y da altura al mismo tiempo
                ejes = ambosejes (i, ejes[0], ejes[1])
                if ejes == False:
                    return "El comando simultáneo presenta error en su sintaxis"
                else:
                    print("Rotando a: ",ejes[0], "grados. ", "Girando a: ", ejes[1])

            elif "pausa" in i:                                      # comando pausar cierto tiempo
                tiempo = pausar (i)
                if tiempo == False:
                    return "El comando de tiempo presenta error en su sintaxis"
                else:
                    print("Pausa de: ", tiempo, "segundos")

            elif "buscar" in i:                                     # comando buscar color específico
                color = i.replace("buscar ", "")
                if color == "r":
                    print("Buscando rojo")
                elif color == "n":
                    print("Buscando negro")
                elif color == "a":
                    print("Buscando azul")
                elif color == "v":
                    print("Buscando verde")
                else:
                    return "El comando de color presenta error en su sintaxis"

            elif "reposo" == i:                                     # comando reposo
                print("Ir a reposo")
            elif "shot" == i:                                       # comando disparo
                print("Disparar")
            elif "vertical" == i:                                   # comando ir a posición vertical
                print("Mandar a posición vertical")
            elif "n" == i:                                          # comando ir al norte
                print("Ir al norte")
            elif "o" == i:                                          # comando ir al oeste
                print("Ir al oeste")
            elif "s" == i:                                          # comando ir al sur
                print("Ir al sur")
            elif "e" == i:                                          # comando ir al este
                print("Ir al este")
            else:
              return "No se reconoce algún comando ingresado"       # valida el comando

        archivo.close()                                             # cierra el archivo

    except FileNotFoundError:
        return "El archivo txt debe llamarse instrucciones"         # Valida el nombre del .txt

#FUNCIONES EXTRA
def buscarEnComandos (variable, lista):                             # funcion que valida la instrucción en la lista de comandos
    for i in lista:
        if i in variable:
            return True
    return False


#-------------------------------------------------------------------# funciones de los comandos
def eje (entrada, horiz):
    grados = entrada.replace("ejerota ", "")
    try:
        vi = int(grados)
        horiz = acumular(horiz, vi, 360)
        return horiz
    except:
        return False

def altura (entrada, vert):
    grados = entrada.replace("altura ", "")
    try:
        vi = int(grados)
        vert = acumular(vert, vi, 180)
        return vert
    except:
        return False

def acumular(actual, sumar, maximo):        # funcion que permite acumular el valor actual de los ejes
    if ((0 > sumar) or (sumar > maximo)):   # valida que solo existan entradas positivas y no sea mayor a lo que el servo permite fisicamente                     
        return False
    else:
        actual = actual + sumar             # actualiza valor
        if actual > maximo:                 # permite contener el valor dentro del rango fisico existente de c/u servos
            actual = actual - maximo
        return actual
    
def pausar (entrada):
    tiempo = entrada.replace("pausa ", "")
    try:
        valor = int(tiempo)
        return tiempo
    except:
        return False

def ambosejes (entrada, horiz, vert):    
    ambos = entrada.replace("simultaneo ", "")
    primer = ""
    segundo = ""
    contador = 0
    salida = []
    try:
        for i in ambos:
            if i == "," and contador == 0:  # separa la instruccion en un par ordenado
                contador = contador + 1
            else:
                if contador == 0:           # otorga el primer valor al mov horizontal
                    primer = primer + i
                elif contador == 1:         # otorga el segundo valor a la altura
                    segundo = segundo + i
        vi1 = int (primer)
        vi2 = int (segundo)
        horiz = acumular(horiz, vi1, 360)   # actualiza el valor horizontal
        vert = acumular(vert, vi2, 180)     # actualiza el valor de la altura
        salida.append(horiz)
        salida.append(vert)
        return salida                       # retorna el par ordenado
    except:
        return False   
