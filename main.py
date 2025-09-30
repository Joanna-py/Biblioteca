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


def atualizar_disponibilidade(id_livro):
            try:
                conexao = sqlite3.connect("biblioteca.db")
                cursor = conexao.cursor()

                cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
                resultado = cursor.fetchone()

                if not resultado:
                    print("Livro não encontrado!")
                    return
                
                status_atual = resultado[0]
                novo_status = "Não" if status_atual == "Sim" else "Sim"

                cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_status, id_livro))

                conexao.commit()
                print(f"Status do livro ID {id_livro} alterado: {status_atual} → {novo_status}")


            finally:
                conexao.close()

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

#Etapa 6

while True:
    print("Bem vindo a nossa biblioteca!✨")
    print("="*50)
    print("1. Cadastrar livro\n2. Listar livros\n3. Atualizar disponibilidade\n4. Remover livro\n5. Sair")
    print("="*50)

    menu = input("Escolha uma das opçoes acima: ")
    
    #Etapa 2

    if menu == 1:
        titulo = input("Digite o titulo: ")
        autor = input(f"Quem é o autor do livro? -| {titulo}: ")
        ano = int(input(f"De que ano é o livro? -| {titulo}: "))
        cadastrar_livro(titulo, autor, ano)


    #Etapa 3

    elif menu == 2:
        listar_livros()


    #Etapa 4

    elif menu == 3:
       
        atualizar_disponibilidade(1)

        
    #Etapa 5

    elif menu == 4:
    
        remover_livro(remover)
        

