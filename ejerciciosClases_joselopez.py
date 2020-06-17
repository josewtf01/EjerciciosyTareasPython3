class Figura:

    def __init__(self, NumeroLados=3):
        self.__NumeroLados = NumeroLados

    def ObtenerNumeroLados(self):
        print(self.__NumeroLados)


class Triangulo(Figura):

    def __init__(self,Base=1,Altura=1):
        super().__init__(3)
        self.__Base = Base
        self.__Altura = Altura
        self.__Area = (Base*Altura)/2

    def AdquirirArea(self):
        print(self.__Area)

    def AdquirirAltura(self):
        print(self.__Altura)

    def AdquirirBase(self):
        print(self.__Base)

class Rectangulo(Figura):

    def __init__(self,Base=1,Altura=1):
        super().__init__(4)
        self.__Base = Base
        self.__Altura = Altura
        self.__Area = Base*Altura
        self.__Perimetro = 2*Base + 2*Altura

    def AdquirirArea(self):
        print(self.__Area)

    def AdquirirAltura(self):
        print(self.__Altura)

    def AdquirirBase(self):
        print(self.__Base)

    def AdquirirPerimetro(self):
        print(self.__Perimetro)


class Estudiante:

    def __init__(self, Nombre="<nombre>",Correo="<correo>",Password="<password>"):
        self.__Nombre = Nombre
        self.__Correo = Correo
        self.__Password = Password

    def AdquirirNombre(self):
        print(self.__Nombre)

    def AdquirirCorreo(self):
        print(self.__Correo)

    def AdquirirPassword(self):
        print(self.__Password)

if __name__ == "__main__":
    x = Figura()
    print("Número de lados: ",end="")
    x.ObtenerNumeroLados()

    print("\n")
    y = Triangulo(3,4)
    print("Area: ", end="")
    y.AdquirirArea()
    print("Base: ", end="")
    y.AdquirirBase()
    print("Altura: ", end="")
    y.AdquirirAltura()

    print("\n")
    z = Rectangulo(5,7)
    print("Area: ", end="")
    z.AdquirirArea()
    print("Base: ", end="")
    z.AdquirirBase()
    print("Altura: ", end="")
    z.AdquirirAltura()
    print("Perimetro: ", end="")
    z.AdquirirPerimetro()
    print("\n")

    jose = Estudiante("José Luis","jl.lopezzaragoza@ugto.mx", "PadtsQuince")
    jose.AdquirirNombre()
    jose.AdquirirCorreo()
    jose.AdquirirPassword()
