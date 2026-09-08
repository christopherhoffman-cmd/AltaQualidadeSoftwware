import pytest

from src.desconto import DescontoNormal, DescontoVIP


@pytest.fixture
def desconto_normal():
    return DescontoNormal()


def test_desconto_normal(desconto_normal):

    resultado = desconto_normal.calcular(100)

    assert resultado == 10, f"Esperado: 10, mas obteve: {resultado}"


@pytest.fixture
def desconto_vip():
    return DescontoVIP()


def test_desconto_100_vip(desconto_vip):

    assert desconto_vip.calcular(100) == 20


def test_desconto_200_vip(desconto_vip):

    assert desconto_vip.calcular(200) == 40