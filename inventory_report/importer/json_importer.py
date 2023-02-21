import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        try:
            with open(path, encoding="utf-8") as json_file:
                return json.load(json_file)
        except Exception:
            raise ValueError("Arquivo inválido")
