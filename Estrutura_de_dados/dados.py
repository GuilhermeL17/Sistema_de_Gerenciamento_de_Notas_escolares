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
        