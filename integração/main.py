import csv


#dados.py
#Primeira classe a ser criada 

class Aluno:
    def __init__(self, id_aluno, nome):
        self.id_aluno = id_aluno
        self.nome = nome

class Disciplina:
    def __init__(self, id_disciplina, nome):
        self.id_disciplina = id_disciplina
        self.nome = nome

class Nota:
    def __init__(self, id_aluno, id_disciplina, valor):
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        self.valor = valor

# Listas de dados 
alunos = []
disciplinas = []
notas = []

# Funções de cadastro 
def cadastrar_aluno(id_aluno, nome):
    alunos.append(Aluno(id_aluno, nome))

def cadastrar_disciplina(id_disciplina, nome):
    disciplinas.append(Disciplina(id_disciplina, nome))

def cadastrar_nota(id_aluno, id_disciplina, valor):
    notas.append(Nota(id_aluno, id_disciplina, valor))

# Função para exportar dados para arquivos .cvs
def exportar_csv():
    with open('alunos.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id_aluno', 'nome'])
        for aluno in alunos:
            writer.writerow([aluno.id_aluno, aluno.nome])

    with open('disciplinas.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id_disciplina', 'nome'])
        for disc in disciplinas:
            writer.writerow([disc.id_disciplina, disc.nome])

    with open('notas.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id_aluno', 'id_disciplina', 'valor'])
        for nota in notas:
            writer.writerow([nota.id_aluno, nota.id_disciplina, nota.valor])

# Função para importar dados de arquivos .cvs
def importar_csv():
    alunos.clear()
    disciplinas.clear()
    notas.clear()

    try:
        with open('alunos.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cadastrar_aluno(int(row['id_aluno']), row['nome'])

        with open('disciplinas.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cadastrar_disciplina(int(row['id_disciplina']), row['nome'])

        with open('notas.csv', mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cadastrar_nota(int(row['id_aluno']), int(row['id_disciplina']), float(row['valor']))
    except FileNotFoundError:
        print("Arquivos CSV não encontrados.")

# Função para exibir os dados armazenados
def exibir_dados():
    print("\n--- Alunos ---")
    for aluno in alunos:
        print(f"{aluno.id_aluno} - {aluno.nome}")

    print("\n--- Disciplinas ---")
    for disc in disciplinas:
        print(f"{disc.id_disciplina} - {disc.nome}")

    print("\n--- Notas ---")
    for nota in notas:
        nome_aluno = next((a.nome for a in alunos if a.id_aluno == nota.id_aluno), "Desconhecido")
        nome_disc = next((d.nome for d in disciplinas if d.id_disciplina == nota.id_disciplina), "Desconhecido")
        print(f"{nome_aluno} - {nome_disc}: {nota.valor}")



#ordenacao.py
#ordena uma lista usando o método bubble sort

def bubble_sort(lista, chave=lambda x: x):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            #se o item atual for maior que o próximo, troca de lugar
            if chave(lista[j]) > chave(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
#ordena uma lista usando o método merge sort
def merge_sort(lista, chave=lambda x: x):
    if len(lista) <= 1:
        return lista  #Já está ordenada
    meio = len(lista) // 2
    #Divide a lista e ordena recursivamente as metades
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    #Junta as listas ordenadas
    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    i = j = 0
    #Junta as duas listas ordenadas
    while i < len(esquerda) and j < len(direita):
        if chave(esquerda[i]) <= chave(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, chave=lambda x: x):
    if len(lista) <= 1:
        return lista  #Já está ordenada
    pivo = lista[0]  #Escolhe o pivô
    iguais = [x for x in lista if chave(x) == chave(pivo)]
    menores = [x for x in lista if chave(x) < chave(pivo)]
    maiores = [x for x in lista if chave(x) > chave(pivo)]
    #Ordena recursivamente
    return quick_sort(maiores, chave) + iguais + quick_sort(menores, chave)


#busca.py
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

#Dados de exemplo 
notas = [7.5, 8.0, 6.0, 9.2, 5.0]
valor = 6.0

alunos = [
    {"nome": "Ana", "disciplina": "Matemática", "nota": 8.5},
    {"nome": "Carlos", "disciplina": "História", "nota": 6.0},
    {"nome": "Beatriz", "disciplina": "Matemática", "nota": 9.2},
    {"nome": "Daniel", "disciplina": "História", "nota": 7.0},
    {"nome": "Eduarda", "disciplina": "Português", "nota": 5.5}
]

#Uso da busca sequencial na lista simples
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

#interface.py
#Menu interativo para o usuário cadastrar dados, exibir, importar/exportar, etc.

def menu():
    while True:
        print("\n==== Menu Principal ====")
        print("1. Cadastrar Aluno | 2. Cadastrar Disciplina | 3. Cadastrar Nota | 4. Exibir Dados")
        print("5. Exportar para CSV | 6. Importar de CSV | 0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id_aluno = int(input("Id do aluno: "))
                nome = input("Nome do Aluno: ")
                cadastrar_aluno(id_aluno, nome)
                print("Aluno cadastrado com sucesso!")
            except:
                print("Dados inválidos.")

        elif opcao == "2":
            try:
                id_disciplina = int(input("Id da disciplina: "))
                nome = input("Nome da Disciplina: ")
                cadastrar_disciplina(id_disciplina, nome)
                print("Disciplina cadastrada com sucesso!")
            except:
                print("Dados inválidos.")

        elif opcao == "3":
            try:
                id_aluno = int(input("Id do Aluno: "))
                id_disciplina = int(input("Id da Disciplina: "))
                valor = float(input("Nota: "))
                cadastrar_nota(id_aluno, id_disciplina, valor)
                print("Nota cadastrada com sucesso!")
            except:
                print("Dados inválidos.")

        elif opcao == "4":
            exibir_dados()

        elif opcao == "5":
            try:
                exportar_csv()
                print("Dados exportados com sucesso!")
            except:
                print("Erro ao exportar dados.")

        elif opcao == "6":
            try:
                importar_csv()
                print("Dados importados com sucesso!")
            except:
                print("Erro ao importar dados.")

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção não encontrada. Tente novamente.")


#main.py
# Ponto de entrada do programa
if __name__ == "__main__":
    menu()

