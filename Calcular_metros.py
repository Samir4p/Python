area = int(input('Digite o tamanho: '))

litros = area // 3
if area % 3 > 0:
    litros = litros + 1

latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1

print('Vocé precisara de', latas, 'latas.')
print('Vai gastar R$', latas*80)


#print(litros)
#print(latas)
#print(latas * 18)



