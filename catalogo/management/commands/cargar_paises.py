import csv

from django.core.management.base import BaseCommand, CommandError
from catalogo.models import c_pais


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--csv", type=str)

    def handle(self, *args, **options):

        try:
            with open(
                options["csv"], mode="r", newline="", encoding="utf-8"
            ) as CsvFile:
                print('Leyendo el archvio "{}" ...'.format(options["csv"]))
                TheData = csv.DictReader(CsvFile, dialect=csv.excel)
                print(TheData.fieldnames)

                try:
                    for row in TheData:
                        str_row = f"CvePais = {row['CVEPAIS']}, Nombre={row['NOMBRE']}"
                        print(str_row)
                        paises = c_pais(
                            CvePais=row["CVEPAIS"],
                            Nombre=row["NOMBRE"],
                            CodigoTelefonico=row["CODIGOTEL"],
                            Continente=row["CONTINENTE"],
                        )
                        paises.save()
                except Exception as e:
                    print("Error:", type(e))
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Finalizado!")
