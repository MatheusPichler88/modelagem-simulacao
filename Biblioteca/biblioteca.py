#Lista de usuários, onde cada usúario é um dicionário
usuarios = [
    {"tipo": "aluno", "matricula": "A001", "historico_emprestimo": []},
    {"tipo": "professor", "matricula": "P001", "historico_emprestimo": []},
    {"tipo": "funcionario", "matricula": "F001", "historico_emprestimo": []},
]

print("Lista inicial de usuários:")
for u in usuarios:
        print(u)
print()


#Lista de livros, onde cada livro é um dicionário
livros = [
    {"isbn": "12345", "titulo": "Python para iniciantes", "disponivel": True, "localizacao": "Estante A", "prazo_devolucao": None},
    {"isbn": "67890", "titulo": "Modelagem e simulação", "disponivel": True, "localizacao": "Estante B", "prazo_devolucao": None},
]
print("Lista inicial de livros:")
for l in livros:
    print(l)
print()

#Lista de bibliotecario

bibliotecarios = [
    {"nome": "Ana", "turno": "manhã", "especialidade":None},
    {"nome": "Carlos", "turno": "tarde", "especialidade": None},
]
print("Lista de bibliotecários:")
for b in bibliotecarios:
    print(b)
print()

# Dicionário vázio que guarda quem pegou o livro emprestado.
emprestimos_ativos = {}

#Funções de busca:

# Função para encontrar usuário por matrícula
def encontrar_usuario(matricula):
    for usuario in usuarios:
        if usuario["matricula"] == matricula:
            return usuario
    return None

# Função para encontrar livro por ISBN
def encontrar_livro(isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
    return None

# Função para emprestar livro
def emprestar_livro(matricula_usuario, isbn_livro):
    usuario = encontrar_usuario(matricula_usuario)
    livro = encontrar_livro(isbn_livro)
# Validações    
    if usuario is None:
        print(f"Usuário com matrícula {matricula_usuario} não encontrado.")
        return False
    
    if livro is None:
        print(f"Livro com ISBN {isbn_livro} não encontrado.")
        return False
    
    if not livro["disponivel"]:
        print(f"Livro '{livro['titulo']}' não está disponível no momento.")
        return False
    
    # Realizar o empréstimo
    livro["disponivel"] = False
    usuario["historico_emprestimo"].append(isbn_livro)
    emprestimos_ativos[isbn_livro] = matricula_usuario
    
    print(f"Livro '{livro['titulo']}' emprestado para {usuario['tipo']} {matricula_usuario}")
    return True

# Função para devolver livro
def devolver_livro(matricula_usuario, isbn_livro):
    usuario = encontrar_usuario(matricula_usuario)
    livro = encontrar_livro(isbn_livro)
# Validações
    if usuario is None:
        print(f"Usuário com matrícula {matricula_usuario} não encontrado.")
        return False
    
    if livro is None:
        print(f"Livro com ISBN {isbn_livro} não encontrado.")
        return False
    
    if livro["disponivel"]:
        print(f"Livro '{livro['titulo']}' já está disponível, não pode ser devolvido.")
        return False
    
    # Realizar a devolução
    livro["disponivel"] = True
    del emprestimos_ativos[isbn_livro]
    
    print(f"Livro '{livro['titulo']}' devolvido por {usuario['tipo']} {matricula_usuario}")
    return True

# Simulação
print("Simulação:")
emprestar_livro("A001", "12345")
emprestar_livro("P001", "67890")
emprestar_livro("A001", "67890")
devolver_livro("A001", "12345")
emprestar_livro("F001", "12345")

# Status dos livros:
print("\nLista dos livros com seus status:")
for livro in livros:
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(f"{livro['titulo']} (ISBN: {livro['isbn']}): {status}")

# Histórico de empréstimos dos usuários
print("\nLista dos históricos de empréstimos:")
for usuario in usuarios:
    print(f"{usuario['tipo']} {usuario['matricula']}: Empréstimos: {usuario['historico_emprestimo']}")

# Empréstimos ativos
print("\nLista dos empréstimos ativos")
for isbn, matricula in emprestimos_ativos.items():
    livro = encontrar_livro(isbn)
    usuario = encontrar_usuario(matricula)
    print(f"Livro: '{livro['titulo']}' (ISBN: {isbn}) emprestado para {usuario['tipo']} (Matrícula: {matricula})")

print("\nFim da simulação.")