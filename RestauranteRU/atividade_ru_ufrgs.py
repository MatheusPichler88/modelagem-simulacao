"""Atividade de simulçao de um restaurante universitário.
Objetivo: Gerenciar o uso de refeições por alunos com base em seus créditos disponíveis.
Cada aluno tem um número de matrícula, nome, curso e créditos.
O sistema deve permitir que um aluno use uma refeição se tiver créditos disponíveis,
atualizar o número de créditos e manter um registro do total de atendimentos e negados
sem créditos.
"""

alunos = None
ru = None

"""Lista de dados dos alunos como se fosse um banco de dados do RU."""
lista_alunos = [
    
    {"matricula": "UFRGS0001", "nome": "Matheus", "curso": "Ciência da Computação", "creditos": 5},
    {"matricula": "UFRGS0002", "nome": "Gabriel", "curso": "Engenharia de Software", "creditos": 0},
    {"matricula": "UFRGS0003", "nome": "Andriza", "curso": "Sistemas de Informação", "creditos": 1},
    {"matricula": "UFRGS0004", "nome": "Ana", "curso": "Direito", "creditos": 3},
    {"matricula": "UFRGS0005", "nome": "Julia", "curso": "Medicina", "creditos": 2}
]

"""Dicionário para armazenar informações do RU."""
dicionario_ru = {"nome": "Restaurante Universitário da UFRGS", "total de atendimentos": 0, "total de negados sem créditos": 0}

def encontrar_aluno(matricula):
    """Encontra um aluno na lista pelo número de matrícula."""
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def usar_refeicao(matricula):
    """Permite que um aluno use uma refeição no RU, se tiver créditos disponiveis."""
    global dicionario_ru
    aluno = encontrar_aluno(matricula)
    if aluno:
        if aluno["creditos"] > 0:
            aluno["creditos"] -= 1
            dicionario_ru["total de atendimentos"] += 1
            return f"Refeição liberada. Créditos restantes: {aluno['creditos']}"
        else:
            dicionario_ru["total de negados sem créditos"] += 1
            return "Sem créditos, por favor, recarregar."
    else:
        return "Aluno não encontrado, matrícula inexistente."

"""Lista de matriculas utilizadas para fazer a simulação"""
lista_matriculas = ["UFRGS0001", "UFRGS0002","UFN0001", "UFRGS0003", "UFRGS0004", "UFRGS0005", "UFRGS0006"]

"""Looping onde percorre a lista de matriculas e tenta usar a refeição no RU"""
for matricula in lista_matriculas:
    resultado = usar_refeicao(matricula)
    print(f"Matrícula: {matricula} - {resultado}")
    
"""Relatório final do RU."""
print("\nRelatório do RU:")
print(f"Total de atendimentos: {dicionario_ru['total de atendimentos']}")
print(f"Total de negados sem créditos: {dicionario_ru['total de negados sem créditos']}")
print("Créditos restantes dos alunos:")
"""Exibe os créditos restantes de cada aluno."""
for aluno in lista_alunos:
    print(f"{aluno['nome']} ({aluno['matricula']}): {aluno['creditos']} créditos")