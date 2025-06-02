# ordena uma lista usando o método bubble sort
def bubble_sort(lista, chave=lambda x: x):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # se o item atual for maior que o próximo, troca de lugar
            if chave(lista[j]) > chave(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# ordena uma lista usando o método merge sort
def merge_sort(lista, chave=lambda x: x):
    if len(lista) <= 1:
        return lista  # já está ordenada
    meio = len(lista) // 2
    # divide a lista em duas partes e ordena cada uma
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    # junta as duas partes ordenadas
    return merge(esquerda, direita, chave)

# junta duas listas ordenadas em uma só
def merge(esquerda, direita, chave):
    resultado = []
    i = j = 0
    # compara os itens das duas listas e junta em ordem
    while i < len(esquerda) and j < len(direita):
        if chave(esquerda[i]) <= chave(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    # adiciona o que sobrou das duas listas
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# ordena uma lista usando o método quick sort
def quick_sort(lista, chave=lambda x: x):
    if len(lista) <= 1:
        return lista  # já está ordenada
    pivo = lista[0]  # escolhe o primeiro item como pivô
    # separa a lista em menores, iguais e maiores que o pivô
    iguais = [x for x in lista if chave(x) == chave(pivo)]
    menores = [x for x in lista if chave(x) < chave(pivo)]
    maiores = [x for x in lista if chave(x) > chave(pivo)]
    # ordena recursivamente e junta tudo
    return quick_sort(maiores, chave) + iguais + quick_sort(menores, chave)

# teste do código
if __name__ == "__main__":
    # lista de alunos (dicionários com nome, nota e disciplina)
    alunos = [
        {"nome": "Carlos", "nota": 7.5, "disciplina": "Matemática"},
        {"nome": "Ana", "nota": 9.0, "disciplina": "Português"},
        {"nome": "Beatriz", "nota": 6.0, "disciplina": "História"}
    ]

    # ordena por nome com bubble sort
    ordenado_nome = bubble_sort(alunos[:], chave=lambda x: x["nome"])
    print("\n==============================")
    print("Ordenado por Nome")
    print("==============================")
    for aluno in ordenado_nome:
        print(f"Nome: {aluno['nome']:<10} Nota: {aluno['nota']} Disciplina: {aluno['disciplina']}")

    # ordena por nota (maior para menor) com merge sort
    ordenado_nota = merge_sort(alunos[:], chave=lambda x: -x["nota"])
    print("\n==============================")
    print("Ordenado por Nota (Maior para Menor)")
    print("==============================")
    for aluno in ordenado_nota:
        print(f"Nome: {aluno['nome']:<10} Nota: {aluno['nota']} Disciplina: {aluno['disciplina']}")

    # ordena por disciplina com quick sort
    ordenado_disciplina = quick_sort(alunos[:], chave=lambda x: x["disciplina"])
    print("\n==============================")
    print("Ordenado por Disciplina")
    print("==============================")
    for aluno in ordenado_disciplina:
        print(f"Nome: {aluno['nome']:<10} Nota: {aluno['nota']} Disciplina: {aluno['disciplina']}")
