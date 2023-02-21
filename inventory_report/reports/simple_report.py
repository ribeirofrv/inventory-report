class SimpleReport:
    @staticmethod
    def generate(stock):
        oldest_date = min(
            [item["data_de_fabricacao"] for item in stock]
        )

        closest_date = min([item["data_de_validade"] for item in stock])

        products_by_company = {}
        for item in stock:
            company = item["nome_da_empresa"]
            if company in products_by_company:
                products_by_company[company] += 1
            else:
                products_by_company[company] = 1

        company_bigger_stock = max(
            products_by_company, key=products_by_company.get
        )

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
