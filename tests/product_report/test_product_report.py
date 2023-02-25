from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="farinha",
        nome_da_empresa="Farinini",
        data_de_fabricacao="2021-05-01",
        data_de_validade="2023-06-02",
        numero_de_serie="123456789",
        instrucoes_de_armazenamento="ao abrigo da luz",
    )

    assert f"{product}" == (
        "O produto farinha"
        " fabricado em 2021-05-01"
        " por Farinini com validade"
        " até 2023-06-02"
        " precisa ser armazenado ao abrigo da luz."
    )
