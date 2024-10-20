#Ao lidar com arquivos, devemos utilizar a palavra reservada with,
# disponibilizada pelo Python. Ela garante que o arquivo será fechado adequadamente após utilizarmos o arquivo,
# não sendo necessário chamar o método close explicitamente. A sintaxe de utilização do with é:

print("Iterando sobre o arquivo")

with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        texto = arquivo.read()
        contador = texto.count(("Ola"))
        print(linha_limpa)
        print(contador)
    print("Fim do arquivo", arquivo.name)



