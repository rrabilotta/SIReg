import csv

from django.core.management.base import BaseCommand, CommandError
from catalogo.models import c_nombre_vialidad


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
                count=0

                try:
                    for row in TheData:
                        count+=1
                        if count%100 ==0:
                            print(f"{count} cargados...")
                        nombresvialidades = c_nombre_vialidad(
                            Nombre=row["NOMBRE"],
                        )
                        nombresvialidades.save()
                except Exception as Excp:
                    print("Error:", Excp)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Finalizado!")
