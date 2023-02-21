import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        try:
            with open(path, encoding="utf-8") as xml_file:
                return list(
                    xmltodict.parse(xml_file.read())["dataset"]["record"]
                )
        except Exception:
            raise ValueError("Arquivo inválido")
