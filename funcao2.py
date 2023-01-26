def define_posicoes(linha,coluna,orientacao,tamanho):
    lista = []
    i = 0
    if orientacao == 'vertical':
        while len(lista)<tamanho:
            lista.append([linha+i,coluna])
            i+=1
        
    elif orientacao == 'horizontal':
        while len(lista)<tamanho:
            lista.append([linha,coluna+i])
            i+=1
    return lista

def preenche_frota(frota,nomenavio,linha,coluna,orientacao,tamanho):
    posicoes =define_posicoes(linha,coluna,orientacao,tamanho)
    if nomenavio not in frota:
        frota[nomenavio] = [posicoes]
    else:
        for nome in frota:
            if nome == nomenavio:
               frota[nome].append(posicoes)
    return frota