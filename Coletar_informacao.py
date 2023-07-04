import whois
dominio = input('ALVO: ')
consulta_whois = whois.whois(dominio)


print(consulta_whois.text)

