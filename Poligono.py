"""
• Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.
Al crear un objeto, en el constructor __init__ ( ), se indica el número de lados que va a tener y se crea una lista
que va a tener ese número de elementos cuyos valores iniciales serán 0.
• La clase Poligono() tendrá un método llamado darlados( ) que le pedirá al usuario que
introduzca uno a uno los valores de todos los lados.
• La clase Polígono() tendrá otro método llamado verlados( ) que
mostrará uno a uno los valores introducidos de todos los lados.
• Se va a crear una clase llamada Triangulo() que hereda de la clase Poligono().
Al crear un objeto triangulo, se invoca al constructor de la clase Poligono() al que se indica el número de lados = 3.
• La clase Triangulo() tendrá un método area( ) que calcule y muestre el área del triángulo.
Puede ser cualquier tipo de triángulo. Puedes usar la fórmula de Herón.
• La clase Triangulo() tendrá un método perimetro( ) que
calcule y muestre el perímetro del triángulo (suma de sus lados).
• Crea dos objetos de la clase Triangulo() y muestra el resultado de ejecutar todos
los métodos tanto de la clase Polígono() como de la clase Triangulo().
"""


class Poligono:
    def __init__(self, num_side):
        if num_side < 3:
            print("Error: el polígono debe tener al menos 3 lados.")
        else:
            self.num_side = num_side
            for i in range(num_side):
                self.side = [0] * num_side

    def darLados(valSide, pol):
        for i in range(pol.num_side):
            valSide = int(input(f'Introduce el valor del lado {i + 1}: '))
            pol.side[i] = valSide

    def verLados(pol):
        for i in range(pol.num_side):
            print(f'El valor del lado {i + 1} es {pol.side[i]}')


class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)

    def area(self):
        a = self.side[0]
        b = self.side[1]
        c = self.side[2]
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f'El área del triángulo es {area}')

    def perimetro(self):
        perimetro = sum(self.side)
        print(f'El perímetro del triángulo es {perimetro}')


print("Punto 1: \n")
pol = int(input("Introduce el número de lados del polígono: "))
pol = Poligono(pol)
print(pol.side)

print("\nPunto 2: \n")
valSide = 0
Poligono.darLados(valSide, pol)
print(pol.side)

print("\nPunto 3: \n")
Poligono.verLados(pol)

print("\nPunto 4: \n")
tri = Triangulo()
print(tri.side)

print("\nPunto 5: \n")
print("Introduce los valores de los lados del triángulo: ")
Triangulo.darLados(valSide, tri)
Triangulo.verLados(tri)
Triangulo.area(tri)

print("\nPunto 6: \n")
Triangulo.perimetro(tri)

print("\nPunto 7: \n")
tri2 = Triangulo()
print("Introduce los valores de los lados del triángulo: ")
Triangulo.darLados(valSide, tri2)
Triangulo.verLados(tri2)
Triangulo.area(tri2)
Triangulo.perimetro(tri2)

