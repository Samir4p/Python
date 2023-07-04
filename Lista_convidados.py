print('Lista de convidados')
numero_convidados = input('Digite o numero de convidados: ')
lista_de_convidados = []

i = 1
while i <= int(numero_convidados):
    nome_do_convidado = input('Coloque o nome do convidado #' + str(i) + ': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1
print('Serão: ', numero_convidados, 'convidados')

for convidados in lista_de_convidados:
    print(convidados)
    
