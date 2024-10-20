arquivo = open("teste.txt")
conteudo = arquivo.read()

print("Tipo de conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo readline: ")
print(repr(conteudo))


proximo_conteudo = arquivo.readline()
print("Próximo conteúdo retornado:")
print(repr(proximo_conteudo))

arquivo.close()