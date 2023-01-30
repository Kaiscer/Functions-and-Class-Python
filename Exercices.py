
while True:
    print("Introduce el número del ejercicio que quieres ejecutar: (1 - 5 ) => ")
    option = int(input())
    match option:
        case 1:
            """
                Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa un número entero n y un carácter.
                Devolverá el carácter multiplicado por n.
                Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx". Tantas x como indique el número.
                """
            print("*** Generar Caracter n de Veces ***")


            def generate_n_characters(num, char):
                return num * char


            character = input("Introduce un caracter: => ")
            number = int(input("Introduce el número veces que vasmo a duplicar el caracter: => "))

            print(generate_n_characters(number, character))

        case 2:
            """
            Crea una función llamada histograma(lista_números) a la que se le pasa una lista de números enteros. 
            Se mostrará un histograma cuyas columnas midan el valor de los números.
            Por ejemplo: histograma([4, 9, 2,7]) debería imprimir lo siguiente:
            """


            def histogram(list_Num):
                print("El historograma queda de la siguente manera: \n")
                for x in list_Num:
                    print(x * "*")


            print("*** Histograma ***")

            listNum = []
            value = int(input("Cuantos Valores se van a introducir => "))
            for i in range(value):
                print(f"Introduce el valor {i + 1}: ")
                listNum.append(int(input()))

            histogram(listNum)

        case 3:
            """
            Escribe una función funcionLista(función, lista) que reciba otra función creada anteriormente y una lista, 
            y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
            Por ejemplo, la función que se le pasa calcula el cubo de un número.
            La lista que se pasa es una lista de números enteros. A cada número de la lista se le aplica la función y 
            se calculará el cubo de todos ellos, mostrándolos en otra lista nueva.
            Si la lista que se pasara fuera [1,2,3,4,5] la función devolvería [1,8,27,64,125]
            
            """
            print("*** Calcular el Cubo ***")


            def functionList(funct, list_Num):
                new_list = []
                for x in list_Num:
                    new_list.append(funct(x))
                return new_list


            def cub(num):
                return num ** 3


            print("Introduce los 5 número que deseas saber su valor al cubo: ")
            list_Num = []
            for i in range(5):
                list_Num.append(int(input()))

            print(functionList(cub, list_Num))

        case 4:
            """
            Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva un diccionario 
            con las palabras que contiene y su longitud.
            Por ejemplo, la función recibe la frase ‘Hola y adiós’ y devuelve 
            un diccionario de la forma {‘Hola’:4, ‘y’:1, ‘adiós’:5}
            """
            print("*** Diccionario con la longitud de una palabra ***")


            def wordLong(chainText):
                words = chainText.split()
                dictionary = {}

                for i in words:
                    dictionary[i] = len(i)
                print(dictionary)


            chain = input("Introduce una frase => ")
            wordLong(chain)

        case 5:
            """
            Escribe una función calificaPalabras(diccionario) que reciba un diccionario con las asignaturas y las notas 
            numéricas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas 
            y las calificaciones correspondientes a las notas con palabras.
            El criterio será el siguiente: nota <5→Suspenso; 5 <= nota < 7→Aprobado;
            7 <= nota < 9→Notable; 9 <= nota <=10→Sobresaliente. La nota no puede sobrepasar 10.
            Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4} y 
            devuelve el diccionario {'ANDROID’:’Notable’, ‘HILOS’:’Aprobado’, 
            ‘PYTHON’:’Sobresaliente’, ‘INTERFACES’:’Suspenso’ }
            """

            print("*** Asignaturas ***")


            def qualifications(subject):
                for x in subject:
                    if subject[x] < 5:
                        subject[x] = "Supenso"
                    elif subject[x] <= 5 or subject[x] < 7:
                        subject[x] = "Apobada"
                    elif subject[x] >= 7 or subject[x] <= 9:
                        subject[x] = "Notable"
                    elif subject[x] >= 9 or subject[x] <= 10:
                        subject[x] = "Sobresaliente"
                print(subject)

            print("¿Cuantas asignaturas vas a introducir? ")
            num = int(input())
            dictionary = {}
            for i in range(int(num)):
                print(f"Introduce la asignatura {i + 1}: ")
                key = input()
                print(f"Introduce la nota de la asignatura {i + 1}: ")
                value = float(input())
                dictionary[key] = value

            qualifications(dictionary)

        case _:
            print("Opción no válida")

    print("¿Deseas probar otro ejercicio? (S/N)")
    answer = input().upper()
    if answer == "S":
        continue
    else:
        print("See you later")
        break
