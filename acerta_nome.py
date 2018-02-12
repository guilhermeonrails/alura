import time

def verifica_resposta(resposta, nome):
    if '.' in resposta:
        return nome
    else:
        nome = nome + resposta[0]
        return nome

def boas_vindas():
    print('######################################')
    print('Seja bem vindo ao jogo da adivinhação')
    print('######################################\n')

nome = ''
boas_vindas()

resposta = input('Qual seu filme favorito?\n')
nome = verifica_resposta(resposta, nome)

resposta = input('Qual seu livro favorito?\n')
nome = verifica_resposta(resposta, nome)

resposta = input('Qual sua fruta favorita?\n')
nome = verifica_resposta(resposta, nome)

resposta = input('Qual sua cor favorita?\n')
nome = verifica_resposta(resposta, nome)

print('Seu nome é ...')
time.sleep(2)
print('Acredito que seu nome seja', nome)