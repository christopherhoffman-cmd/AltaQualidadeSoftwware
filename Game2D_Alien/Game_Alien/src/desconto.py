from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular_desconto(self, preco):
        pass


class DescontoNormal(Desconto):
    def calcular_desconto(self, preco):
        return preco * 0.1

class DescontoVIP(Desconto): 
    def calcular_desconto(self, preco):
        return preco * 0.2


class DescontoPremium(Desconto):
    def calcular_desconto(self, preco):
        return preco * 0.3


