# Francisco Ronny e Francisco Edson
from sys import stdin
# leitura do arquivo
ent = input('Nome do arquivo das Entradas: ')
with open(ent, "r", encoding='utf-8') as a:
    entrada = a.readlines()
entrada = ' '.join(entrada).replace('\n', '').split()

pres = ['o', 'os', 'a', 'om', 'ons', 'am']
pret = ['ei', 'es', 'e', 'em', 'est', 'im']
fut = ['ai', 'ais', 'i', 'aem', 'aist', 'aim']
_4 = ['aist']
_3 = ['ons', 'est', 'ais', 'aem', 'aim']
_2 = ['os', 'om', 'am', 'ei', 'es', 'em', 'im', 'ai']
_1 = ['o', 'a', 'e', 'i',]
a1 = ['o', 'ei', 'ai']
a2 = ['os', 'es', 'ais']
a3 = ['a', 'e', 'i']
a4 = ['om', 'em', 'aem']
a5 = ['ons', 'est', 'aist']
a6 = ['am', 'im', 'aim']
Ns = [4, 3, 2, 1]
_tp = [pres, pret, fut]
_ps = [a1, a2, a3, a4, a5, a6]


for pal in entrada:
    for num in Ns:
        t = False
        suff = None
        ent = pal[-num:]
        if len(ent) == 4:
            for i in _4:
                if ent == i:
                    suff = i
                    t = True
        if t:
            break
        if len(ent) == 3:
            for i in _3:
                if ent == i:
                    suff = i
                    t = True
        if t:
            break
        if len(ent) == 2:
            for i in _2:
                if ent == i:
                    suff = i
                    t = True
        if t:
            break
        if len(ent) == 1:
            for i in _1:
                if ent == i:
                    suff = i
                    t = True
    time = None
    # tempo
    t = False
    for tp in _tp:  # pres,pret,fut
        for i in tp:  # itens de cada lista
            if suff == i:
                t = True
                if tp == pres:
                    time = 'presente'
                elif tp == pret:
                    time = 'pretérito'
                else:
                    time = 'futuro'
        if t:
            break

    # pessoa
    person = None
    t = False
    for ps in _ps:  # a1,a2,a3...
        for i in ps:  # itens de cada lista
            if suff == i:
                t = True
                if ps == a1:
                    person = '1a pessoa'
                elif ps == a2:
                    person = '2a pessoa'
                elif ps == a3:
                    person = '3a pessoa'
                elif ps == a4:
                    person = '4a pessoa'
                elif ps == a5:
                    person = '5a pessoa'
                else:
                    person = '6a pessoa'
        if t:
            break

    if suff == None:
        print(pal, ' - não é um tempo verbal')
    else:
        print('{} - verbo {} - {} - {}'.format(pal,
              pal.replace(ent, 'en'), time, person))
