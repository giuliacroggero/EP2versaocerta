def posiciona_frota(frota):
    linhatab = [0]*10
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)
    print(tabuleiro)
    for navio,lista in frota.items():
        for l in lista:
            for posicao in l:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro