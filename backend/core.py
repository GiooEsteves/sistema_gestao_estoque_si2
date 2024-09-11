estoque = []

def adicionar_produto(nome, categoria, quantidade, preco): # CREATE
    for produto in estoque:
        if produto['nome'] == nome:
            return "Produto já existe no estoque."
    
    novo_produto = {
        'nome': nome,
        'categoria': categoria,
        'quantidade': int(quantidade),
        'preco': float(preco)
    }
    estoque.append(novo_produto)
    return f"Produto '{nome}' adicionado com sucesso!"

def listar_produtos(): # READ
    if not estoque:
        return "Estoque vazio."
    
    lista = "\n".join([f"Nome: {p['nome']}, Categoria: {p['categoria']}, Quantidade: {p['quantidade']}, Preço: {p['preco']}" for p in estoque])
    return lista

def atualizar_estoque(nome, quantidade): # UPDATE
    for produto in estoque:
        if produto['nome'] == nome:
            produto['quantidade'] += int(quantidade)
            return f"Quantidade do produto '{nome}' atualizada!"
    return "Produto não encontrado."

<<<<<<< HEAD
=======
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

>>>>>>> 3207bc9377864f8daa63b28bb977930aa4d354e5
def remover_produto(nome): # DELETE
    for produto in estoque:
        if produto['nome'] == nome:
            estoque.remove(produto)
            return f"Produto '{nome}' removido com sucesso."
    
<<<<<<< HEAD
    return "Produto não encontrado."
=======
    return "Produto não encontrado."
>>>>>>> 3207bc9377864f8daa63b28bb977930aa4d354e5
