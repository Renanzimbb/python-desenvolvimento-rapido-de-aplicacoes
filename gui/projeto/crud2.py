import psycopg2

#-----------------------------------------------------------------------------
#Essa classe possui métodos CRUD
#-----------------------------------------------------------------------------

class AppBD:
    def __init__(self):
        print('Método Construtor')

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="con89ga6",
                                               port="5432",
                                               database="postgres")
        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Faha ao se conectar ao Banco de Dados", error)


    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            print("Selecionando todos os produtos")
            sql_select_query = """SELECT * from public."PRODUTO" """
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except(Exception,psycopg2.Error) as error:
            print("Error in select operation", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com  o Postgres SQL foi fechada")

        return registros

    def atualizarDados(self,codigo,nome,preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização")
            sql_select_query="""select * from public."PRODUTO" 
            where "CODIGO" = %s """
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
            # Atualizar registro
            sql_update_query = """UPDATE public."PRODUTO" set "NOME" = %s, 
            "PRECO" = %s where "CODIGO" = %s"""
            cursor.execute(sql_update_query, (nome,preco,codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro Depois da Atualização")
            sql_select_query = """select * from public."PRODUTO" 
            where "CODIGO" = %s """
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception,psycopg2.Error) as error:
            print("Erro na atualização", error)
        finally:

            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL fi fechada.")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Atualizar registro
            sql_delete_query = """Delete from public."PRODUTO" 
             where "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")