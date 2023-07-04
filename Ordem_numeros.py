a = int(input('Digie um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

if a >= b >= c:
    print('Maior: ', a,'Menor: ', c)
elif a >= c >= b:
    print('Maior: ',a, 'Menor: ',b)
elif b >= a >= c:
    print('Maior: ', b, 'Menor: ',c)
elif b >= c >= a:
    print('Maior: ',b, 'Menor: ', a)
elif c >= a >= b:
    print('Maior: ',c, 'Menor: ', b)
else:
    print('Maior: ', c, 'Menor: ', a)




