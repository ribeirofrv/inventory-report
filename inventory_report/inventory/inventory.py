from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if "csv" in path:
            file_to_report = CsvImporter.import_data(path)

        if "json" in path:
            file_to_report = JsonImporter.import_data(path)

        if "xml" in path:
            file_to_report = XmlImporter.import_data(path)

        return (
            SimpleReport.generate(file_to_report)
            if report_type == "simples"
            else CompleteReport.generate(file_to_report)
        )
