
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
''')
conn.commit()

# Função para salvar cliente
def salvar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        cursor.execute(
            'INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)',
            (nome, email, telefone)
        )
        conn.commit()
        messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        limpar_formulario()
    else:
        messagebox.showwarning(
            "Atenção",
            "Todos os campos devem ser preenchidos!"
        )

# Função para limpar formulário
def limpar_formulario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# Criar janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x300")

# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=15)

# Campo Nome
tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

# Campo Email
tk.Label(janela, text="Email:").pack()
entry_email = tk.Entry(janela, width=40)
entry_email.pack(pady=5)

# Campo Telefone
tk.Label(janela, text="Telefone:").pack()
entry_telefone = tk.Entry(janela, width=40)
entry_telefone.pack(pady=5)

# Botões
tk.Button(
    janela,
    text="Salvar",
    command=salvar_cliente,
    width=20
).pack(pady=10)

tk.Button(
    janela,
    text="Limpar",
    command=limpar_formulario,
    width=20
).pack()

# Iniciar programa
janela.mainloop()

# Fechar conexão
conn.close()
