import psycopg2

# Abertura de conexão
conexao = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
