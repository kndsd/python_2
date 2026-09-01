tarefas = []

while True:
    print("\n--- MENU DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")
    
    opcao = input("Opção: ")

    if opcao == '1':
        item = input("Digite a tarefa: ")
        tarefas.append(item)
        print("Tarefa adicionada!")
    elif opcao == '2':
        item = input("Digite a tarefa a remover: ")
        if item in tarefas:
            tarefas.remove(item)
            print("Tarefa removida!")
        else:
            print("Tarefa não encontrada.")
    elif opcao == '3':
        print("Tarefas atuais:", tarefas)
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")