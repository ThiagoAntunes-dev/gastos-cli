from main import adicionar_gasto, total_gastos, gastos
def setup_function():
    gastos.clear()


def test_adicionar_gasto():
    adicionar_gasto("Almoço", 20)
    assert len(gastos) == 1


def test_valor_negativo():
    try:
        adicionar_gasto("Erro", -10)
    except ValueError:
        assert True
    else:
        assert False


def test_total_gastos():
    adicionar_gasto("A", 10)
    adicionar_gasto("B", 20)
    assert total_gastos() == 30