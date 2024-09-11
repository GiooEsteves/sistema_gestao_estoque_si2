import tkinter as tk
from tkinter import messagebox
<<<<<<< HEAD
from backend.core import adicionar_produto, listar_produtos, atualizar_estoque, remover_produto, estoque

def cadastrar_produto():
    nome = entry_nome.get()
    preco = entry_preco.get()
    quantidade = entry_quantidade.get()
    
    if nome and preco and quantidade:
        categoria = "Geral"
        resultado = adicionar_produto(nome, categoria, quantidade, preco)
        messagebox.showinfo("Resultado", resultado)
        limpar_campos()
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

def localizar_produto():
    nome = entry_nome.get()
    if nome:
        for produto in estoque:
            if produto['nome'] == nome:
                resultado = f"Nome: {produto['nome']}\nCategoria: {produto['categoria']}\nQuantidade: {produto['quantidade']}\nPreço: {produto['preco']}"
                messagebox.showinfo("Produto Encontrado", resultado)
                return
        messagebox.showwarning("Aviso", "Produto não encontrado.")
    else:
        messagebox.showwarning("Aviso", "Digite o nome do produto.")

def listar_produto():
    produtos = listar_produtos()
    messagebox.showinfo("Estoque", produtos)

def atualizar_produto():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    
    if nome and quantidade:
        resultado = atualizar_estoque(nome, quantidade)
        messagebox.showinfo("Resultado", resultado)
        limpar_campos()
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

def remover_produto():
    nome = entry_nome.get()
    
    if nome:
        resultado = remover_produto(nome)
        messagebox.showinfo("Resultado", resultado)
        limpar_campos()
    else:
        messagebox.showwarning("Aviso", "Digite o nome do produto.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

def criar_interface():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Cadastro e Localização de Produtos")

    # Labels e entradas de dados
    tk.Label(root, text="Nome do Produto:").pack(pady=5)
    global entry_nome
    entry_nome = tk.Entry(root)
    entry_nome.pack(pady=5)

    tk.Label(root, text="Preço:").pack(pady=5)
    global entry_preco
    entry_preco = tk.Entry(root)
    entry_preco.pack(pady=5)

    tk.Label(root, text="Quantidade:").pack(pady=5)
    global entry_quantidade
    entry_quantidade = tk.Entry(root)
    entry_quantidade.pack(pady=5)

    # Botões
    btn_cadastrar = tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto)
    btn_cadastrar.pack(pady=10)

    btn_localizar = tk.Button(root, text="Localizar Produto", command=localizar_produto)
    btn_localizar.pack(pady=10)

    btn_listar = tk.Button(root, text="Listar Produtos", command=listar_produto)
    btn_listar.pack(pady=10)

    btn_atualizar = tk.Button(root, text="Atualizar Estoque", command=atualizar_produto)
    btn_atualizar.pack(pady=10)

    btn_remover = tk.Button(root, text="Remover Produto", command=remover_produto)
    btn_remover.pack(pady=10)

    btn_sair = tk.Button(root, text="Sair", command=root.quit)
    btn_sair.pack(pady=10)

    # Inicia o loop principal da interface gráfica
    root.mainloop()
=======

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
>>>>>>> 3207bc9377864f8daa63b28bb977930aa4d354e5
