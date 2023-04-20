import os
import pandas as pd
import shutil
from colorama import Fore, Style


print(Fore.YELLOW + "                    © Daniel Rueda ®    " + Style.RESET_ALL)
print(Fore.YELLOW + '                    █║▌│█│║▌║││█║▌║▌║' + Style.RESET_ALL)
print(Fore.YELLOW + '         ▂ ▃ ▅ ▆ █ Tecnico en Sistemas █ ▆ ▅ ▃ ▂ '+ Style.RESET_ALL)
print('\n')

print('El programa es una herramienta que facilita la organización de archivos en una carpeta. El programa tiene la capacidad de crear carpetas con nombres específicos y mover archivos específicos a la ruta de esas carpetas.\nPara utilizar el programa el usuario debe proporcionar la ruta especifica de donde se encuentran los archivos.\n')

print(Fore.RED + '𝙄𝙉𝙎𝙏𝙍𝙐𝘾𝘾𝙄𝙊𝙉𝙀𝙎' + Style.RESET_ALL)

print('1. El nombre de los archivos debe estar separado por una coma (,) que será la referencia para tomar el nombre de la carpeta donde sé guardará el archivo.\n2. El programa soporta los siguientes tipos de archivos.\n\n•pdf\n•xlsx\n•docx\n•xls\n•jpg\n•png\n')


comprobacion = True
while comprobacion:
    seleccion = int(input('Seleccione el numero del tipo de documento:\n1. pdf\n2. xlsx\n3. docx\n4. jpg\n5. png\n\nQue tipo de documento es: '))
    if seleccion < 6:
            ruta = input('Ingrese la ruta donde se encuentran los archivos: ')
            ruta = ruta.replace("\\", "/")
            comprobacion = False
            if seleccion == 1:
                extension = "pdf"
            elif seleccion == 2:
                extension = "xlsx"
            elif seleccion == 3:
                extension = "docx"
            elif seleccion == 4:
                extension = "jpg"
            else:
                extension = "png"
    else:
        print('\nEl numero ingresado no es correcto, por favor intenta de nuevo\n')


def aplicacion(extension):
    lista_archivos_extension = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(f'.{extension}'):
            lista_archivos_extension.append(archivo)

    nombres_sin_extension = []

    for nombre in lista_archivos_extension:
        nombre_archivo, extension = nombre.split(',')
        nombres_sin_extension.append(nombre_archivo)

    #quitar duplicados
    nombres_sin_extension_sin_duplicados = list(set(nombres_sin_extension))

    diccionario = {'Nombres': nombres_sin_extension_sin_duplicados}

    df = pd.DataFrame(diccionario)


    #Creando las carpetas con la lista generada

    for nombre in nombres_sin_extension_sin_duplicados:
        carpeta = os.path.join(ruta, nombre)
        os.makedirs(carpeta, exist_ok=True)

    #moviendo los archivos a cada carpeta segun su nombre
    ruta_archivos = ruta
    ruta_carpetas = ruta

    for archivo in lista_archivos_extension:
        name = archivo.split(',')[0]
        for carpeta in nombres_sin_extension_sin_duplicados:
            if name in carpeta:
                shutil.move(os.path.join(ruta_archivos, archivo), os.path.join(ruta_carpetas, carpeta, archivo))

aplicacion(extension)
