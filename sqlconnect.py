import pyodbc

from datascraping import get_notebook_data

notebooks = get_notebook_data()

for notebook in notebooks:
    print(f"Name: {notebook['name']}")
    print(f"Specs: {notebook['specs']}")
    print(f"Price: {notebook['price']}")
    print('================================================')

dados_conexao = (
    'Driver={SQL Server};'
    'Server=localhost\SQLEXPRESS;'
    'Database=scrapping;'
    'Trusted_Connection=yes;'
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("SELECT MAX(id) FROM infonote")
result = cursor.fetchone()
current_max_id = result[0] if result[0] is not None else 0 


for i, notebook in enumerate(notebooks, start=current_max_id + 1):
    cursor.execute(
        """
        INSERT INTO infonote (id, name, specs, price, store)
        VALUES (?, ?, ?, ?, ?)
        """,
        i, notebook['name'], notebook['specs'], notebook['price'], notebook['store']
    )

conexao.commit()


cursor.close()
conexao.close()
