import string as s
import time as t
from random import *

#inputs do usuario
#conter simbolos
#conter numeros
#conter letras maiusculas
#conter letras minusculas

def gerarSemente():
    print('  **Responda com s ou n\n  **Para especificar sua lista de senhas**\n')
    
    sb = input('  1) Deve conter simbolos?\n  >> ')
    nr = input('  2) Deve conter numeros?\n  >> ')
    L =  input('  3) Deve conter letras maiusculas?\n  >> ')
    l = input('  4) Deve conter letras minusculas?\n  >> ')
    
    semente = ' '
    if sb == 's':
        semente += s.punctuation
    if nr == 's':
        semente += s.digits
    if L == 's':
        semente += s.ascii_uppercase
    if l == 's':
        semente += s.ascii_lowercase
    if semente == ' ':
        print('  Opção invalida!\nErro detectado')
        exit()
        
    print('  \tEtapa concluida!!\n')
    
    semente = [x for x in semente]
    return semente
    
#tamanho da senha
#quantas senhas devem ser impressas.
#gerar senhas com base nos parametros
    
def gerarSenha():
    semente = gerarSemente()
    print('  **Responda com numeros\n  **Para gerar sua lista de senhas**\n')
        
    tm = int(input('  1) Quantidade de caracteres?\n  >> '))
    qs = int(input('  2) Quantidade de senhas para gerar?\n  >> '))
    nome = input('  3) Nome do arquivo de saida com as senhas?\n  >> ')
    nome += '.txt'
    
    for i in range(qs):
        senha = ''
        for j in range(tm):
            previa = semente[randint(0,len(semente)-1)]
            senha = str(previa) + str(senha)
            
#salvar em um arquivo .txt
        senha += '\n'
        with open(nome, 'a') as arquivo:
                arquivo.write(senha)

#Run
gerarSenha()
print('\n\tArquivo criado, acesse sua pasta!!\n\n')