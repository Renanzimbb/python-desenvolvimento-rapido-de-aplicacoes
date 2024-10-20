import sqlite3

class Veiculo:
    def __init__(self,id,nome,marca,ano):
        self.id = id
        self.nome = nome
        self.marca = marca
        self.ano = ano

hb20 = Veiculo('1','Hb20','Hyundai','2002')
xfactor = Veiculo('2','X Factor','Tesla','2003')
gol = Veiculo('3','Gol','Volksvagen','1999')

try:
    conexao = sqlite3.connect("teste.db")
    cursor = conexao.cursor()

    sql0 = """DROP TABLE veiculo"""
    sql = """CREATE TABLE veiculo(
                id INTEGER,
                nome STRING,
                marca STRING,
                ano FLOAT,
                PRIMARY KEY(id))"""
    sql2 = """INSERT INTO veiculo (id, nome, marca, ano) Values (:id,:nome,:marca,:ano)"""
    sql3 = """SELECT * from veiculo"""

    cursor.execute(sql3)
    conexao.commit()
    registros =  cursor.fetchall()

    for registro in registros:
        veiculo = Veiculo(*registro)
        print("Nome: ", veiculo.nome)

except sqlite3.DatabaseError as error:
    print(f"Falha ao conectar ao banco de dados: ", error)

finally:
    if conexao:
        cursor.close()
        conexao.close()