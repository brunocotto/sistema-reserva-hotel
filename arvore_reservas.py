from datetime import datetime
from interfaces import RepositorioReservasInterface
from exceptions import ReservaExistenteException

class ArvoreReservas(RepositorioReservasInterface):
    def __init__(self):
        self.raiz = None

    def inserir_reserva(self, reserva):
        data_atual = datetime.now().date()
        data_reserva = datetime.strptime(reserva.data, "%Y-%m-%d").date()

        # Verifica se a data da reserva é maior ou igual à data atual
        if data_reserva < data_atual:
            return False  # Indicativo de falha devido à data inválida

        # Verifica se o quarto está disponível na data da reserva
        if not self.verificar_disponibilidade(reserva.data, reserva.numero_quarto):
            return False  # Indicativo de falha devido ao quarto já estar reservado para essa data

        # Chama a inserção recursiva na árvore
        self.raiz = self._inserir_reserva_recursivo(self.raiz, reserva)
        return True  # Indicativo de sucesso após a inserção na árvore


    def _inserir_reserva_recursivo(self, no, reserva):
        if not no:
            return No(reserva)

        # Comparação considerando data e número do quarto para inserção na árvore
        if reserva.data == no.reserva.data and reserva.numero_quarto == no.reserva.numero_quarto:
            # Não permitir a inserção de reservas no mesmo dia e quarto
            return False

        if reserva.data < no.reserva.data or (reserva.data == no.reserva.data and reserva.numero_quarto < no.reserva.numero_quarto):
            no.esquerda = self._inserir_reserva_recursivo(no.esquerda, reserva)
        else:
            no.direita = self._inserir_reserva_recursivo(no.direita, reserva)

        return no

    def verificar_disponibilidade(self, data, numero_quarto):
        return not self._buscar_reserva_recursivo(self.raiz, data, numero_quarto)

    def _buscar_reserva_recursivo(self, no, data, numero_quarto):
        if not no:
            return None

        if data == no.reserva.data and numero_quarto == no.reserva.numero_quarto:
            return no

        if data < no.reserva.data:
            return self._buscar_reserva_recursivo(no.esquerda, data, numero_quarto)
        else:
            return self._buscar_reserva_recursivo(no.direita, data, numero_quarto)

    def cancelar_reserva(self, data, numero_quarto):
        self.raiz = self._remover_reserva_recursivo(self.raiz, data, numero_quarto)

    def _remover_reserva_recursivo(self, no, data, numero_quarto):
        if not no:
            return no

        if data < no.reserva.data:
            no.esquerda = self._remover_reserva_recursivo(no.esquerda, data, numero_quarto)
        elif data > no.reserva.data:
            no.direita = self._remover_reserva_recursivo(no.direita, data, numero_quarto)
        else:
            if numero_quarto != no.reserva.numero_quarto:
                no.direita = self._remover_reserva_recursivo(no.direita, data, numero_quarto)
            else:
                if not no.esquerda:
                    temp = no.direita
                    no = None
                    return temp
                elif not no.direita:
                    temp = no.esquerda
                    no = None
                    return temp

                temp = self._encontrar_minimo(no.direita)
                no.reserva.data = temp.reserva.data
                no.reserva.numero_quarto = temp.reserva.numero_quarto
                no.direita = self._remover_reserva_recursivo(no.direita, temp.reserva.data, temp.reserva.numero_quarto)

        return no

    def listar_reservas(self, numero_quarto):
        reservas_quarto = []
        self._listar_reservas_recursivo(self.raiz, numero_quarto, reservas_quarto)
        return reservas_quarto

    def _listar_reservas_recursivo(self, no, numero_quarto, lista_reservas):
        if no is not None:
            if no.reserva.numero_quarto == numero_quarto:
                lista_reservas.append({
                    "data": no.reserva.data,
                    "numero_quarto": no.reserva.numero_quarto,
                    "nome": no.reserva.nome,
                    "cpf": no.reserva.cpf
                })
            if numero_quarto <= no.reserva.numero_quarto:
                self._listar_reservas_recursivo(no.esquerda, numero_quarto, lista_reservas)
            if numero_quarto >= no.reserva.numero_quarto:
                self._listar_reservas_recursivo(no.direita, numero_quarto, lista_reservas)


    def _encontrar_minimo(self, no):
        current = no
        while current.esquerda:
            current = current.esquerda
        return current

class No:
    def __init__(self, reserva):
        self.reserva = reserva
        self.esquerda = None
        self.direita = None
