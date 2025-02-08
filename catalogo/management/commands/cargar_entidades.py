import csv
from django.core.management.base import BaseCommand, CommandError
from catalogo.models import c_entidad, c_pais


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #    print(f"{parser}")
    #    return super().add_arguments(parser)

    def add_arguments(self, parser):
        parser.add_argument("--csv", type=str)

    def handle(self, *args, **options):

        try:
            with open(
                options["csv"], mode="r", newline=""
            ) as CsvFile:
                print('Leyendpo el archvio "{}" ...'.format(options["csv"]))
                TheData = csv.DictReader(CsvFile, dialect=csv.excel)
                cvePais = c_pais.objects.get(pk="MEX")
                print(cvePais.CvePais)

                try:
                    for row in TheData:
                        str_row = f"CveGeograficaEntidad = {row['CVEGEOGRAFICA']}, Entidad = {row['NOMBRE']}, CvePais='MEX'"
                        print(str_row)
                        entidad = c_entidad(
                            CveGeograficaEntidad=row["CVEGEOGRAFICA"],
                            ClaveEntidad=row["CVEENTIDAD"],
                            Nombre=row["NOMBRE"],
                            ClavePais=cvePais,
                        )
                        entidad.save()
                except Exception as Excp:
                    print("Error:", Excp)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Finalizado!")
