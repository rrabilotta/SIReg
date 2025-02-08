import csv

from django.core.management.base import BaseCommand, CommandError
from catalogo.models import c_moneda


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--csv", type=str)

    def handle(self, *args, **options):

        try:
            with open(
                options["csv"], mode="r", newline=""
            ) as CsvFile:
                print('Leyendo el archvio "{}" ...'.format(options["csv"]))
                TheData = csv.DictReader(CsvFile, dialect=csv.excel)

                try:
                    for row in TheData:
                        str_row = f"CveMoneda = {row['CVEMONEDA']}, Moneda={row['NOMMONEDA']}"
                        print(str_row)
                        moneda = c_moneda(
                            CveMoneda=row["CVEMONEDA"],
                            Moneda=row["NOMMONEDA"]
                        )
                        moneda.save()
                except Exception as Excp:
                    print("Error:", Excp)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Finalizado!")
