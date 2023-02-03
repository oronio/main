# Francisco Ronny e Francisco Edson
from sys import stdin
# leitura do arquivo
ent = input('Nome do arquivo das Entradas: ')
with open(ent, "r", encoding='utf-8') as a:
    entrada = a.readlines()
entrada = ' '.join(entrada).replace('\n', '').split()
listPar = list()
t = 0
x = 1
while x == 1:
    if t == len(entrada):
        break
    while entrada[t] != '%':
        if int(entrada[t]) % 2 == 0:
            par = 0
        else:
            par = 1
        listPar.append(par)
        t += 1

    del listPar[0]

    lp = list()
    tt = 1
    y = 1
    Pt = 1
    listPar.append('.')
    while tt <= len(listPar):
        if tt == len(listPar):
            break

        if listPar[tt] == listPar[tt-1]:
            Pt += 1

        if listPar[tt] != listPar[tt-1]:
            lp.append(Pt)
            Pt = 1
        tt += 1
    ttt = 0
    for i in lp:

        if i == len(lp):
            if i == lp[i-1]+1:
                break
            print(lp[-1])
            break
        if i+1 != lp[i]:
            print('NAO')
            break

    print('%')

    listPar = []

    t += 1
