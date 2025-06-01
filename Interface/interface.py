# Menu Interativo
def menu():
    while True:
        print("\n==== Menu Principal ====")
        print("1. Cadastrar Aluno | 2. Cadastrar Disciplina | 3. Cadastrar Nota | 4. Exibir Dados")
        print()
        print("5. Exportar para CSV | 6. Importar de CSV | 0. Sair")
        print()
        
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
                print("Dados enviados com sucesso!")
            except:
                print("Erro ao enviar dados.")

        elif opcao == "6":
            try:
                importar_csv()
                print("Dados carregados com sucesso!")
            except:
                print("Erro ao carregar dados.")

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção não encontrada. Tente novamente.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    menu()





