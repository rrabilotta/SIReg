import csv

from django.core.management.base import BaseCommand, CommandError
from registro.models import c_regimen_fiscal

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
                        str_row = f"ClaveSAT = {row['CVESAT']}"
                        print(str_row)
                        regimen_fiscal = c_regimen_fiscal(
                            ClaveSAT=row["CVESAT"],
                            Nombre=row["NOMBRE"],
                            Descripcion=row['NOMBRE'],
                            PersonaMoral=row['PERSONAMORAL']
                        )
                        regimen_fiscal.save()
                except Exception as Excp:
                    print("Error:", Excp)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Finalizado!")
