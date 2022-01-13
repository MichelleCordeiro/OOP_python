'''
## Exercício de Fixação 3

Considere uma classe para representar um `Ponto2D`.
Esta classe deve ter como atributos as coordenadas `x` e `y` do ponto.

Implemente o restante da classe como a seguir.

- Sobrecarregue o operador `+` (método mágico `__add__`): ele deve poder operar com o parâmetro sendo uma tupla de dois números ou uma instância de `Ponto2D`, retornando o resultado em um objeto da mesma classe do parâmetro.
- Sobrecarregue o operador `*` (método mágico `__mul__`): ele deve poder operar com o parâmetro sendo um número real ou um `Ponto2D`. No primeiro caso, o método deve retornar uma instância de `Ponto2D` resultante da multiplicação do parâmetro pelas coordenadas do ponto. No segundo caso, o método deve retornar o produto interno entre os dois pontos (o produto interno é igual ao produto das coordenadas x dos dois pontos somado com o produto das coordenadas y dos dois pontos).
- Sobrecarregue o operador `==` (método mágico `__eq__`): dele deve poder operar com o parâmetro sendo uma tupla de dois números ou uma instância de `Ponto2D`, retornando verdadeiro caso as coordenadas dos pontos sejam iguais ou falso caso contrário.

Utilize o código a seguir para testar o seu programa.
'''

class Ponto2D:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def __str__(self):
        return f'{self.__class__.__name__}{self._x, self._y}'
        
    def __add__(self, p):
        if isinstance(p, Ponto2D):
        #if type(p) is Ponto2D:
            res = Ponto2D(self._x + p._x, self._y + p._y)
        else:
            res = (self._x + p[0], self._y + p[1])
        return res
    
    def __mul__(self, p):
        if isinstance(p, Ponto2D):
            res = (self._x * p._x) + (self._y * p._y)
        else:
            res = Ponto2D(self._x * p, self._y * p)
        return res

if __name__ == '__main__':

    p1 = Ponto2D(2.0, -2.0)
    p2 = Ponto2D(-2.0, 2.0)
    print(p1 + p2)   # retorna Ponto2D
    print(p1 + (5.0, 5.0))   # retorna tupla

    p3 = p1 * 4   # multiplica por escalar, retorna Ponto2D
    print(p3)

    print(p1 * p2)   # produto interno/escalar, retorna nr. real

    print(p3 == (8.0, -8.0))
    print(p3 == p1)