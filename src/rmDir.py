import os
import shutil

pastaAtual = os.path.dirname(os.path.realpath(__file__))
 
todosArquivos = os.listdir(pastaAtual)

for arquivo in todosArquivos:    
    pathArquivo = pastaAtual + '\\' + arquivo

    if(os.path.isdir(pathArquivo)):
        pastaAdiantamento = pathArquivo + '\\ADIANTAMENTO\\2021'
        pastaFolha = pathArquivo + '\\FOLHA DE PAGAMENTO\\2021'

        shutil.rmtree(pastaAdiantamento)
        shutil.rmtree(pastaFolha)