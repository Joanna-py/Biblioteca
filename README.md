# 📚 Sistema de Gerenciamento de Biblioteca

Este é um projeto simples de gerenciamento de livros utilizando **Python** e **SQLite**. O sistema permite cadastrar, listar, atualizar e remover livros de uma base de dados local (`biblioteca.db`).

---

## ⚙️ Funcionalidades

- 📘 Cadastrar novos livros
- 📄 Listar todos os livros cadastrados
- 🔁 Atualizar status de disponibilidade (Sim/Não)
- 🗑️ Remover livros por ID
- 🧱 Criação automática da tabela `livros` no banco de dados

---

## 🧰 Tecnologias Utilizadas

- Python 3.x
- SQLite3 (embutido no Python)

---

## 📦 Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

   python biblioteca.py

   🗃️ Estrutura da Tabela livros
Campo	Tipo	Descrição
id	INTEGER	Identificador único (PRIMARY KEY)
titulo	TEXT	Título do livro
autor	TEXT	Nome do autor
ano	INTEGER	Ano de publicação
disponivel	TEXT	Disponibilidade: "Sim" ou "Não"
