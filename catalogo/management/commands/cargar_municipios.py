import csv
from django.core.management.base import BaseCommand, CommandError
from catalogo.models import c_entidad, c_municipio, c_pais


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
                print('Leyendo el archvio "{}" ...'.format(options["csv"]))
                TheData = csv.DictReader(CsvFile, dialect=csv.excel)
                try:
                    for row in TheData:
                        entidad = c_entidad.objects.get(pk=row["CVEGEOENTIDAD"])
                        pais = c_pais.objects.get(pk=entidad.ClavePais.CvePais)
                        CveMunicipio = row["CVEMUNICIPIO"]
                        CveGoeMunicipio =row["CVEGEOGRAFICA"]
                        print(
                            f"CveGeograficaMunicipio = {CveGoeMunicipio}, ClaveMunicipo = {CveMunicipio}, Nombre = {row['NOMBRE']}"
                        )
                        municipio = c_municipio(
                            CveGeograficaMunicipio=CveGoeMunicipio,
                            Nombre=row["NOMBRE"],
                            ClaveMunicipio=CveMunicipio,
                            ClavePais=pais,
                            ClaveGeogEntidad=entidad,
                        )
                        print(municipio)
                        municipio.save()
                except Exception as e:
                    print(e)
        except FileNotFoundError:
            raise CommandError('El archivo "{}" does not exist'.format(options["csv"]))

    print("Finalizado!")
