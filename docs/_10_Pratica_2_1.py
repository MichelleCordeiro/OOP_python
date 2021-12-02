class InfoArquivo():
    
    _formatos_suportados = []
    
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        InfoArquivo._formatos_suportados = ['txt', 'pdf', 'jpg', 'zip', 'mp4']
        
    def __str__(self):
        return f'Arquivo: {self.nome} ({self.tamanho} MB)'
    
    def excede_tamanho(self):
        if self.tamanho > 1000:
            return True
        else:
            return False
        
    @staticmethod
    def imprime_arquivos_suportados():
        print('---------------------\nFormatos suportados:')
        for i in InfoArquivo._formatos_suportados:
            print(i)
        print('--------------------')
        

class InfoImagem(InfoArquivo):
    def __init__(self, nome, tamanho, resolucao):
        InfoArquivo.__init__(self, nome, tamanho)
        self.resolucao = resolucao
        
    def __str__(self):
        return f'Imagem: {self.nome}, resolucao: {self.resolucao} ({self.tamanho} MB)'
    
    def redimensiona(self):
        self.resolucao = [self.resolucao[0]/2, self.resolucao[1]/2]
    

class InfoVideo(InfoImagem):
    def __init__(self, nome, tamanho, resolucao, duracao):
        InfoImagem.__init__(self, nome, tamanho, resolucao)
        self.duracao = duracao
            
    def __str__(self):
        return f'Video: {self.nome}, resolucao: {self.resolucao}, duracao: {self.duracao} ({self.tamanho} MB)'
    
    def excede_tamanho(self):
        #for i in range(2):
        if InfoArquivo.excede_tamanho(self) or self.resolucao[0] > 3840:
            return True
        else:
            return False