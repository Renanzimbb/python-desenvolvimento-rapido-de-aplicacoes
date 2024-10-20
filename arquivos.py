import os.path

arquivo = open("teste.txt", "a")


print(os.path.realpath(arquivo.name))  # Caminho Relativo
print(os.path.abspath(arquivo.name))    # Caminho Absoluto
print(arquivo)

print("Nome do Arquivo: ", arquivo.name)
print("Modo do Arquivo: ", arquivo.mode)
print("Arquivo fechado: ", arquivo.closed)

#arquivo.close()
print("Arquivo fechado: ", arquivo.closed)

#Retorna todo o conteúdo de um arquivo como uma única string.
#conteudo = arquivo.read()
#print(conteudo)

#Retorna uma linha de arquivo, incluindo caracteres de final (\n ou \r\n), e avança o cursor para a próxima.
#conteudo = arquivo.readline()
#print(conteudo)

#Retorna uma lista em que cada item da lista é uma linha do arquivo.
#conteudo = arquivo.readlines()
#print(conteudo)

arquivo.write("Conteudo da terceira linha")
arquivo.write("\n Conteudo da quarta linha")