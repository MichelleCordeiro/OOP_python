'''
Saída esperada para o código acima:

31/12/2012 - Ao avancar um dia vamos para a data:  01/01/2013
2012 é ano Bissexo:
28/02/2012 - Ao avancar um dia vamos para a data:  29/02/2012
28/02/2013 - Ao avancar um dia vamos para a data:  01/03/2013
1900 não é ano Bissexo. O número é divisivel por 100 mas não por 400: 
28/02/1900 - Ao avancar um dia vamos para a data:  01/03/1900
2000 foi um é ano Bissexo. O número é divisivel por 400: 
28/02/2000 - Ao avancar um dia vamos para a data:  29/02/2000
'''


class Calendario():

    ultimo_dia_mes = (31,28,31,30,31,30,31,31,30,31,30,31)

    @staticmethod
    def ehBissexto(ano):
        """ 
        O metodo retorna True se o parametro ano é ano bissexto, False caso contrario
        """
        # para ser ano bissexto (fev=29dias):
        #     é ano % 4 == 0
        # nao é ano % 100 == 0
        # nao é ano % 400 == 0
        if ((ano % 4 == 0) and not(ano % 100 == 0)) or (ano % 400 == 0):
            return True
        else:
            return False


    def __init__(self, dia, mes, ano):
        self.set_data(dia, mes, ano)
                

    def set_data(self, dia, mes, ano):
        """
        dia, mes e ano devem ser numeros inteiros
        """
        if type(dia)  == int and type(mes)  == int and type(ano)  == int:
            self.__dias = dia
            self.__meses = mes
            self.__anos = ano
        else:
            print("Dia, mês ou ano não é um inteiro")
        
        #Remove zero no primeiro digito
        if mes < 10:
            self.__meses = mes % 10
            

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.__dias,
                                               self.__meses,
                                               self.__anos)
    
    def avanca_dia(self):
        """
        Avança um dia no calendário.
        """
        #verifique qual o ultimo dia do mes
        #verifique se mes de fevereiro é bissexto
        #se o dia é o ultimo do mes atual, dia tem valor 1
        #se o dia é o ultimo do ano, mes tem valor 1 e ano += 1
        #para todos os outros casos apenas dia é incrementado
        
        #Checa se ano é bissexto e se é o último dia do mês
        if self.__meses == 2 and Calendario.ehBissexto(self.__anos):
            if self.__dias == 29:
                self.__dias = 1
                self.__meses += 1
            else:
                self.__dias += 1
        elif self.__dias == Calendario.ultimo_dia_mes[self.__meses-1]:
            self.__dias = 1
            
            if self.__meses == 12:
                self.__meses = 1
                self.__anos +=1
            else:
                self.__meses += 1
        else:
            self.__dias += 1
        

if __name__ == "__main__":
    c = Calendario(31,12,2012)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("----------")
    
    print("2012 é ano Bissexo:")
    c = Calendario(28,2,2012)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("----------")
    
    c = Calendario(28,2,2013)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("----------")
    
    print("1900 não é ano Bissexo. O número é divisivel por 100 mas não por 400: ")
    c = Calendario(28,2,1900)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)
    print("----------")
    
    print("2000 foi um é ano Bissexo. O número é divisivel por 400: ")
    c = Calendario(28,2,2000)
    print(c, end=" ")
    c.avanca_dia()
    print("- Ao avancar um dia vamos para a data: ", c)