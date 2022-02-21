def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("No se encontró el archivo config.txt", err)
    except IsADirectoryError:
        print("Se encontró a config.txt pero es un directorio, no se puede leer")
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos bajo carga pesada, no se puede terminar de leer al archivo de configuración.")

#Aunque puedes agrupar excepciones, solo debes hacerlo cuando no sea necesario controlarlas individualmente. Evita agrupar muchas excepciones para proporcionar un mensaje de error generalizado.


if __name__ == '__main__':
    main()

def main2():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")
            
main2()