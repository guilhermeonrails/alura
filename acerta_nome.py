import time

print('\n######################################')
print('Seja bem vindo ao jogo da adivinhação')
print('######################################\n')

def verifica_resposta(resposta, nome):
    if '.' in resposta:
        return nome
    else:
        nome = nome + resposta[0]
        return nome

nome = ''

resposta = input('Qual seu filme favorito?\n')
nome = verifica_resposta(resposta, nome)

resposta = input('Qual seu livro favorito?\n')
nome = verifica_resposta(resposta, nome)

resposta = input('Qual sua fruta favorita?\n')
nome = verifica_resposta(resposta, nome)

resposta = input('Qual sua cor favorita?\n')
nome = verifica_resposta(resposta, nome)

print('Seu nome é ...\n')
time.sleep(2)
print('Acredito que seu nome seja', nome)