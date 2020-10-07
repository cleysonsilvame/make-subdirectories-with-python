import os


pastaAtual = os.path.dirname(os.path.realpath(__file__))

todosArquivos = os.listdir(pastaAtual)

for arquivo in todosArquivos:    
    pathArquivo = pastaAtual + '\\' + arquivo

    if(os.path.isdir(pathArquivo)):
        i = 1
        while i <= 13:            
            pastaAdiantamento = pathArquivo + '\\ADIANTAMENTO\\2021\\' + '%02d' % i
            pastaFolha = pathArquivo + '\\FOLHA DE PAGAMENTO\\2021\\' + '%02d' % i

            os.makedirs(pastaAdiantamento)
            os.makedirs(pastaFolha)
            i += 1