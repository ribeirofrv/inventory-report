from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(stock):
        simple_report = SimpleReport.generate(stock)

        # products stocked by company -> name of company: number of products
        products_by_company = {}
        for item in stock:
            company = item["nome_da_empresa"]
            if company in products_by_company:
                products_by_company[company] += 1
            else:
                products_by_company[company] = 1

        companies = ""
        for company, number in products_by_company.items():
            companies += f"- {company}: {number}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies}"
        )
