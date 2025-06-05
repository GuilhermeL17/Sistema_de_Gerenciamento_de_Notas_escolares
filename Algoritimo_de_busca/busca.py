# Função de busca sequencial em lista simples (por valor)
def busca_sequencial(lista, valor_procurado):
    for indice, elemento in enumerate(lista):
        if elemento == valor_procurado:
            return indice  # Retorna o índice onde encontrou
    return -1  # Retorna -1 se não encontrou

# Função de busca por nome exato em lista de alunos
def busca_por_nome(lista_alunos, nome_procurado):
    resultados = []
    for aluno in lista_alunos:
        if aluno["nome"].lower() == nome_procurado.lower():
            resultados.append(aluno)
    return resultados

# Função de busca por disciplina em lista de alunos
def busca_por_disciplina(lista_alunos, disciplina_procurada):
    resultados = []
    for aluno in lista_alunos:
        if aluno["disciplina"].lower() == disciplina_procurada.lower():
            resultados.append(aluno)
    return resultados

# --- Dados de exemplo ---
notas = [7.5, 8.0, 6.0, 9.2, 5.0]
valor = 6.0

alunos = [
    {"nome": "Ana", "disciplina": "Matemática", "nota": 8.5},
    {"nome": "Carlos", "disciplina": "História", "nota": 6.0},
    {"nome": "Beatriz", "disciplina": "Matemática", "nota": 9.2},
    {"nome": "Daniel", "disciplina": "História", "nota": 7.0},
    {"nome": "Eduarda", "disciplina": "Português", "nota": 5.5}
]

# --- Uso da busca sequencial na lista simples ---
posicao = busca_sequencial(notas, valor)
if posicao != -1:
    print(f"Valor {valor} encontrado na posição {posicao}")
else:
    print("Valor não encontrado na lista.")

print("\n--- Busca por nome 'Beatriz' ---")
resultados_nome = busca_por_nome(alunos, "Beatriz")
for aluno in resultados_nome:
    print(aluno)

print("\n--- Busca por disciplina 'História' ---")
resultados_disciplina = busca_por_disciplina(alunos, "História")
for aluno in resultados_disciplina:
    print(aluno)