#Menu Interativo 
def menu ()
 while True:
     print("\n === Menu Principal ===")
     print(" 1. Cadastrar Aluno")
     print(" 2. Cadastrar Diciplina")
     print(" 3. Cadastrar Nota")
     print(" 4. Exibir Dados")
     print(" 5. Enviar para CSV")
     print(" 6. Trazer de CSV")
     print(" 0. Sair ")
     opcao = input(" Escolha uma opção )
if opcao == "1":
                try:
                    id_aluno = int(input("Id do aluno: "))
                    nome = input("Nome do Aluno: ")
                    cadastrar_aluno(id_aluno , nome)
                    print("Aluno cadastrado com sucesso! ")
                except:
                    print ("Dados inválidos.")
                    
 elif opcao == "2":
                try:
                    id_disciplina = int(input("Id do diciplina: "))
                    nome = input("Nome da Diciplina: ")
                    cadastrar_diciplina(id_diciplina , nome)
                    print("Diciplina cadastrada com sucesso! ")
                except:
                    print ("Dados inválidos.")

elif opcao == "2":
                try:
                    id_disciplina = int(input("Id da diciplina: "))
                    nome = input("Nome da Diciplina: ")
                    cadastrar_diciplina(id_diciplina , nome)
                    print("Diciplina cadastrada com sucesso! ")
                except:
                    print ("Dados inválidos.")

elif opcao == "3":
                try:
                    id_aluno = int(input("Id do Aluno: "))
                    id_disciplina = int(input("Id da Diciplina: "))
                    valor = float(input("Nota: "))
                    cadastrar_nota(id_aluno, id_diciplina , nota)
                    print("Nota cadastrada com sucesso! ")
                except:
                    print ("Dados inválidos.")

elif opcao == "4":
  exibir_dados()
elif opcao == "5":
enviar_csv()
print("Dados enviados com sucesso!")
elif opcao == "6":
trazer_csv()
print("Dados carregados com sucesso!")
elif opcao == "0":
print("Programa encerrado!")
break
else:
print("Opção não encontrada. Tente novamente.")

if__name__ == "__main__":
menu()






