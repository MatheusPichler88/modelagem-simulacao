import numpy as np 

'''OBJETIVO Criar um programa Python que analise um sistema de filas real, calculando λ (taxa de
chegada), μ (taxa de atendimento), ρ (ocupação) e interpretando os resultados.'''

taxa_chegada = [5, 7, 6, 8, 9, 4, 6, 7, 5, 8, 6, 7, 5, 9, 6, 2, 4, 7, 1, 4, 8, 2, 2, 5, 6, 3, 5, 1, 3, 2]  #Taxa de chegada (λ) - número de pessoas que chegam por minuto
tempo_atendimento = [1, 2, 1.5, 2.5, 3, 1, 1.5, 2, 1, 2.5, 1.5, 2, 1, 3, 1.5, 0.5, 1, 2, 0.5, 1, 2.5, 0.5, 0.5, 1.5, 1.5, 1, 1.5, 0.5, 1, 0.5] #Tempo de atendimento (μ) - tempo médio que um cliente leva para ser atendido
numero_servidores = 8  #Número de servidores (atendentes/caixas/computadores)
taxa_atendimento = len(taxa_chegada) / sum(tempo_atendimento)  #Cálculo da taxa de atendimento (μ)
taxa_ocupacao = (sum(taxa_chegada) / len(taxa_chegada)) / (numero_servidores * taxa_atendimento)  #Cálculo da taxa de ocupação (ρ)

if taxa_ocupacao < 0.5:
    interpretacao = "Sistema subutilizado"
elif 0.5 <= taxa_ocupacao < 0.8:
    interpretacao = "Sistema eficiente"
elif 0.8 <= taxa_ocupacao < 1.0: 
    interpretacao = "Sistema no limite"
else:
    interpretacao = "Sistema em colapso"
    

print("""ANÁLISE DE FILAS - RU da Faculdade
Horário: 12h às 12h30
=====================================""")
print("DADOS COLETADOS:")
print("Total de chegadas em 30 minutos:", sum(taxa_chegada), "pessoas")
print("Total de atendimentos em 30 minutos:", numero_servidores * taxa_atendimento, "pessoas")
print("Número de servidores: ", numero_servidores)
print("=====================================")
print("CÁLCULOS:")
print(f"Taxa de chegada (λ): {sum(taxa_chegada) / len(taxa_chegada):.2f} pessoas por minuto")
print(f"Taxa de atendimento (μ): {taxa_atendimento:.2f} pessoas por minuto")
print(f"Taxa de ocupação (ρ): {taxa_ocupacao:.2f}")
print("=====================================")
print("INTERPRETAÇÃO:")
print(interpretacao,"Cuidado com o aumento de chegadas!")
print("Recomenda-se manter a taxa de ocupação abaixo de 0.8 para garantir um atendimento eficiente.")
print("=====================================")



"""Caixa de supermercado"""
taxa_chegada = [3, 4, 2, 5, 6, 3, 4, 5, 3, 4, 2, 5, 3, 6, 4, 1, 2, 4, 1, 2, 3, 6, 4, 1, 2, 4, 1, 2, 4, 5]
tempo_atendimento = [2, 3, 2.5, 3.5, 4, 2, 2.5, 3, 2, 3.5, 2.5, 3, 2, 4, 2.5, 1.5, 2, 3, 1.5, 2, 3.5, 1.5, 1.5, 2.5, 2.5, 2, 2.5, 1.5, 2, 1.5]
numero_servidores = 5
taxa_atendimento = len(taxa_chegada) / sum(tempo_atendimento)
taxa_ocupacao = (sum(taxa_chegada) / len(taxa_chegada)) / (numero_servidores * taxa_atendimento)

if taxa_ocupacao < 0.5:
    interpretacao = "Sistema subutilizado"
elif 0.5 <= taxa_ocupacao < 0.8:
    interpretacao = "Sistema eficiente"
elif 0.8 <= taxa_ocupacao < 1.0: 
    interpretacao = "Sistema no limite"
else:
    interpretacao = "Sistema em colapso"    
print("\nANÁLISE DE FILAS - Caixa de Supermercado")
print("DADOS COLETADOS:")
print("Total de chegadas em 30 minutos:", sum(taxa_chegada), "pessoas")
print("Total de atendimentos em 30 minutos:", numero_servidores * taxa_atendimento, "pessoas")
print("Número de servidores: ", numero_servidores)
print("=====================================")
print("CÁLCULOS:")
print(f"Taxa de chegada (λ): {sum(taxa_chegada) / len(taxa_chegada):.2f} pessoas por minuto")
print(f"Taxa de atendimento (μ): {taxa_atendimento:.2f} pessoas por minuto")
print(f"Taxa de ocupação (ρ): {taxa_ocupacao:.2f}")
print("=====================================")
print("INTERPRETAÇÃO:")
print(interpretacao,"Cuidado com o aumento de chegadas!")
print("Recomenda-se manter a taxa de ocupação abaixo de 0.8 para garantir um atendimento eficiente.")
pr
print("=====================================")