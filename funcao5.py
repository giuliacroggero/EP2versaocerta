def afundados (frota,tabuleiro):
    j=0
    for nome,lista in frota.items():
        for navio in lista:
            z=0
            for i in range(len(navio)):
                linha=navio[i][0]
                coluna=navio[i][1]
                if tabuleiro[linha][coluna]=="X":
                    z+=1
            if z == len(navio):
                j+=1
            z=0    
    return j