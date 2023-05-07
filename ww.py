class Object:
    def __init__(self, forma, color, tama):
        self.forma = forma
        self.color = color
        self.tama = tama

    def accion(self):
        print("yo soy " + self.forma, self.color, "y", self.tama)


b1 = Object("cuadrado", "rojo", "grande")

b1.accion()
