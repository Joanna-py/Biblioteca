import sqlite3

#Etapa 1

conexao= sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
    )              
""")
print("Tabela criada com sucesso!")

#Etapa 2

def cadastrar_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        
        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)                              
        """, 
        (titulo, autor, ano, "Sim")
        )
        
        conexao.commit()
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar livro: {erro}")
    finally:   
        conexao.close()


titulo = input("Digite o titulo: ")
autor = input(f"Quem é o autor do livro? -| {titulo}: ")
ano = int(input(f"De que ano é o livro? -| {titulo}: "))

cadastrar_livro(titulo, autor, ano)