# 📊 Modelagem e Simulação

Repositório da disciplina **Modelagem e Simulação**, contendo implementações práticas em Python voltadas para simulação de sistemas reais e análise de desempenho utilizando Teoria das Filas.

---

## 🎯 Objetivo

Aplicar conceitos de modelagem matemática e simulação computacional para representar sistemas reais, analisar seu comportamento e avaliar métricas de desempenho.

Os projetos desenvolvidos simulam:

- 📚 Sistema de biblioteca
- 🍽 Restaurante Universitário (RU)
- 🛒 Sistema de filas (supermercado e RU)
- 📈 Modelo de filas M/M/c
- 🧮 Fórmula de Erlang C

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Biblioteca `math`
- Biblioteca `numpy`

---

## 📂 Estrutura do Projeto

### 📚 1. Sistema de Biblioteca

Simulação de:

- Cadastro de usuários (aluno, professor, funcionário)
- Cadastro de livros
- Empréstimo e devolução
- Controle de disponibilidade
- Histórico de empréstimos
- Empréstimos ativos

**Conceitos aplicados:**
- Listas e dicionários
- Funções
- Validações
- Simulação de eventos

---

### 🍽 2. Simulação de Restaurante Universitário (RU)

Sistema que:

- Controla créditos dos alunos
- Permite uso de refeição se houver crédito
- Registra atendimentos realizados
- Registra tentativas negadas por falta de crédito

**Conceitos aplicados:**
- Modelagem de entidades
- Controle de estado
- Registro estatístico
- Simulação de fluxo de atendimento

---

### 📈 3. Análise de Sistema de Filas

Simulação baseada em dados coletados:

- Taxa de chegada (λ)
- Taxa de atendimento (μ)
- Número de servidores (c)
- Taxa de ocupação (ρ)

Cenários simulados:

- Restaurante Universitário
- Caixa de Supermercado

Classificação do sistema:

- Sistema subutilizado
- Sistema eficiente
- Sistema no limite
- Sistema em colapso

---

### 🧮 4. Implementação da Fórmula de Erlang C (M/M/c)

Implementação matemática da probabilidade de espera:

P(wait)

Cálculo das métricas:

- Utilização (ρ)
- Probabilidade de espera
- Tempo médio na fila (Wq)
- Número médio na fila (Lq)
- Tempo médio no sistema (W)
- Número médio no sistema (L)

**Conceitos aplicados:**

- Teoria das Filas
- Modelo M/M/c
- Fórmula de Erlang C
- Lei de Little
- Estabilidade do sistema (a < c)

---

## ▶ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/modelagem-simulacao.git
