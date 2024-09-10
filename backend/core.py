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

def listar_produtos(): # READ
    if not estoque:
        return "Estoque vazio."
    
    for produto in estoque:
        print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")

def remover_produto(nome): # DELETE
    for produto in estoque:
        if produto['nome'] == nome:
            estoque.remove(produto)
            return f"Produto '{nome}' removido com sucesso."
    
    return "Produto não encontrado."
