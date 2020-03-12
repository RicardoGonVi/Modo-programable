def mProgramable():
    ##class

    comandosExistentes = ["ejerota", "desplazar", "simultaneo", "color", "shot", "pausa"]
    try :
        archivo= open("instrucciones.txt", "r")                     #abre el archivo
        comandos = archivo.readlines()                              #c/u lineas en una lista
        comandosCorrectos = []
        quitarEspacio = ""
        
        for i in comandos:                                          
            quitarEspacio = i.strip("\n")                           #Quita el espacio

            if quitarEspacio not in comandosExistentes:
                 return "No se reconoce algún comando ingresado"    #valida el comando

            comandosCorrectos.append(quitarEspacio)

        
        for i in comandosCorrectos:                                 
            if (i == "ejerota"):
                print(1)
            elif (i == "desplazar"):
                print(2)
            elif (i == "simultaneo"):
                print(3)
            elif (i == "color"):
                print(4)
            elif (i == "shot"):
                print(5)
            elif i == "pausa":
                print(6)
            else:
                return "No se reconoce algún comando ingresado"    #valida el comando
        
       

  
    
        archivo.close()                                             #cierra el archivo

    except FileNotFoundError:
        return "El archivo txt debe llamarse instrucciones"         #Valida el nombre del .txt


def aa (comandos, comandosExistentes):
    for i in comandos:                                          
            quitarEspacio = i.strip("\n")                           #Quita el espacio
        for j in comandosExistentes:
            if j in quitarEspacio:
                return True
            
    return "No se reconoce algún comando ingresado"    #valida el comando

            comandosCorrectos.append(quitarEspacio)
            
