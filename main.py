import sqlite3

#Etapa 1

conexao= sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER
    )              
""")
print("Tabela criada com sucesso!")

#Etapa 2

def inserir_dados(titulo, autor, ano):
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute(""""
    INSERT INTO livros (titulo, autor, ano)
    VALUES (?, ?, ?)
    """, (titulo, autor, ano))

    conexao.commit()
    conexao.close()

    print(f"Dados inseridos na tabela com sucesso!\nTITULO: {titulo}\nAUTOR: {autor}\nANO: {ano}")
