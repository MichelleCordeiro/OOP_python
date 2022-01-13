'''
## Exercício de Fixação 2

Considerando a hierarquia de animais desta aula:

- Implemente o método abstrato `pode_voar` (que deve retornar `True/False`) na classe `Ave`.
- Implemente na classe `Ave` um método de classe que recebe como parâmetro uma lista de  
  aves `L` e retorna uma sublista de  `L` com 
  as aves que podem voar.
- Adicione um atributo e propriedade `peso` na classe `Animal`.
- Implemente um método de classe que retorne a média dos pesos de uma 
  lista de animais. 
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    '''Classe abstrata'''
    def __init__(self, peso):
        self.nasce()
        self.peso = peso

    @abstractmethod
    def nasce(self):
        pass

    def morre(self):
        print('Animal morreu')

    @abstractmethod
    def emite_som(self):
        pass        
    
    def media_pesos(self, lista):
        soma = self.peso
        for a in lista:
            soma += a.peso
        return soma / (len(lista)+1)

class Mamifero(Animal):
    '''Abstrata: não implementa o método emite_som'''
    
    def amamenta(self):
        print('Mamífero amamentou')
        
    def nasce(self):
        print('Mamífero nasceu do ventre')

class Ave(Animal):
    '''Abstrata: não implementa o método emite_som'''
        
    def voa(self):
        print('Ave voou')
        
    def nasce(self):
        print('Ave nasceu do ovo')
    
    @abstractmethod
    def pode_voar(self):
        pass
    
    def aves_q_voam(self, aves):
        if self.pode_voar():
            aves_voam = [self]
        for l in aves:
            if l.pode_voar():
                aves_voam.append(l)
        return aves_voam

class Gato(Mamifero):
    
    def emite_som(self):
        print('Miau')

class Cachorro(Mamifero):
    
    def emite_som(self):
        print('Au')

class Ornitorrinco(Mamifero):
    
    def emite_som(self):
        print('Prprpr')
        
    def nasce(self):
        print('Ornitorrinco nasceu do ovo')

class Pinguim(Ave):
    
    def emite_som(self):
        print('Quack')
        
    def voa(self):
        print('Pinguim não voa')
        
    def pode_voar(self):
        return False

class Aguia(Ave):
    
    def emite_som(self):
        print('In')
    
    def pode_voar(self):
        return True

if __name__ == "__main__":
    g = Gato(5)
    c = Cachorro(20)
    o = Ornitorrinco(15)
    p = Pinguim(4)
    a = Aguia(6)
    a.voa()
    p.voa()
    animais = [g,c,o,p,a]

    for a in animais:
        print(f'Nome da classe: {a.__class__.__name__}') # So para testar, imprimimos o nome da classe
        a.emite_som()
        a.morre()
        
    print(a.pode_voar())
    print(p.pode_voar())
    a2 = Aguia(10)
    a3 = Aguia(3)
    lista = [p, a2, a3]
    #print(a.aves_q_voam([p, a2, a3]))
    print(f'{a.aves_q_voam(lista)}')
    
    print(f'Media = {a2.media_pesos([g,c,o,p,a])}')