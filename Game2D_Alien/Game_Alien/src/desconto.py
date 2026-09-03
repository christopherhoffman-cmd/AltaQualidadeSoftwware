from abc import ABC, abstractmethod


class IDesconto(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass

class ICupom(ABC):

    @abstractmethod
    def aplicar_cupom(self, codigo):
        pass

class IVIP(ABC):

    @abstractmethod
    def validar_usuario_vip(self, usuario):
        pass


class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1

class DescontoVIP(IDesconto, ICupom, IVIP):

    def calcular(self, valor):
        return valor * 0.2

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"

class DescontoPremium(IDesconto):

    def calcular(self, valor):
        return valor * 0.3

