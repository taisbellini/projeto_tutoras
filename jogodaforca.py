import random

def getPalavra(listaDePalavras):
    # Retorna uma palavra aleatoria da lista
    index = random.randint(0, len(listaDePalavras) - 1)
    return listaDePalavras[index]

def mostra(erradas, certas, palavra):
    print 'Letras erradas:',
    for letra in erradas:
        print letra,
    print " " 

    espacos = '_' * len(palavra)

    for i in range(len(palavra)): # substitui espacos com as letras corretas
        if palavra[i] in certas:
            espacos = espacos[:i] + palavra[i] + espacos[i+1:]

    for letra in espacos: # mostra os espacos com as letras corretas
        print  letra,
    print " "

def getChute(usadas):
    # Retorna a letra digitada e faz a validacao se eh uma letra valida
    while True:
        print('Chute uma letra.')
        chute = input()
        chute = chute.lower()
        if len(chute) != 1:
            print('Por favor informe uma unica palavra')
        elif chute in usadas:
            print('Voce ja usou essa letra. Tente novamente')
        elif chute not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor use apenas LETRAS.')
        else:
            return chute


print " F O R C A "

erradas = []
certas = []
fim = False
chances = 7

palavras = 'batata barriga bocejo camelo cachorro candelabro cobra cadeira sapato paralelepipedo macaco'.split()
palavra = getPalavra(palavras)  

while fim == False:
    mostra(erradas, certas, palavra)

    # Pega a letra escolhida pelo jogador
    chute = getChute(erradas + certas)

    if chute in palavra:	
        certas += chute

        # Verifica se o jogador ganhou
        achouTodas = True
        for i in range(len(palavra)):
            if palavra[i] not in certas:
                achouTodas = False
                break
        if achouTodas:
            print('Sim! A palavra era "' + palavra + '"! Voce ganhou!')
            fim = True
    else:
        erradas += chute

        # Verifica se o jogador ainda tem chances
        if len(erradas) == chances:
            mostra(erradas, certas, palavra)
            print "Voce nao tem mais chances. A palavra correta era: ", palavra
            fim = True