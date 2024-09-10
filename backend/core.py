estoque = []

def adicionar_produto(nome, categoria, quantidade, preco): # CREATE
    for produto in estoque:
        if produto['nome'] == nome:
            return "Produto já existe no estoque."
    
    novo_produto = {
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco
    }
    estoque.append(novo_produto)

# READ

def atualizar_estoque(nome, quantidade): # UPDATE
    for produto in estoque:
        if produto['nome'] == nome:
            produto['quantidade'] += quantidade # adicionar mais produtos
            return
    return "Produto não encontrado."

# DELETE

# teste unitário
# adicionar_produto("laranja", "fruta", 30, 15.66)
# print(estoque)
# atualizar_estoque("laranja", 2)
# print(estoque)

def listar_produtos():
    """Lista todos os produtos no estoque."""
    estoque = carregar_estoque()
    if not estoque:
        print("Nenhum produto encontrado.")
    else:
        for produto in estoque:
            print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")

# DELETE
def remover_produto(nome):
    """Remove um produto pelo nome do estoque."""
    estoque = carregar_estoque()
    estoque_atualizado = [produto for produto in estoque if produto['nome'] != nome]
    if len(estoque) == len(estoque_atualizado):
        print(f"Produto '{nome}' não encontrado.")
    else:
        salvar_estoque(estoque_atualizado)
        print(f"Produto '{nome}' removido com sucesso.")
        
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Listar produtos")
        print("2. Remover produto")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            listar_produtos()
        elif escolha == '2':
            nome = input("Nome do produto a remover: ")
            remover_produto(nome)
        elif escolha == '3':
            break
        else:
            print("Opção inválida, tente novamente.")
