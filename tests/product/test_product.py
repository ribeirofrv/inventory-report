from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Arroz",
        "Arroz do Brasil",
        "2020-01-01",
        "2022-01-01",
        "123456789",
        "em local seco",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Arroz"
    assert product.nome_da_empresa == "Arroz do Brasil"
    assert product.data_de_fabricacao == "2020-01-01"
    assert product.data_de_validade == "2022-01-01"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "em local seco"
