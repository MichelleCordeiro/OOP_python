'''
Prática 1.3: classe Conjunto¶
A biblioteca padrão Python possui uma classe para representar um conjunto, chamada de set. Entretanto, ao invés de usar os métodos desta classe nesta aula, você deve implementá-los.

Para isto, encapsule uma lista Python (list) para conter os elementos do conjunto como o único atributo da classe e implemente os métodos solicitados a seguir:

  adiciona: Adiciona objeto ao conjunto. Não faz nada se o objeto já estiver presente.
  interseccao: Retorna conjunto intersecção entre o conjunto e um conjunto c passado como parâmetro.
  __contains__: Retorna verdadeiro se elementoe está no conjunto. Torna possível utilizar o operador in.
  __str__: Retorna uma str representando o conjunto com todos os elementos separados por vírgulas entre chaves.
  ehVazio: Retorna verdadeiro se o conjunto é vazio.

Utilize o código a seguir como ponto de partida.


Resposta esperada para a execução acima:

True
{}
{a, b, c}
True
False
True
{h, i, b}
{b}
'''

class Conjunto:
    '''Representa um conjunto de objetos'''
    
    def __init__(self):
        self.__lista = []
        
    def adiciona(self, valor):
        if valor not in self.__lista:
            self.__lista.append(valor)
            
    def interseccao(self, conj):
        lista_aux = Conjunto()
        for item in self.__lista:
            conj = str(conj)
            if item in conj:
                lista_aux.adiciona(item)
        return lista_aux
    
    #def __contains__(self, arg):
        #if arg in self.__lista:
            #return True
        #else:
            #return False
    
    def __contains__(self, arg):
        return arg in self.__lista    
            
    def __str__(self):
        x = '{'
        for i,item in enumerate(self.__lista):
            x += f'{item}'
            if i != len(self.__lista)-1:
                x += f', '
        
        x += '}'
        return x
    
    #ef ehVazio(self):
        #eturn not(any(self.__lista))
    
    def ehVazio(self):
        return not bool(len(self.__lista))

    
if __name__ == '__main__':
    c1 = Conjunto()
    print(c1.ehVazio())
    print(c1)
    c1.adiciona('a')
    c1.adiciona('b')
    c1.adiciona('c')
    print(c1)
    print('a' in c1)
    print('g' in c1)
    c2 = Conjunto()
    c2.adiciona('h')
    c2.adiciona('i')
    c3 = c1.interseccao(c2)
    print(c3.ehVazio())
    c2.adiciona('b')
    print(c2)
    c3 = c1.interseccao(c2)
    print(c3)