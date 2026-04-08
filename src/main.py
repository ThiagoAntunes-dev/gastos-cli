gastos = []

def adicionar_gasto(nome, valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    gastos.append({"nome": nome, "valor": valor})

def listar_gastos():
    return gastos

def total_gastos():
    return sum(g["valor"] for g in gastos)

def remover_gasto(nome):
    global gastos
    gastos = [g for g in gastos if g["nome"] != nome]


def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total")
        print("4 - Remover gasto")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            valor = float(input("Valor: "))
            adicionar_gasto(nome, valor)

        elif opcao == "2":
            for g in listar_gastos():
                print(g)

        elif opcao == "3":
            print("Total:", total_gastos())

        elif opcao == "4":
            nome = input("Nome: ")
            remover_gasto(nome)

        elif opcao == "0":
            break


if __name__ == "__main__":
    menu()