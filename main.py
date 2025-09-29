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


#Etapa 3

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        print("\n=== LISTA DE LIVROS ===")
        for linha in cursor.fetchall():
            print(f"ID {linha[0]} | TÍTULO {linha[1]} | AUTOR {linha[2]} | ANO {linha[3]} | DISPONÍVEL {linha[4]}")

    except sqlite3.Error as erro:
        print(f"Erro ao listar livros: {erro}")
    finally:
        conexao.close()

listar_livros()


#Etapa 5


def remover_livro(id_livro):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("livro removido com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido!")

    except Exception as erro:
         print(f"Erro ao tentar excluir livro: {erro}")

    finally:
        if conexao:
            conexao.close()

remover = input("Digite o id do livro que deseja deletar: ")
remover_livro(remover)
