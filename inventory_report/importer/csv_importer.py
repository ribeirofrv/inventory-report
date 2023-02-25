import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if "csv" not in path:
            raise ValueError("Arquivo inválido")
        # try:
        with open(path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            return list(reader)
        # except Exception:
        #     raise ValueError("Arquivo inválido")
