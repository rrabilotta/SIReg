import csv

from django.core.management.base import BaseCommand, CommandError
from catalogo.models import (
    c_localidad,
    c_asentamiento_humano,
    c_municipio,
    c_pais,
    c_entidad,
)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--csv", type=str)

    def handle(self, *args, **options):
        models = dict()

        try:
            with open(
                options["csv"], mode="r", newline=""
            ) as CsvFile:
                print('Leyendo el archvio "{}" ...'.format(options["csv"]))
                TheData = csv.DictReader(CsvFile, dialect=csv.excel)
                contador = 0
                try:
                    for row in TheData:
                        contador += 1
                        localidad = c_localidad.objects.get(pk=row["CVEGEOLOCALIDAD"])                       
                        municipio = c_municipio.objects.get(pk=localidad.ClaveGeogMunicipio.CveGeograficaMunicipio)
                        entidad = c_entidad.objects.get(pk=municipio.ClaveGeogEntidad.ClaveEntidad)
                        pais = c_pais.objects.get(pk=entidad.ClavePais.CvePais)
                        if contador % 100 == 0:
                            print(f" {contador} registros cargados...")
                        asentamiento = c_asentamiento_humano(
                            Nombre=row["ASENTAMIENTO"],
                            CodigoPostal=row["CODIGOPOSTAL"],
                            TipoAsentamiento=row["TIPOASENTAMIENTO"],
                            ClaveAsentamiento=row["CVEASENTAMIENTO"],
                            ClaveGeograficaAsentamiento=row["CVEGEOASENTAMIENTO"],
                            ClaveGeogLocalidad=localidad,
                            ClaveGeogMunicipio=municipio,
                            ClaveGeogEntidad=entidad,
                            ClavePais=pais,
                            FUltimaActualizacion=row["ULTIMAACTUALIZACION"],
                            AutoridadResponsable=row["AUTORIDADRESPONSABLE"],
                        )
                        asentamiento.save()
                except Exception as e:
                    print(e)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

        print("Import complete")
