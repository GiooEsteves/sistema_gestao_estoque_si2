import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os produtos
produtos = {}

def cadastrar_produto():
    messagebox.showinfo('Cadastrar produto')
  

def localizar_produto():
    messagebox.showinfo('Localizar produto')

def listar_produto():
    messagebox.showinfo('Listar produto')


# Criação da janela principal
root = tk.Tk()
root.title("Cadastro e Localização de Produtos")

# Labels e entradas de dados
tk.Label(root, text="Nome do Produto:").pack(pady=5)
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

tk.Label(root, text="Preço:").pack(pady=5)
entry_preco = tk.Entry(root)
entry_preco.pack(pady=5)

tk.Label(root, text="Quantidade:").pack(pady=5)
entry_quantidade = tk.Entry(root)
entry_quantidade.pack(pady=5)

# Botões
btn_cadastrar = tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto)
btn_cadastrar.pack(pady=10)

btn_localizar = tk.Button(root, text="Localizar Produto", command=localizar_produto)
btn_localizar.pack(pady=10)

btn_listar = tk.Button(root, text="Listar Produto", command=listar_produto)
btn_listar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=root.quit)
btn_sair.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
