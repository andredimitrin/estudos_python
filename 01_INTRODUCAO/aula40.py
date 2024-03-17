"""
Calculadora com while

"""

while True:
    print("\nSelecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "5":
        print("Saindo do programa...")
        break

    if opcao not in {"1", "2", "3", "4"}:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    try:
        num_1 = float(input("Digite o primeiro valor: "))
        num_2 = float(input("Digite o segundo valor: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        continue

    if opcao == "1":
        resultado = num_1 + num_2
        print(f"A soma de {num_1} e {num_2} é igual a: {resultado}")
    elif opcao == "2":
        resultado = num_1 - num_2
        print(f"A subtração de {num_1} por {num_2} é igual a: {resultado}")
    elif opcao == "3":
        resultado = num_1 * num_2
        print(f"A multiplicação de {num_1} por {num_2} é igual a: {resultado}")
    elif opcao == "4":
        if num_2 == 0:
            print("Erro: divisão por zero.")
        else:
            resultado = num_1 / num_2
            print(f"A divisão de {num_1} por {num_2} é igual a: {resultado}")
