from django.db import models


# Create your models here.


class c_moneda(models.Model):
    """Catálogo de monedas"
    Catálogo de monedas, indica su nombre, clave y símbilo (si existe)

    Returns:
        str: Clave de la moneda (3 posiciones)
    """

    CveMoneda = models.CharField(
        max_length=5,
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="CVEMONEDA",
        verbose_name="Clave ISO de la moneda",
    )
    Moneda = models.CharField(
        max_length=50,
        db_index=True,
        null=False,
        db_column="NOMMONEDA",
        verbose_name="Moneda",
    )

    class Meta:
        ordering = ("Moneda",)
        verbose_name_plural = "Catálogo de monedas"

    def __str__(self):
        return f"{self.Moneda}"


class c_pais(models.Model):
    """Catálogo de países

    Nota: ClavePais para México será MEX, Colombia COL, Perús PER, etc.

    Returns:
        str: Clave del país (3 posiciones)
    """

    CvePais = models.CharField(
        max_length=5,
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="CVEPAIS",
        verbose_name="Clave ISO",
        help_text="Clave ISO (tres posiciones) del país",
    )
    Nombre = models.CharField(
        max_length=100,
        unique=False,
        null=False,
        db_column="NOMBRE",
        verbose_name="País",
        help_text="Nombre del país",
    )
    CodigoTelefonico = models.CharField(
        max_length=10,
        db_column="CODIGOTEL",
        verbose_name="Código telefónico",
        help_text="Código telefónico",
    )
    Moneda = models.ForeignKey(
        c_moneda,
        on_delete=models.CASCADE,
        db_column="CVEMONEDA",
        null=True,
        verbose_name="Moneda",
        help_text="Moneda de curso legal",
    )
    Continente = models.CharField(
        max_length=15,
        null=True,
        verbose_name="Continente",
        help_text="Continente",
        db_column="CONTINENTE",
    )

    class Meta:
        ordering = ("Nombre", "CvePais")
        verbose_name_plural = "Países"

    def __str__(self):
        return f"{self.Nombre}"

    def __repr__(self):
        return f"{self.Nombre}"

class c_entidad(models.Model):
    """Catálogo de entidades. departamento o provincia

    Returns:
        str: Clave de la entidad federativa, departamento o provincia
    """

    CveGeograficaEntidad = models.CharField(
        max_length=20,
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="CVEGEOGRAFICA",
        verbose_name="Clave geográfica",
        help_text="Clave geográfica INEGI de la entidad",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Entidad",
        help_text="Nombre de la entidad",
    )
    ClaveEntidad = models.CharField(
        max_length=2,
        null=True,
        db_column="CVEENTIDAD",
        verbose_name="Clave de la entidad",
        help_text="Clave INEGI de la entidad",
    )
    ClavePais = models.ForeignKey(
        c_pais,
        on_delete=models.CASCADE,
        null=True,
        db_constraint=False,
        verbose_name="País",
        help_text="País",
        db_column="CVEPAIS",
    )

    class Meta:
        ordering = ("CveGeograficaEntidad", "Nombre")
        verbose_name_plural = "Entidades (estados, provincias o departamentos)"

    def __str__(self):
        return f"{self.Nombre}, {self.ClavePais.Nombre}"

    def __repr__(self):
        return f"{self.Nombre}"


class c_municipio(models.Model):
    """Catálogo de municipios

    Returns:
        str: Clave del municipio
    """

    CveGeograficaMunicipio = models.CharField(
        max_length=20,
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="CVEGEOGRAFICA",
        verbose_name="Clave geográfica",
        help_text="Clave geográfica INEGI del municipio",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Municipio",
        help_text="Nombre del municipio",
    )
    ClaveMunicipio = models.CharField(
        max_length=3,
        null=True,
        db_column="CVEMUNICIPIO",
        verbose_name="Clave del Municipio",
        help_text="Clave INEGI del municipio respecto a la entidad",
    )
    ClaveGeogEntidad = models.ForeignKey(
        c_entidad,
        on_delete=models.CASCADE,
        null=True,
        db_index=True,
        db_column="CVEGEOENTIDAD",
        db_constraint=False,
        verbose_name="Entidad",
        help_text="Entidad",
    )

    class Meta:
        ordering = ("CveGeograficaMunicipio", "Nombre")
        verbose_name_plural = "Municipios"

    def __str__(self):
        return f"{self.Nombre}, {self.ClaveGeogEntidad.Nombre}"

    def __repr__(self):
        return f"{self.Nombre}"

class c_localidad(models.Model):
    """Catálogo de localidades

    Returns:
        str: Clave de localidad
    """

    CveGeograficaLocalidad = models.CharField(
        max_length=20,
        primary_key=True,
        null=False,
        db_default="",
        db_index=True,
        db_column="CVEGEOGRAFICA",
        verbose_name="Clave geográfica",
        help_text="Clave geográfica INEGI de la localidad",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_default="LOCALIDAD",
        db_column="NOMBRE",
        verbose_name="Localidad",
        help_text="Nombre de la localidad",
    )
    ClaveLocalidad = models.CharField(
        max_length=4,
        null=True,
        db_column="CVELOCALIDAD",
        verbose_name="Clave de la localidad",
        help_text="Clave INEGI  de la localidad respecto al municipio",
    )
    ClaveGeogMunicipio = models.ForeignKey(
        c_municipio,
        on_delete=models.CASCADE,
        db_constraint=False,
        db_index=True,
        db_column="CVEGEOMUNICIPIO",
        verbose_name="Municipio",
        help_text="Municipio y entidad",
    )

    class Meta:
        ordering = ("CveGeograficaLocalidad", "Nombre")
        verbose_name_plural = "Localidades"
        unique_together = ("CveGeograficaLocalidad", "Nombre")

    def __str__(self):
        return f"{self.Nombre}, {self.ClaveGeogMunicipio.Nombre}, {self.ClaveGeogMunicipio.ClaveGeogEntidad.Nombre}"

    def __repr__(self):
        return f"{self.Nombre}"


class c_asentamiento_humano(models.Model):
    """Catálogo de asentamientos humanos

    Fuente: INEGI

    Returns:
        str: Clave geográfica del asentamiento
    """

    ClaveGeograficaAsentamiento = models.CharField(
        max_length=20,
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="CVEGEOASENTAMIENTO",
        verbose_name="Clave geográfica",
        help_text="Clave geográfica INEGI del asentamiento",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_default="",
        db_column="ASENTAMIENTO",
        verbose_name="Asentamiento",
        help_text="Nombre del asentamiento (colonia, barrio, pueblo, unidad habitacional, etc.)",
    )
    CodigoPostal = models.CharField(
        max_length=5,
        null=False,
        db_index=True,
        db_column="CODIGOPOSTAL",
        verbose_name="Código postal",
        help_text="Código postal SEPOMEX",
    )
    AutoridadResponsable = models.CharField(
        max_length=100,
        null=True,
        db_column="AUTORIDADRESPONSABLE",
        verbose_name="Atoridad responsable",
        help_text="Autoridad responsable por el dato",
    )
    TipoAsentamiento = models.CharField(
        max_length=50,
        null=False,
        db_default="COLONIA",
        db_column="TIPOASENTAMIENTO",
        verbose_name="Tipo",
        help_text="Tipo de asentamiento humano",
    )
    FUltimaActualizacion = models.CharField(
        max_length=10,
        db_column="ULTIMAACTUALIZACION",
        verbose_name="Fecha de la actualización",
        help_text="Fecha de la actualización correspondiente (mes/año)",
    )
    ClaveAsentamiento = models.CharField(
        max_length=4,
        null=True,
        db_column="CVEASENTAMIENTO",
        verbose_name="Clave del asentamiento",
        help_text="Clave INEGI del asentamiento respecto a la localidad",
    )
    ClaveGeogLocalidad = models.ForeignKey(
        c_localidad,
        on_delete=models.CASCADE,
        db_constraint=False,
        db_index=True,
        db_column="CVEGEOLOCALIDAD",
        verbose_name="Localidad",
        help_text="Localidad, municipio y entidad",
    )

    class Meta:
        ordering = ("CodigoPostal", "ClaveGeograficaAsentamiento", "Nombre")
        verbose_name_plural = "Asentamientos (colonias, barrios, etc.)"
        unique_together = ("ClaveGeograficaAsentamiento", "Nombre", "CodigoPostal")

    def __str__(self):
        return f"{self.Nombre}, {self.ClaveGeogLocalidad.Nombre}, {self.ClaveGeogLocalidad.ClaveGeogMunicipio.Nombre}, {self.ClaveGeogLocalidad.ClaveGeogMunicipio.ClaveGeogEntidad.Nombre}"

    def __repr__(self):
        return f"{self.Nombre}"


class c_clase_documento(models.Model):
    """Catálogo de clases de documentos

    Nota: Clase de documento es un conjunto clasificador de documentos, constituidos pero no
    limitado a:
    - Escritura
    - Poder
    - Carta
    - Oficio
    - Plan
    - Programa
    - Identidad
    - etc.


    Returns:
        int: Identificador de la clase de documento
    """

    IdClaseDocumento = models.AutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDCLASEDOC"
    )
    Nombre = models.CharField(
        max_length=50, null=False, unique=True, db_column="NOMBRE"
    )
    Descripcion = models.TextField(db_column="DESCRIPCION")
    Oficial = models.BooleanField(db_default=False, db_column="OFICIAL")
    Expira = models.BooleanField(db_default=True, db_column="EXPIRA")

    class Meta:
        ordering = ("Nombre",)
        verbose_name_plural = "Catálogo de clase de documentos"

    def __str__(self):
        return f"{self.Nombre}, {str(self.Expira)}, {str(self.Oficial)}"


class c_tipo_documento_identidad(models.Model):
    """Catálogo de tipos de documentos de identidad

    Returns:
        int: Identificador del tipo de documento
    """

    IdTipoDocumentoIdentidad = models.AutoField(
        primary_key=True, db_index=True, null=False, db_column="IDTIPODOCIDENT"
    )
    Nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        db_default="Credencial de ...",
        db_column="NOMBRE",
        verbose_name="Tipo de documento",
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")
    Expira = models.BooleanField(
        default=True, db_column="DOCEXPIRA", verbose_name="¿El documento expira?"
    )

    class Meta:
        ordering = ("Nombre", "Expira")
        verbose_name_plural = "Tipos de documentos de identidad"

    def __str__(self):
        return f"{self.Nombre}, {self.Expira}"


class c_nombre_vialidad(models.Model):
    """Tabla de vialidades

    Returns:
        str: El nombre de la vialidad en mayúsculas
    """

    IdNombreVialidad = models.BigAutoField(
        primary_key=True, null=False, db_index=True, db_column="IDNOMVIALIDAD"
    )

    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_default="Calle",
        db_index=True,
        db_column="NOMBRE",
    )

    Aliases = models.JSONField(
        db_column="ALIASES",
        verbose_name="Aliases",
        db_default="",
        help_text="Aliases (viariantes) en JSON del nombre",
    )

    class Meta:
        ordering = ("Nombre",)
        verbose_name_plural = (
            "Nombres de vialidades (Calles, avenidas, callejones, etc.)"
        )

    def __str__(self):
        return f"{self.Nombre},{self.Aliases}"


class c_regimen_fiscal(models.Model):
    """Catálogo de regímenes fiscales

    Returns:
        int: Identificador del régimen fiscal
    """

    IdRegimenFiscal = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDREGIMENFISCAL",
    )
    ClaveSAT = models.IntegerField(
        db_column="CVESAT",
        db_default=0,
        db_index=True,
        null=False,
        verbose_name="Clave SAT",
        help_text="Clave SAT del régimen fiscal",
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Régimen fiscal",
        help_text="Régimen fiscal",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        verbose_name="Descripción",
        help_text="Descripción del régime fiscal",
    )
    PersonaMoral = models.BooleanField(
        db_default=False,
        db_column="PERSONAMORAL",
        verbose_name="Aplica a persona moral",
        help_text="Selecciónelo si es aplicable a una persona moral o jurídica",
    )
    Vigente = models.BooleanField(
        db_column="VIGENTE",
        default=False,
        verbose_name="Está vigente",
        help_text="Selecciónelo si es un régimen fiscal vigente",
    )

    class Meta:
        ordering = ("Nombre", "Descripcion", "PersonaMoral")
        verbose_name_plural = "Catálogo de regímenes fiscales"

    def __str__(self):
        return str(self.IdRegimenFiscal)


class c_uso_cdfi(models.Model):
    """Catálogo de usos de los usos

    Returns:
        int: Identificador del uso del certificado fiscal
    """

    IdUsoCDFI = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDUSOCDFI"
    )
    ClaveSAT = models.CharField(
        max_length=5,
        db_column="CVESAT",
        null=False,
        db_default="",
        verbose_name="Clave SAT",
        help_text="Clave SAT del régimen fiscal",
    )
    Nombre = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Uso del CDFI",
        help_text="Uso del certificado digital fiscal",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        null=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    PersonaMoral = models.BooleanField(
        db_default=False,
        db_column="PERSONAMORAL",
        verbose_name="Perosna moral",
        help_text="Aplicable a personas morales o jurídicas",
    )
    PersonaFisica = models.BooleanField(
        db_default=False,
        db_column="PERSONAFISICA",
        verbose_name="Perosna física",
        help_text="Aplicable a personas físicas",
    )

    class Meta:
        ordering = ("ClaveSAT", "Nombre", "PersonaMoral")
        verbose_name_plural = "Catálogo de usos de los CDFI"

    def __str__(self):
        return str(self.IdUsoCDFI)


class c_clase_reporte(models.Model):
    """Catálogo de clases de reportes

    Returns:
        int: Identificador de clase de reportes
    """

    IdClaseReporte = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDTIPOCONSTANCIA",
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Clase de reporte",
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")

    class Meta:
        ordering = ("Nombre",)
        verbose_name_plural = "Catálogo de clases de reportes"

    def __str__(self):
        return str(self.IdClaseReporte)


class c_tipo_recibo(models.Model):
    """Catálogo de tipos de recibos

    Returns:
        int: Identificador del tipo de recibo
    """

    IdTipoRecibo = models.AutoField(
        primary_key=True, unique=True, db_index=True, db_column="IDTIPORECIBO"
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Tipo de recibo",
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")

    class Meta:
        ordering = ("Nombre", "Descripcion")
        verbose_name_plural = "Tipos de recibos"

    def __str__(self):
        return str(self.IdTipoRecibo)

