import faker as Faker
import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(database="postgres", user="postgres",
                        password="con89ga6", host="127.0.0.1", port="5432")
print("Conexão aberta com sucesso!")

# Create a cursor to interact with the database
cursor = conn.cursor()

# Initialize the Faker instance for generating fake data
fake = Faker.Faker('pt_BR')  # Use Faker.Faker instead of just Faker

n = 10
for i in range(n):
    codigo = i + 10
    nome = 'produto_' + str(i + 1)
    preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True,
                         min_value=5, max_value=1000)  # Corrected the parameter name
    print(preco)
    print(nome)

    # Use triple quotes for multi-line strings
    comandoSQL = """INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)"""
    registro = (codigo, nome, preco)
    cursor.execute(comandoSQL, registro)

# Commit the changes to the database
conn.commit()
print("Inserção realizada com sucesso!")

# Close the database connection
conn.close()