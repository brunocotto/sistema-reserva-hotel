from abc import ABC, abstractmethod
from reserva import Reserva

class RepositorioReservasInterface(ABC):
    @abstractmethod
    def inserir_reserva(self, reserva: Reserva):
        pass

    @abstractmethod
    def verificar_disponibilidade(self, data: str, numero_quarto: int) -> bool:
        pass