import csv

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

#Função para exportar o arquivo .csv

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

#Função para importar um .csv

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



