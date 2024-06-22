import os

Libros = []


def regis_libr():
    try:
        Nombre = input("Ingrese nombre del libro: ")
        Autor = input("Ingrese autor del libro")
        Año = input("Ingrese año de publicacion")
        SKU = input("Ingrese SKU")
        EstadoLibro = input("Ingrese estado del libro")
        if SKU == "" or  Autor == "" or Año == "" or SKU == "" <=0:
            raise  ValueError ("Error en los datos ingresados verifique e intente nuevamente")


        Libro = {
            'nombre': Nombre,
            'autor': Autor,
            'año' : Año,
            'sku': SKU,
            'estado': EstadoLibro,

        }
        Libros.append(Libro)
        print("Libro registrado exitosamente")
    except ValueError as e:
        print(e)


def ListLibr():
    if not Libros:
        print("No existe registro de libros.")
    else:
        for Libro in Libros:
            print(f"Nombre de libro: {Libro['nombre']}\t Autor:{Libro['autor']}\tAño:{Libro['año']}\tSku:{Libro['sku']}")


def registro():
    try:
        op = int(input("¿Como desea ver el registro?\n1. Detalle completo\n2. Nombre especifico\n3. SKU "))
        if op == 1 :
            filename == "Libros.txt"
        elif op == 2:
            nombre = input("Ingrese nombre del libro para ver detalle (SIN SKU)").lower()
            filename = ("Detalle_{nombre}.txt")
        else:
            raise ValueError("Opción Fuera de rango intente nuevamente")
        with open(filename, "w") as archivo:
            for Libro in Libros:
                if op == 1 or (op ==2 and Libro['nombre'].lower() == Libro):
                    archivo.write(f"Nombre libro: {Libro['libro']}\t Autor Libro: {Libro['autor']}\t Año:{Libro['año']}\t SKU:  {Libro['sku']}")
        print(f"Detalle generado exitosamente en : {os.getcwd()}")    
    except ValueError as e:
        print(e)

def prestamo():
    while True:
        try: 
            print("Este es el registro de libros:  ")
            print(Libros)
            print("1. Pedir Libro mediante SKU\n2 Salir del")
            op= int(input("Ingrese una opcion:\t"))
            
            if op ==1:
                SKU = input("Ingrese SKU")
                ("Su Libro ha sido pedido : {SKU}")
            
            if SKU == "" <=0:
                raise ValueError("SKU invalido intente otra vez")

            elif op ==2:
                print("Programa finalizado\n Desarrollado por Camilo Aguilar\nRUN: 21.602.549-0")
                break


            else:
                print("Opcion Invalida intente nuevamente")
        except ValueError as e:
            print(e)







def menu1():
    while True:
        try: 
            print("\n REGISTRO LIBROS\n")
            print("1. Registrar Libro\n2 Listar los Libros ya registrados\n3 Imprimir el registro\n4 Menu Prestamo\n5 Salir del programa")
            op= int(input("Ingrese una opcion:\t"))
            if op ==1:
                regis_libr()
            elif op ==2:
                ListLibr()
            elif op == 3:
                registro()
            elif op == 4: 
                prestamo() 
                break

            elif op == 5:
                print("Programa finalizado\n Desarrollado por Camilo Aguilar\nRUN: 21.602.549-0 ")
                break
            else:
                print("Opcion Invalida intente nuevamente")
        except ValueError as e:
            print(e)
