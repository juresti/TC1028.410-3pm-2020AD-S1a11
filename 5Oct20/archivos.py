def leerArchivo(nombre):
    archivo = open(nombre + ".txt","r")
    #todo = archivo.read(40) #lee todo como string
    #todo = archivo.readline() #lee una linea
    todo = archivo.readlines() #lee todo el archivo como lista
    print(todo)
    archivo.close()
    return todo
 
def escribirArchivo(nombre):
    miArch = open(nombre + ".txt","a")
    #miArch.write("NO es HOla MUndo")
    miArch.writelines(["este es\n","un archivo\n","de texto\n"])
    miArch.close()
    print("Archivo escrito a disco")
    
    