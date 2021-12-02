from abc import ABC, abstractmethod
import math

class Figura(ABC):
    
    @abstractmethod
    def __init__(self, num):
        self._num = num
    
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

        
class TrianguloEquilatero(Figura):
    def __init__(self, num):
        super().__init__(num)
    
    def area(self):
        area_triag = self._num * math.sqrt(3) / 4
        print(f'Área do Triangulo Equilatero = {round(area_triag,2)}')
    
    def perimetro(self):
        print(f'Perímetro do Triangulo Equilatero = {3 * self._num}')
    
    def __repr__(self):
        return f'\nTriangulo Equilatero com lado {self._num} criado'
    
class Quadrado(Figura):
    def __init__(self, num):
        super().__init__(num)
        
    def area(self):
        print(f'Área do Quadrado = {pow(self._num,2)}')

    def perimetro(self):
        print(f'Perímetro do Quadrado = {4 * self._num}')
    
    def __repr__(self):
        return f'\nQuadrado com lado {self._num} criado'


class Circulo(Figura):
    def __init__(self, num):
        super().__init__(num)
        
    def area(self):
        print(f'Área do Circulo = {pow(self._num,2) * 3.14}')
    
    def perimetro(self):
        print(f'Perímetro do Circulo = {round(2 * 3.14 * self._num, 2)}')
    
    def __repr__(self):
        return f'\nCirculo com raio {self._num} criado'
    
    
if __name__ == "__main__":

    f1 = TrianguloEquilatero(3)
    print(f1)
    f1.area()
    f1.perimetro()

    f2 = Quadrado(5)
    print(f2)
    f2.area()
    f2.perimetro()
    
    f3 = Circulo(5)
    print(f3)
    f3.area()
    f3.perimetro()