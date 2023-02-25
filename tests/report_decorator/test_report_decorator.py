import pytest
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport


@pytest.fixture
def report():
    return [
        {
            "id": 2,
            "nome_do_produto": "arroz",
            "nome_da_empresa": "Arrozini",
            "data_de_fabricacao": "2021-05-01",
            "data_de_validade": "2023-06-02",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "ao abrigo da luz",
        },
        {
            "id": 1,
            "nome_do_produto": "feijão fradinho",
            "nome_da_empresa": "Feijãini",
            "data_de_fabricacao": "2021-05-01",
            "data_de_validade": "2023-06-02",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "ao abrigo da luz",
        },
        {
            "id": 3,
            "nome_do_produto": "feijão",
            "nome_da_empresa": "Feijãini",
            "data_de_fabricacao": "2021-05-01",
            "data_de_validade": "2023-06-02",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "ao abrigo da luz",
        },
    ]


def test_decorar_relatorio(report):
    simple_report = ColoredReport(SimpleReport).generate(report)
    complete_report = ColoredReport(CompleteReport).generate(report)

    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[36m"

    assert simple_report == (
        f"{GREEN}Data de fabricação mais antiga:{RESET} "
        f"{BLUE}2021-05-01{RESET}\n"
        f"{GREEN}Data de validade mais próxima:{RESET} "
        f"{BLUE}2023-06-02{RESET}\n"
        f"{GREEN}Empresa com mais produtos:{RESET} {RED}Feijãini{RESET}"
    )

    assert complete_report == (
        f"{GREEN}Data de fabricação mais antiga:{RESET} "
        f"{BLUE}2021-05-01{RESET}\n"
        f"{GREEN}Data de validade mais próxima:{RESET} "
        f"{BLUE}2023-06-02{RESET}\n"
        f"{GREEN}Empresa com mais produtos:{RESET} {RED}Feijãini{RESET}\n"
        f"Produtos estocados por empresa:\n"
        f"- Arrozini: 1\n"
        f"- Feijãini: 2\n"
    )
