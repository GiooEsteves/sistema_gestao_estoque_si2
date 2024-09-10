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