'''
Função percorre uma lista indica o maior e menor item
'''

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([1,2,3,4,55,6666,9999,123456, -1, -7, 0]))