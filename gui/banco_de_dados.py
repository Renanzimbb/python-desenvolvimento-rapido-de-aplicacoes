import psycopg2
conn = psycopg2.connect(database = "postgres", user="postgres" , password="con89ga6" , host="127.0.0.1" , port="5432" )
print ("Conexão com o Banco de Dados aberta com sucesso!")
cur=conn.cursor()
cur.execute("""Delete from public."agenda" where "id"=1""")
conn.commit()
cont=cur.rowcount
print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!");
conn.close()




# cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
# cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""")
# cur.execute("""select * from public."AGENDA" where "id"=1""")
# cur.execute("""Update public."agenda" set "telefone"='02188888888' where "id"=1""")

#  A propriedade “rowcount” do “cursor” retorna a quantidade de registros que foram excluídos da tabela “Agenda”.