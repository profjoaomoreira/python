arq = open('lista.txt', 'r')
texto = arq.readlines()
for linha in texto:
    print(linha)
arq.close()
