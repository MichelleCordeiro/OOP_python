'''
POO 2021.2 - Prática 2.1 - Herança e métodos/atributos de classe
Considere um sistema de armazenamento em nuvem, tal como o Google Drive, Dropbox, Microsoft OneDrive, etc.

Neste sistema, existem classes que armazenam informações sobre arquivos, como por exemplo, qual o seu nome e tamanho.

Considerando este contexto, desenvolva as classes como solicitado a seguir.

Classe InfoArquivo
Contém informações sobre um arquivo qualquer.

Atributos:

nome: nome do arquivo
tamanho: tamanho em megabytes (MB) que o arquivo ocupa
_formatos_suportados: atributo de classe que contém em uma lista de strings os formatos de arquivo que o sistema da nuvem pode salvar (txt, pdf, mp4, etc.)
Métodos:

__init__: recebe como parâmetro o nome e tamanho do arquivo
__str__: retorna uma str que representa um arquivo no formato Arquivo: {nome} ({tamanho} MB)
excede_tamanho: retorna verdadeiro caso o tamanho do arquivo seja superior a 1000 MB ou falso caso contrário
imprime_arquivos_suportados: método de classe que imprime todos os formatos de arquivo suportados
Classe InfoImagem
Contém informações sobre arquivos de imagem. Deve herdar os atributos e métodos de InfoArquivo. Deve conter também os atributos e métodos a seguir.

Atributos:

resolucao: list com tamanho 2 contendo a largura e altura da imagem
Métodos:

__init__: recebe como parâmetro o nome, tamanho e resolução da imagem
__str__: retorna uma str que representa uma imagem no formato Imagem: {nome}, resolucao: {resolucao} ({tamanho} MB)
redimensiona: redimensiona a imagem dividindo a sua largura e altura por 2
Classe InfoVideo
Contém informações sobre arquivos de vídeo. Deve herdar os atributos e métodos de InfoImagem. Deve conter também os atributos e métodos a seguir.

Atributos:

duracao: duração do vídeo em segundos
Métodos:

__init__: recebe como parâmetro o nome, tamanho, resolução e duração do vídeo
__str__: retorna uma str que representa um vídeo no formato Video: {nome}, resolucao: {resolucao}, duracao: {duracao} ({tamanho} MB)
Nesta classe, o método excede_tamanho deve ser estendido: além de checar se o arquivo excede o tamanho em megabytes, deve checar também se a largura da imagem do vídeo é maior do que 3840 e retornar verdadeiro se for o caso (falso caso contrário).

Utilize o código a seguir para testar o seu programa.

Saída esperada:

---------------------
Formatos suportados:
txt
pdf
jpg
zip
mp4
---------------------

>>>>>>>>>>>>>>>>>>>>>
Antes do redimensionamento:
Arquivo: anotacoes.txt (0.01 MB)
False
Arquivo: nota_fiscal.pdf (2.0 MB)
False
Arquivo: arquivo.zip (1500 MB)
True
Imagem: foto1.jpg, resolucao: [3000, 2000] (3.0 MB)
False
Imagem: foto2.jpg, resolucao: [3000, 2000] (3.0 MB)
False
Video: video1.mp4, resolucao: [1920, 1080], duracao: 3602 (50.0 MB)
False
Video: video2.mp4, resolucao: [3840, 2060], duracao: 300 (20.0 MB)
False
Video: video3.mp4, resolucao: [7680, 4320], duracao: 20 (65.0 MB)
True

>>>>>>>>>>>>>>>>>>>>>
Depois do redimensionamento:
Arquivo: anotacoes.txt (0.01 MB)
False
Arquivo: nota_fiscal.pdf (2.0 MB)
False
Imagem: foto1.jpg, resolucao: [3000, 2000] (3.0 MB)
False
Imagem: foto2.jpg, resolucao: [1500.0, 1000.0] (3.0 MB)
False
Video: video1.mp4, resolucao: [1920, 1080], duracao: 3602 (50.0 MB)
False
Video: video2.mp4, resolucao: [3840, 2060], duracao: 300 (20.0 MB)
False
Video: video3.mp4, resolucao: [3840.0, 2160.0], duracao: 20 (65.0 MB)
False
'''

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