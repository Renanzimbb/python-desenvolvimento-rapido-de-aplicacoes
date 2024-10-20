import mysql.connector as conector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'rlsites',
    'auth_plugin': 'mysql_native_password'  # dependendo da versão do MySQL, pode ser necessário
                                            # especificar o plugin de autenticação
}

# Abertura de conexão
conexao = conector.connect(**db_config)

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
comando = '''SELECT post_title FROM wp_posts'''
cursor.execute(comando)
registros = cursor.fetchone()

print(registros[0])


# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
