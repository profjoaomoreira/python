arq = open('lista.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva1\n')
texto.append('José Lima1\n')
texto.append('Maria das Dores1')
arq.writelines(texto)
arq.close()
