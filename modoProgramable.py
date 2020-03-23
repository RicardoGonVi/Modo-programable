def mP():                                                           #main
    listaComandos = ["ejerota", "altura", "simultaneo", "pausa", "buscar", "reposo", "shot", "vertical"]
    try :
        archivo= open("instrucciones.txt", "r")                     #abre el archivo
        comandos = archivo.readlines()                              #c/u lineas en una lista
        comandosCorrectos = []
        quitarEspacio = ""
        
        for i in comandos:                                          
            quitarEspacio = i.strip("\n")                           #Quita el espacio
            comandosCorrectos.append(quitarEspacio)
        comandosCorrectos.append("reposo")                          #Obliga ir a reposo al finalizar
        
        for i in comandosCorrectos:
            existe = buscarEnComandos(i, listaComandos)             #valida que sea comando correcto comando                
            if existe == False:
                return "No se reconoce algún comando"
        
        for i in comandosCorrectos:                                 #recorre los comandos uno a uno
            if "ejerota" in i:                                      #realiza el comando rotar eje
                grotacion = eje (i)
                if grotacion == False:
                    return "El comando de rotación presenta error en su sintaxis"
                else:
                    print("Rotar: ",grotacion, "grados")
                    
            elif "altura" in i:                                     #realiza el comando dar altura
                galtura = altura (i)
                if galtura == False:
                    return "El comando de elevación presenta error en su sintaxis"
                else:
                    print("Altura: ",galtura, "grados")
                
            elif "simultaneo" in i:                                 #rota el eje y da altura al mismo tiempo
                ejes = ambosejes (i)
                if ejes == False:
                    return "El comando simultáneo presenta error en su sintaxis"
                else:
                    print("Rotar: ",ejes[0], "grados. ", "Alzar: ", ejes[1])
                    
            elif "pausa" in i:                                      #comando pausar cierto tiempo                                
                tiempo = pausar (i)
                if tiempo == False:
                    return "El comando de tiempo presenta error en su sintaxis"
                else:
                    print("Pausa de: ", tiempo, "segundos")
                    
            elif "buscar" in i:                                     #comando buscar color específico
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
                    
            elif "reposo" == i:                                     #comando reposo
                print("Ir a reposo")
            elif "shot" == i:                                       #comando disparo
                print("Disparar")
            elif "vertical" == i:                                   #comando ir a posición vertical
                print("Mandar a posición vertical")
            else:
              return "No se reconoce algún comando ingresado"       #valida el comando

    
        archivo.close()                                             #cierra el archivo

    except FileNotFoundError:
        return "El archivo txt debe llamarse instrucciones"         #Valida el nombre del .txt

#FUNCIONES EXTRA
def buscarEnComandos (variable, lista):                             #funcion que valida la instrucción en la lista de comandos                                     
    for i in lista:
        if i in variable:
            return True
    return False


#-------------------------------------------------------------------#funciones de los comandos
def eje (entrada):
    grados = entrada.replace("ejerota ", "")
    try:
        int(grados)
        return grados
    except:
        return False

def altura (entrada):
    grados = entrada.replace("altura ", "")
    try:
        int(grados)
        return grados
    except:
        return False

def pausar (entrada):
    tiempo = entrada.replace("pausa ", "")
    try:
        int(tiempo)
        return tiempo
    except:
        return False

def ambosejes (entrada):
    ambos = entrada.replace("simultaneo ", "")
    primer = ""
    segundo = ""
    contador = 0
    salida = []
    try:
        for i in ambos:
            if i == "," and contador == 0:
                contador = contador + 1
            else:
                if contador == 0:
                    primer = primer + i
                elif contador == 1:
                    segundo = segundo + i
        int (primer)
        int (segundo)        
        salida.append(primer)
        salida.append(segundo)
        return salida
    
    except:
        return False
