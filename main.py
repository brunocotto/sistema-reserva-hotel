from reserva import Reserva
from arvore_reservas import ArvoreReservas

# Lista com os dados das 20 reservas


def exibir_menu():
    print("\n Sistema de Reservas de Hotel ")
    print("1. Inserir Reserva")
    print("2. Verificar Disponibilidade")
    print("3. Cancelar Reserva")
    print("4. Listar Reservas por Quarto")
    print("5. Sair")

if __name__ == "__main__":
    arvore_reservas = ArvoreReservas()

    while True:
        exibir_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            data = input("Digite a data da reserva (AAAA-MM-DD): ")
            numero_quarto = int(input("Digite o número do quarto: "))
            nome = input("Digite o seu nome: ")
            cpf = input("Digite o seu CPF(XXX.XXX.XXX-XX): ")

            reserva_sucesso = arvore_reservas.inserir_reserva(Reserva(data, numero_quarto, nome, cpf))

            if reserva_sucesso:
              print("Reserva inserida com sucesso.")
            else:
                print("Não é possível inserir reservas para datas passadas.")
        elif opcao == "2":
            data = input("Digite a data para verificar disponibilidade (AAAA-MM-DD): ")
            numero_quarto = int(input("Digite o número do quarto: "))
            disponivel = arvore_reservas.verificar_disponibilidade(data, numero_quarto)
            if disponivel:
                print(f"O quarto {numero_quarto} está disponível na data {data}.")
            else:
                print(f"O quarto {numero_quarto} não está disponível na data {data}.")
        elif opcao == "3":
            data = input("Digite a data da reserva a ser cancelada (AAAA-MM-DD): ")
            numero_quarto = int(input("Digite o número do quarto: "))
            arvore_reservas.cancelar_reserva(data, numero_quarto)
            print("Reserva cancelada com sucesso!")
        elif opcao == "4":
            numero_quarto = int(input("Digite o número do quarto para listar as reservas: "))
            reservas_quarto = arvore_reservas.listar_reservas(numero_quarto)
            if reservas_quarto:
                print(f"Reservas do quarto {numero_quarto}:")
                for reserva in reservas_quarto:
                    print(reserva)
            else:
                print(f"Não há reservas para o quarto {numero_quarto}.")
        elif opcao == "5":
            print("Saindo do sistema... CHUCHUBELEZA... Sopinha de minhoca")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

