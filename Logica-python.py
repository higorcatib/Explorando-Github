# Lista inicial de tarefas
tarefas = ["Comprar leite", "Estudar Python", "Assistir filme"]

def exibir_tarefas(tarefas):
    """Função para exibir todas as tarefas"""
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa}")
    print("\n")

def adicionar_tarefa(tarefas, tarefa):
    """Função para adicionar uma nova tarefa"""
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')

def remover_tarefa(tarefas, indice):
    """Função para remover uma tarefa pelo índice"""
    try:
        removida = tarefas.pop(indice - 1)
        print(f'Tarefa "{removida}" removida com sucesso!')
    except IndexError:
        print("Erro: Índice de tarefa inválido!")

def editar_tarefa(tarefas, indice, nova_tarefa):
    """Função para editar uma tarefa existente"""
    try:
        tarefas[indice - 1] = nova_tarefa
        print(f'Tarefa {indice} editada com sucesso para "{nova_tarefa}"!')
    except IndexError:
        print("Erro: Índice de tarefa inválido!")

def main():
    """Função principal para gerenciar o programa"""
    while True:
        exibir_tarefas(tarefas)
        print("Selecione uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Editar Tarefa")
        print("4. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            nova_tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa)
        elif opcao == "2":
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(tarefas, indice)
            except ValueError:
                print("Erro: Por favor, insira um número válido!")
        elif opcao == "3":
            try:
                indice = int(input("Digite o número da tarefa para editar: "))
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                editar_tarefa(tarefas, indice, nova_tarefa)
            except ValueError:
                print("Erro: Por favor, insira um número válido!")
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()
