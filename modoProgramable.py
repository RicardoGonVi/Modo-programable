def mP():                                                           #main
    listaComandos = ["ejerota", "desplazar", "simultaneo", "pausa", "color", "reposo", "shot", "vertical"]
    try :
        archivo= open("instrucciones.txt", "r")                     #abre el archivo
        comandos = archivo.readlines()                              #c/u lineas en una lista
        comandosCorrectos = []
        quitarEspacio = ""
        
        for i in comandos:                                          
            quitarEspacio = i.strip("\n")                           #Quita el espacio
            comandosCorrectos.append(quitarEspacio)
        print(comandosCorrectos)
        
        for i in comandosCorrectos:
            existe = buscarEnComandos(i, listaComandos)             #valida que sea comando correcto comando                
            if existe == False:
                return "No se reconoce algún comando"
                
        
        for i in comandosCorrectos:                                 
            if "ejerota" in i:
                print(1)
            elif "desplazar" in i:
                print(2)
            elif "simultaneo" in i:
                print(3)
            elif "pausa" in i:
                print(4)
            elif "color" in i:
                print(5)
            elif "reposo" == i:
                print("Ir a reposo")
            elif "shot" == i:
                print("Disparar")
            elif "vertical" == i:
                print("Mandar a posición vertical")
            else:
              return "No se reconoce algún comando ingresado"    #valida el comando

    
        archivo.close()                                             #cierra el archivo

    except FileNotFoundError:
        return "El archivo txt debe llamarse instrucciones"         #Valida el nombre del .txt


def buscarEnComandos (variable, lista):                                           
    for i in lista:
        if i in variable:
            return True
    return False
