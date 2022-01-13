class PreProcessador():
    def __init__(self, texto):
        self.__texto = texto
        self._lista_palavras = []
    
    def __str__(self):
        #return str(self._lista_palavras)
        return ''
                
    def processa(self):
        #self.__lista_palavras = self.__texto.strip()
        self._lista_palavras = self.__texto.split(" ")
        
        symbols = "!@#$,;.:"
        for i in range(len(self._lista_palavras)):
            for s in symbols:
                self._lista_palavras[i] = self._lista_palavras[i].replace(s, "")
            self._lista_palavras[i] = self._lista_palavras[i].lower()
        #print("metodo processa de PreProcessador")
            
    
class ContadorPalavras(PreProcessador):
    def __init__(self, texto):
        self.__ocorrencias = {}
        super().__init__(texto)
    
    def __str__(self):
        r = f'Frequencia das palavras:'
        for i in self.__ocorrencias:
            r += '\n' + i + ': ' + str(self.__ocorrencias[i]) + ' vezes'
        return f'{r}'

    def processa(self):
        counts = []
        super().processa()
        
        for w in self._lista_palavras:
            counts.append(self._lista_palavras.count(w))
        
        self.__ocorrencias = dict(zip(self._lista_palavras, counts))
        #print("metodo processa de ContadorPalavras")


class Tradutor(PreProcessador):
    def __init__(self, texto):
        self.__traducoes = {'olá': 'hello', 'este': 'this', 'é': 'is', 'um': 'a', 'exemplo': 'example', 'de': 'of', 
                            'texto': 'text', 'com': 'with', 'termos': 'terms', 'repetidos': 'repeated', 'possui': 'has',  
                            'vários': 'varius'}
        self.__lista_palavras_trad = []
        super().__init__(texto)
    
    def __str__(self):
        r = f'\nTradução robótica:\n'
        r += str(' '.join(self.__lista_palavras_trad))
        return r
        
    def processa(self):
        super().processa()

        for i,w in enumerate(self._lista_palavras):
            for k,v in self.__traducoes.items():
                if w == k:
                    self.__lista_palavras_trad.append(self._lista_palavras[i].replace(w, v))
        #print("metodo processa de Tradutor")


class ProcessadorTexto(ContadorPalavras, Tradutor):
    def __init__(self, texto):
        super().__init__(texto)
        
    def processa(self):
        #print("metodo processa de ProcessadorTexto")
        super().processa()
        #ContadorPalavras.imprime(self)
        #Tradutor.imprime(self)
        print(ContadorPalavras.__str__(self))
        print(Tradutor.__str__(self))


if __name__ == '__main__':
    #Descomente a seguir para testar apenas a classe PreProcessador
    preprocessador = PreProcessador('OLá! Este é um exemplo de texto com termos repetidos.'
                                     ' Este texto possui vários termos repetidos:'
                                     ' este, Este, ESte, esTE!')
    #preprocessador.processa()
    #print(preprocessador)
    
    # Descomente a seguir para testar apenas a classe ContadorPalavras
    contador = ContadorPalavras('OLá! Este é um exemplo de texto com termos repetidos.'
                                 ' Este texto possui vários termos repetidos:'
                                 ' este, Este, ESte, esTE!')
    #contador.processa()
    #print(contador)

    # Descomente a seguir para testar apenas a classe Tradutor
    tradutor = Tradutor('OLá! Este é um exemplo de texto com termos repetidos.'
                         ' Este texto possui vários termos repetidos:'
                         ' este, Este, ESte, esTE!')
    #tradutor.processa()
    #print(tradutor)

    processadortexto = ProcessadorTexto('OLá! Este é um exemplo de texto com termos repetidos.'
                                        ' Este texto possui vários termos repetidos:'
                                        ' este, Este, ESte, esTE!')
    #print("\nMRO de ProcessadorTexto: ", ProcessadorTexto.mro())
    processadortexto.processa()