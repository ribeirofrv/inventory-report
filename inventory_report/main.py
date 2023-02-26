import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        _method, file_path, report_type = sys.argv
        importer = get_importer(file_path)
        return sys.stdout.write(
            InventoryRefactor(importer).import_data(file_path, report_type))
    except ValueError:
        return sys.stderr.write("Verifique os argumentos\n")


def get_importer(file_path):
    if file_path.endswith("csv"):
        return CsvImporter
    elif file_path.endswith("json"):
        return JsonImporter
    elif file_path.endswith("xml"):
        return XmlImporter


if __name__ == "__main__":
    main()
