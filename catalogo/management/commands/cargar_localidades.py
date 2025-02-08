import csv
import re

from django.core.management.base import BaseCommand, CommandError
from catalogo.models import c_municipio, c_localidad, c_entidad, c_pais


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #    print(f"{parser}")
    #    return super().add_arguments(parser)

    def add_arguments(self, parser):
        parser.add_argument("--csv", type=str)

    def handle(self, *args, **options):
        models = dict()
        count = 0
        try:
            with open(options["csv"], mode="r", newline="") as CsvFile:
                print('Leyendo el archvio "{}" ...'.format(options["csv"]))
                TheData = csv.DictReader(CsvFile, dialect=csv.excel)

                try:
                    for row in TheData:
                        count += 1

                        municipio = c_municipio.objects.get(pk=row["CVEGEOMUNICIPIO"])
                        entidad = c_entidad.objects.get(
                            pk=municipio.ClaveGeogEntidad.ClaveEntidad
                        )
                        pais = c_pais.objects.get(pk=municipio.ClavePais.CvePais)
                        if count % 100 == 0:
                            print(f"{count} registros cargados...")

                        localidad = c_localidad(
                            CveGeograficaLocalidad=row["CVEGEOGRAFICA"],
                            ClaveLocalidad=row["CVELOCALIDAD"],
                            Nombre=row["NOMBRE"],
                            ClaveGeogMunicipio=municipio,
                            ClaveGeogEntidad=entidad,
                            ClavePais=pais,
                        )
                        localidad.save()
                except Exception as Excp:
                    print("Error:", Excp)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Finalizado!")
