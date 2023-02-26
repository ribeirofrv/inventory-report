from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer = Importer):
        self.importer = importer
        self.data = list()

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path: str, type: str):
        self.data.extend(self.importer.import_data(file_path))
        try:
            return (
                SimpleReport.generate(self.data)
                if type == "simples"
                else CompleteReport.generate(self.data)
            )
        except:
            raise ValueError("Arquivo inválido")
