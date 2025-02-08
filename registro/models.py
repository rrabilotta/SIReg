# from django.db import models
from django.db import models
from django.utils.timezone import now
from catalogo.models import (
    c_asentamiento_humano,
    c_entidad,
    c_localidad,
    c_moneda,
    c_municipio,
    c_pais,
    c_regimen_fiscal,
    c_uso_cdfi,
    c_tipo_documento_identidad,
    c_clase_documento,
    c_clase_reporte,
)
from sireg.contantes import Const
from adminusr.models import usuario, fedatario_y_funcionario

# Create your models here.


class autorizacion(models.Model):
    """Control de autorizaciones de los procesos registrales.

    Returns:
        str: Devuelve la cadena de autorización.
    """

    Cadena = models.CharField(
        max_length=300,
        primary_key=True,
        unique=True,
        null=False,
        db_column="AUTORIZACION",
        verbose_name="Cadena de autorización",
        help_text="Cadena de autorización",
    )

    FHAutorizacion = models.DateTimeField(
        db_column="FHAUTORIZACION",
        verbose_name="Fecha y hora de la autorización",
        help_text="Fecha y hora del registro de la autorización",
        db_default=now(),
        null=False,
    )
    FirmadoElectronicamente = models.BooleanField(
        db_default=True,
        db_column="FIRMADOELEC",
        verbose_name="e-firma",
        help_text="Firmado electrónicamente si es verdadero",
    )
    Detalles = models.JSONField(
        db_column="DETALLES",
        verbose_name="Detalles",
        help_text="Detalles de la autorización",
        null=False,
    )
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES",
        null=True,
        verbose_name="Datos adicionales",
        help_text="Datos adicionales",
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        default=now(),
        verbose_name="Fecha y hora de alta",
        help_text="Fecha y hora de alta",
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        null=True,
        verbose_name="Fecha y hora de la última modificación",
        help_text="Fecha y hora de la última modificación",
    )

    IdUsuario = models.ForeignKey(
        usuario,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDUSUARIO",
        verbose_name="Usuario",
        help_text="Usuario",
    )

    class Meta:
        ordering = (
            "Cadena",
            "FHAutorizacion",
        )
        verbose_name_plural = "Autorizaciones"

    def __str__(self):
        return f"{self.IdAutorizacion}"


class c_tipo_instrumento(models.Model):
    """Catálogo de tipos de instrumentos (jurídicos)

    Returns:
        int: Identificador del tipo de instrumento
    """

    IdTipoInstrumento = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDTIPOINSTRUMENTO",
        verbose_name="Identificador del tipo de instrumento",
        help_text="Identificador del tipo de instrumento jurídico",
    )
    Nombre = models.CharField(
        max_length=50,
        null=False,
        db_column="NOMBRE",
        verbose_name="Nombre del tipo de instrumento",
        help_text="Nombre del tipo de instrumento jurídico",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        null=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    Emisor = models.IntegerField(
        choices=Const.EMISOR_INSTRUMENTO,
        db_default=0,
        db_column="EMISOR",
        verbose_name="Emisor del instrumento",
        help_text="Quien emite el instrumento",
    )

    class Meta:
        ordering = ("Nombre", "Descripcion")
        verbose_name_plural = "Tipos de instrumentos legales"

    def __str__(self):
        return f"{self.Nombre}"


class c_uso_inmueble(models.Model):
    """Catálogo del uso de los inmuebles

    Returns:
        int: Identificador del uso de un inmueble
    """

    IdUsoInmueble = models.AutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="IDUSOINMUEBLE",
        verbose_name="Identificador del uso del inmueble",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_column="NOMBRE",
        db_index=True,
        verbose_name="Uso del inmueble",
        help_text="Uso del inmueble",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION", verbose_name="Descripción", help_text="Descripción"
    )

    def __str__(self):
        return self.IdUsoInmueble


class c_tipo_construccion(models.Model):
    """Catálogo de tipos de construcciones

    Nota: Tipología constructiva

    Returns:
        int: Identificador del tipo de construcción
    """

    IdTipoConstruccion = models.AutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="IDTIPOCONST",
        verbose_name="Identificador del tipo de construcción",
        help_text="Identificador del tipo de construcción",
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Tipo de construcción",
        help_text="Tipo de construcción",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION", verbose_name="Descripción", help_text="Descripción"
    )

    def __str__(self):
        return self.IdTipoConstruccion


class c_interes_juridico(models.Model):
    """Catálogo de intereses jurídicos

    Nota: Estos pueden ser:
    - Propietarioo
    - Usufructuario
    - Autoridad judicial
    - Autoridad ejecutiva
    - Juzgado
    - Autoridad ministerial
    - etc.

    Returns:
        int: Identificador del interés jurídico
    """

    IdInteresJuridico = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_column="IDINTERESJURIDICO",
        verbose_name="Identificador del interés juridico",
        help_text="Identificador del interés juridico",
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Interés jurídico",
        help_text="Interés jurídico",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        null=False,
        verbose_name="Descripción",
        help_text="Descripción",
    )

    class Meta:
        ordering = ("Nombre",)
        verbose_name_plural = "Catálogo de intereses jurídicos"

    def __str__(self):
        return f"{self.Nombre}"


class documento(models.Model):
    """tabla de documentos

    Returns:
        int: Identificador del documento
    """

    IdDocumento = models.BigAutoField(
        primary_key=True,
        db_index=True,
        null=False,
        unique=True,
        db_column="IDDOCUMENTO",
        verbose_name="Identificador del documento",
        help_text="Identificador del documento",
    )
    Archivo = models.CharField(
        max_length=250,
        null=False,
        db_default=" ",
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Archivo",
        help_text="Archivo",
    )
    FormatoDocumento = models.IntegerField(
        choices=Const.FORMATO_DOCUMENTOS,
        db_default=0,
        db_column="FORMATO",
        verbose_name="Formato del archivo",
        help_text="Formato del documento",
    )
    HashContenidohDocumento = models.TextField(
        db_column="HASHCONTDOC",
        verbose_name="Hash del contenido",
        help_text="Hash del contenido",
    )
    FHDigitalizacion = models.DateTimeField(
        db_column="FHDIGITALIZACION",
        null=True,
        verbose_name="Fecha y hora de su digitalización",
        help_text="Fecha y hora de la digitalización",
    )
    FHCarga = models.DateTimeField(
        db_column="FHCARGA",
        null=False,
        db_index=True,
        verbose_name="Fecha y hora de la carga",
        help_text="Fecha y hora de la carga",
    )
    TamCarga = models.FloatField(
        db_column="TAMCARGA",
        null=False,
        verbose_name="Tamaño del archivo (bytes)",
        help_text="Tamaño del archivo en bytes",
    )
    FHCotejo = models.DateTimeField(
        db_column="FHCOTEJO",
        null=True,
        verbose_name="Fecha y hora de cotejo",
        help_text="Fecha y hora de cotejo",
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        verbose_name="Fecha y hora de alta del registro",
        help_text="Fecha y hora de la última modificación",
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        verbose_name="Fecha y hora de la última modificación",
        help_text="Fecha y hora de la última modificación",
        null=True,
    )

    IdClaseDocumento = models.ForeignKey(
        c_clase_documento,
        on_delete=models.CASCADE,
        db_column="IDCLASEDOC",
        verbose_name="Clase de documento",
        help_text="Clase de documento",
    )

    def __str__(self):
        return self.IdDocumento


class r_documento_usuario(models.Model):
    """Tabla de relación entre las entidades documento y usuario

    Nota: Esta entidad resuelve la problemática de que un documento tiene
    una relación de varios usuarios con diferentes roles respecto a un documento

    Roles:
    - Digitalización
    - Carga
    - Cotejo
    - Verificación
    - Auditoría
    - etc.

    Returns:
        int: Identificador de la relación
    """

    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")
    Rol = models.IntegerField(choices=Const.ROL_USUARIO_DOCUMENTO, db_column="ROL")
    IdUsuario = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )
    IdDocumento = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCUMENTO"
    )


class instrumento(models.Model):
    """instrumento legal

    Returns:
        int: Identificador del instrumento
    """

    IdInstrumento = models.BigAutoField(
        primary_key=True,
        db_index=True,
        unique=True,
        null=False,
        db_column="IDINSTRUMENTO",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_default=" ",
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Instrumento",
        help_text="Nombre del instrumento jurídico",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        verbose_name="Descripción",
        help_text="Descripción del instrumento jurídico",
    )
    Extracto = models.TextField(
        db_column="EXTRACTO",
        verbose_name="Extracto",
        help_text="Extracto del instrumento jurídico",
    )
    FechaInstrumento = models.DateField(
        db_column="FINSTRUMENTO",
        verbose_name="Fecha de elaboración",
        help_text="Fecha de elaboración del instrumento",
    )
    RegistroInstrumento = models.CharField(
        max_length=100,
        null=True,
        db_column="REGINSTRUMENTO",
        verbose_name="Registro",
        help_text="Registro (folio o equivalente) del instrumento",
    )
    FechaRegistro = models.DateField(
        db_column="FREGISTRO",
        null=True,
        verbose_name="Fecha de registro",
        help_text="Fecha del registro",
    )
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES", verbose_name="Datos adicionales"
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA", verbose_name="Fecha y hora del alta", default=now()
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        null=True,
        verbose_name="Fecha y hora de la última modificación",
    )
    Vigente = models.BooleanField(db_default=False, db_column="VIGENTE")
    IdTipoInstrumento = models.ForeignKey(
        c_tipo_instrumento,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPOINSTRUMENTO",
        verbose_name="Tipo de instrumento",
        help_text="Tipo de instrumento",
    )
    IdFedFun = models.ForeignKey(
        fedatario_y_funcionario,
        models.CASCADE,
        null=True,
        db_column="IDFEDFUNC",
        verbose_name="Fedatario/funcionario",
        help_text="Notario, corredor público, juez o funcionario",
    )
    IdDocumento = models.ForeignKey(
        documento,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDDOCUMENTO",
        verbose_name="Documento del instrumento",
        help_text="Documento",
    )

    class Meta:
        ordering = ("FechaInstrumento", "Nombre", "IdFedFun", "Extracto", "Descripcion")
        verbose_name_plural = "Instrumentos jurídicos y administrativos"

    def __str__(self):
        return self.IdInstrumento


class r_entidad_instrumento(models.Model):
    """Tabla de relación entre instrumento y entidad

    Returns:
        int: Identificador de la relación
    """

    IdUsuario = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )
    IdInstrumento = models.ForeignKey(
        instrumento, on_delete=models.CASCADE, null=True, db_column="IDINSTRUMENTO"
    )


class sujeto_fiscal(models.Model):
    RFC = models.CharField(
        max_length=15,
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="RFC",
    )
    NombreORazonSocial = models.CharField(
        max_length=150, null=False, db_index=True, db_column="NOMBRERAZONSOCIAL"
    )
    PersonaMoral = models.BooleanField(db_default=False, db_column="PERSONAMORAL")
    Nombre = models.CharField(
        max_length=100, null=False, db_index=True, db_column="NOMBRE"
    )
    PrimerApellido = models.CharField(
        max_length=100, null=False, db_index=True, db_column="APELLIDO1"
    )
    SegundoApellido = models.CharField(
        max_length=100, null=False, db_index=True, db_column="APELLIDO2"
    )
    CorreoFacturacion = models.EmailField(db_column="CORREO")
    Vialidad = models.CharField(
        max_length=100, null=False, db_index=True, db_column="NOMVIALIDAD"
    )
    NumeroExterior = models.CharField(
        max_length=10, db_index=True, db_column="NUMEXTERIOR"
    )
    NumeroInterior = models.CharField(max_length=10, db_column="NUMINTERIOR")
    Km = models.CharField(max_length=10, db_column="KM")
    Manzana = models.CharField(max_length=10, db_column="MANZANA")
    Lote = models.CharField(max_length=10, db_column="LOTE")
    Asentamiento = models.CharField(max_length=50, db_column="ASENTAMIENTO")

    Localidad = models.ForeignKey(
        c_localidad, on_delete=models.CASCADE, db_column="CVELOCALIDAD", null=True
    )
    Municipio = models.ForeignKey(
        c_municipio, on_delete=models.CASCADE, db_column="CVEMUNICIPIO", null=True
    )
    Entidad = models.ForeignKey(
        c_entidad, on_delete=models.CASCADE, db_column="CVEENTIDAD", null=True
    )

    IdRegimenFiscal = models.ForeignKey(
        c_regimen_fiscal,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDREGIMENFISCAL",
    )
    IdUsoCDFI = models.ForeignKey(
        c_uso_cdfi, on_delete=models.CASCADE, null=True, db_column="IDUSOCDFI"
    )

    def __str__(self):
        return self.RFC


class persona_fisica(models.Model):
    """Persona física

    Returns:
        int: Identificador de la persona física
    """

    IdPersonaFisica = models.IntegerField(
        primary_key=True,
        unique=True,
        serialize=True,
        db_index=True,
        db_column="IDPERSONAFISICA",
    )
    CURP = models.CharField(
        max_length=20,
        unique=True,
        help_text="Clave única de registro de población",
        db_index=True,
        db_column="CURP",
    )
    RFC = models.CharField(
        max_length=15,
        unique=True,
        help_text="Registro Federal de Contribuyente",
        db_index=True,
        db_column="RFC",
    )
    CURPVerificado = models.BooleanField(
        default=False, help_text="CURP verificado", db_column="CURPVERIFICADO"
    )
    RFCVerificado = models.BooleanField(
        default=False, help_text="RFC verificado", db_column="RFCVERIFICADO"
    )
    Nombre = models.CharField(
        max_length=100, help_text="Nombre(s)", db_index=True, db_column="NOMPAIS"
    )
    PrimerApellido = models.CharField(
        max_length=100,
        help_text="Primer apellido (paterno)",
        db_index=True,
        db_column="APELLIDO1",
    )
    SegundoApellido = models.CharField(
        max_length=100,
        help_text="Segundo apellido (materno)",
        db_index=True,
        db_column="APELLIDO2",
    )
    EstadoCivil = models.PositiveSmallIntegerField(
        choices=Const.ESTADO_CIVIL,
        help_text="Estado civil",
        default=0,
        db_column="ESTADOCIVIL",
    )
    FechaNacimiento = models.DateField(
        help_text="Fecha de nacimiento", db_column="FECHANACIMIENTO"
    )
    RegimenMatrimonio = models.PositiveSmallIntegerField(
        choices=Const.REGIMEN_MATRIMONIAL,
        help_text="Regimen del matrimonio",
        default=0,
        db_column="REGMATRIMONIAL",
    )
    NumeroDocumentoIdentidad = models.CharField(
        max_length=50,
        help_text="Número del documento de identidad",
        db_column="NUMDOCIDENTIDAD",
    )
    TelefonoContacto = models.CharField(
        max_length=15, help_text="Teléfono de contacto", db_column="TELCONTACTO"
    )
    Email = models.EmailField(help_text="Correo electrónico", db_column="CORREO")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")

    TipoDocumentoIdentidad = models.ForeignKey(
        c_tipo_documento_identidad, on_delete=models.CASCADE, db_column="IDDOCIDENTIDAD"
    )
    P1ais = models.ForeignKey(c_pais, on_delete=models.CASCADE, db_column="CVEPAIS")

    def __str__(self):
        return self.CURP


class persona_moral(models.Model):
    IdPersonaMoral = models.IntegerField(
        primary_key=True, serialize=True, unique=True, db_column="IDPERSONAMORAL"
    )
    RFC = models.CharField(max_length=15, unique=True, db_index=True, db_column="RFC")
    RFCVerificado = models.BooleanField(default=False, db_column="REFVERIFICADO")
    RazonSocial = models.CharField(
        max_length=100, unique=True, db_index=True, db_column="RAZONSOCIAL"
    )
    FechaConstitucion = models.DateField(db_column="FECHACONTITUCION")
    EntidadExtranjero = models.CharField(max_length=50, db_column="ENTIDADEXTRAJERO")
    DatosAdicionales = models.JSONField(db_column="DATPSADICIONAL")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FECHAMODIF")

    Pais = models.ForeignKey(c_pais, on_delete=models.CASCADE, db_column="CVEPAIS")

    def __str__(self):
        return self.RFC


class propietario(models.Model):
    """Propietario

    Returns:
        int: Identificador del propietario
    """

    IdPropietario = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDPROPIETARIO",
    )
    PersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.CASCADE, db_column="IDPERSONAFISICA", null=True
    )
    PersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, db_column="IDPERSONAMORAL", null=True
    )
    Tipo = models.PositiveSmallIntegerField(
        choices=Const.TIPO_PERSONA, db_column="TIPOPERSONA", db_default=0
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    def __str__(self):
        return self.IdPropietario


class folio_no_inmobiliario(models.Model):
    FolioReal = models.CharField(
        max_length=40, primary_key=True, db_index=True, null=False, db_column="FOLIO"
    )
    FolioProdCancelacion = models.CharField(
        max_length=40, null=True, db_column="FOLIOCAN"
    )
    FolioActoProdCancelacion = models.CharField(
        max_length=40, null=True, db_column="FOLIOACTOCAN"
    )
    Nombre = models.CharField(
        max_length=100, null=False, db_index=True, db_column="NOMBRE"
    )
    Descripcion = models.TextField(db_column="DESCRIPPCION")
    Objeto = models.TextField(null=False, db_column="OBJETO")
    FHCancelacion = models.DateTimeField(db_column="FHCANCELACION")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    def __str__(self):
        return self.FolioReal


class folio_inmobiliario(models.Model):
    """Folio (carátula) del inmueble

    Returns:
        str: Folio real inmobiliario
    """

    FolioReal = models.CharField(
        max_length=40,
        primary_key=True,
        db_index=True,
        null=False,
        db_column="FOLIO",
        verbose_name="Folio real inmobiliario",
    )
    FolioProdCancelacion = models.CharField(
        max_length=40,
        null=True,
        db_column="FOLIOCAN",
        verbose_name="Folio que genera su cancelación",
    )
    FolioActoProdCancelacion = models.CharField(
        max_length=40,
        null=True,
        db_column="FOLIOACTOCAN",
        verbose_name="Folio cancelado producto del actual",
    )

    FolioMatriz = models.CharField(
        max_length=40, null=True, db_column="FOLIOMATRIZ", verbose_name="Folio matriz"
    )
    FolioCondominio = models.CharField(
        max_length=40,
        null=True,
        db_column="FOLIOCONDOMINIO",
        verbose_name="Folio del condominio al que pertenece",
    )
    ClaveCatastral = models.CharField(
        max_length=40,
        null=True,
        db_column="CVECATASTRAL",
        verbose_name="Clave catastral del inmueble",
    )
    FolioCancelado = models.BooleanField(
        default=False,
        db_column="FOLIOCANCELADO",
        verbose_name="Estatus del folio (verdadero=cancelado)",
    )
    FHCancelacion = models.DateTimeField(
        db_column="FHCANCELACION", verbose_name="Fecha y hora dela cancelación"
    )
    NombreInmueble = models.CharField(
        max_length=100,
        null=True,
        db_column="NOMBREINMUEBLE",
        db_index=True,
        verbose_name="Nombre del inmueble",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION", null=True, verbose_name="Descripción del inmueble"
    )
    Observaciones = models.TextField(
        db_column="OBSERVACIONES",
        null=True,
        verbose_name="Obervaciones al instrumento y/o inmueble",
    )
    EsCondominio = models.BooleanField(
        default=False,
        db_column="ESCONDOMINIO",
        verbose_name="Verdadero si es un folio de condominio",
    )
    EsFolioMatriz = models.BooleanField(
        default=False,
        db_column="ESFOLIOMATRIZ",
        verbose_name="Verdadero si es folio matriz",
    )
    SuperficieIndiviso = models.FloatField(
        default=0.00,
        db_column="SUPERFICIEINDIVISO",
        verbose_name="Superficie de indiviso",
    )
    SuperficieSuelo = models.FloatField(
        default=0.00,
        null=False,
        db_column="SUPERFICIESUELO",
        verbose_name="Superficie del suelo",
    )
    SuperficieConstruccion = models.FloatField(
        default=0.00,
        null=True,
        db_column="SUPERFICIECONSTRUCCION",
        verbose_name="Superficie total de los elementos constructivos",
    )
    Ambito = models.PositiveSmallIntegerField(
        default=0,
        choices=Const.AMBITO,
        db_column="AMBITO",
        verbose_name="Ámbito (urbano, rural, etc.)",
    )
    CuadroConstruccion = models.JSONField(
        db_column="CUADROCONSTRUCCION",
        null=True,
        verbose_name="Cuatro de construcción (coordenadas de los vértices)",
    )
    MetodoInmatriculacion = models.PositiveSmallIntegerField(
        db_default=0,
        choices=Const.METODO_INMATRICULACION,
        db_column="METODOINMAT",
        verbose_name="Vía de inmatriculación",
    )
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES", null=True, verbose_name="Datos adicionales"
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        db_default=now(),
        null=False,
        verbose_name="Fecha y hora de alta del registro",
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        null=True,
        verbose_name="Fecha y hora  de la última modificación",
    )

    Vialidad = models.CharField(
        max_length=100,
        db_index=True,
        null=False,
        db_default="",
        db_column="VIALIDAD",
        verbose_name="Vialidad",
    )
    TipoVialidad = models.PositiveSmallIntegerField(
        choices=Const.TIPO_VIALIDAD,
        db_default=0,
        db_column="TIPOVIALIDAD",
        verbose_name="Tipo de vialidad",
    )
    NumeroExterior = models.CharField(
        max_length=10,
        db_index=True,
        db_column="NUMEXTERIOR",
        null=True,
        verbose_name="Número exterior / km / manzana",
    )
    TipoNumeracion = models.SmallIntegerField(
        choices=Const.TIPO_NUMERACION_INMUEBLE,
        db_default=0,
        db_column="TIPONUMERACION",
        null=False,
        verbose_name="Tipo de numeración exterior",
    )
    NumeroInterior = models.CharField(
        max_length=10,
        db_column="NUMINTERIOR",
        null=True,
        verbose_name="Número interior / departamento / lote",
    )
    AliasAsentamiento = models.CharField(
        max_length=50,
        db_column="ASENTAMIENTO",
        null=True,
        verbose_name="Alias asentamiento",
    )
    Logitud = models.FloatField(
        default=0.0, db_column="LON", verbose_name="Longitud (coordenadas geográficas)"
    )
    Latitud = models.FloatField(
        default=0.0, db_column="LAT", verbose_name="Latitud (coordenadas geográficas)"
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        db_default=now(),
        verbose_name="Fecha y hora alta del registro",
    )
    UltimoValorInmueble = models.FloatField(
        db_default=0.0,
        db_column="ULTIMOVALOR",
        verbose_name="Valor del inmueble de la última avalúo",
    )
    FUltimoValor = models.DateField(
        db_column="FULTIMOVALOR", null=True, verbose_name="Fecha del último avalúo"
    )

    IdUsoInmueble = models.ForeignKey(
        c_uso_inmueble,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDUSOINMUEBLE",
        verbose_name="Uso del inmueble",
    )
    ClaveGeoAsentamiento = models.ForeignKey(
        c_asentamiento_humano,
        on_delete=models.CASCADE,
        null=True,
        db_column="CLAVEASENTAMIENTO",
        verbose_name="Asentamiento",
    )

    class Meta:
        verbose_name_plural = "Entidad de folios inmobiliarios (INMUEBLES)"
        ordering = ("FolioReal",)

    def __str__(self):
        return self.Folio


class representacion_legal(models.Model):
    """Representaciones legales

    Returns:
        int: Identificador de la representación
    """

    IdRepresentacion = models.BigAutoField(
        primary_key=True, null=False, db_index=True, db_column="IDREPRESENTACION"
    )
    Activo = models.BooleanField(db_default=False, db_column="ACTIVO")
    RepresentaA = models.PositiveSmallIntegerField(
        choices=Const.TIPO_PERSONA, db_column="REPRESENTA"
    )
    FRepresentacion = models.DateField(db_column="FREPRESENTACION")
    FConclusionRepresentacion = models.DateField(db_column="FCONCREPRESENTACION")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")
    NombreRepresentante = models.CharField(
        max_length=100, null=False, db_column="NOMBREREP"
    )
    PrimerApellidoRepresentante = models.CharField(
        max_length=100, null=False, db_column="APELLIDO1REP"
    )
    SegundoApellidoRepresentante = models.CharField(
        max_length=100, null=False, db_column="APELLIDO2REP"
    )

    IdPersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.CASCADE, null=True, db_column="IDPERSONAFISICA"
    )
    IdPersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, null=True, db_column="IDPERSONAMORAL"
    )

    def __str__(self):
        return self.IdRepresentacion


class construccion(models.Model):
    """Tabla de elementos constructivos

    Nota: Asociado a folio_inmueble

    Returns:
        int: Identificador del elemento constructivo
    """

    IdElementoConstructivo = models.BigAutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="IDELEMENTOCONST",
    )
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    Descripcion = models.TextField(db_column="DESCRIPCION")
    Superficie = models.FloatField(db_default=0.00, null=False, db_column="SUPERFICIE")
    Niveles = models.IntegerField(default=0, db_column="NIVELES")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    FolioReal = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )
    idTipoConstruccion = models.ForeignKey(
        c_tipo_construccion,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPOCONST",
    )

    def __str__(self):
        return self.IdElementoConstructivo


class colindancia(models.Model):
    """Tabla de colindancias

    Nota: Se relaciona con folio_inmueble

    Returns:
        int: Identificación de la colindancia
    """

    IdColindancia = models.BigAutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="IDCOLINDANCIA",
    )
    NombreColindante = models.CharField(
        max_length=100, null=False, db_column="NOMCOLINDANTE"
    )
    DescripcionColindante = models.TextField(db_column="DESCCOLINDANTE")
    Lado = models.PositiveSmallIntegerField(
        null=False, db_default=0, choices=Const.LADO, db_column="LADO"
    )
    LongitudColindancia = models.FloatField(
        db_default=0.00, db_column="LONGCOLINDANCIA"
    )
    Rumbo = models.FloatField(db_default=0.00, db_column="RUMBO")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    FolioReal = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )

    def __str__(self):
        return self.IdColindancia


class plantilla_reporte(models.Model):
    idPlantillaReporte = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDPLANTILLAREP",
    )
    Nombre = models.CharField(
        max_length=100, null=False, unique=True, db_column="NOMBRE"
    )
    Descripcion = models.TimeField(db_column="DESCRIPCION")
    ArchivoPlantilla = models.CharField(max_length=250, db_column="PLANTILLA")
    Version = models.IntegerField(db_default=0, db_column="VERSION")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")


class reporte(models.Model):
    """Reportes

    Returns:
        str: Nombre
    """

    idReporte = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDREPORTE"
    )
    Nombre = models.CharField(
        max_length=100, null=False, unique=True, db_column="NOMBRE"
    )
    Descripcion = models.TimeField(db_column="DESCRIPCION")
    Contenido = models.JSONField(db_column="CONTENIDO")
    Impreso = models.BooleanField(db_column="IMPRESO")
    FHImpresion = models.DateTimeField(db_column="FHIMPRESION")
    Guardado = models.BooleanField(db_column="GUARDADO")
    FHGuardado = models.DateTimeField(db_column="FHGUARDADO")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdClaseReporte = models.ForeignKey(
        c_clase_reporte, on_delete=models.CASCADE, null=True, db_column="IDCLASEREPORTE"
    )
    IdPlantillaReporte = models.ForeignKey(
        plantilla_reporte, models.CASCADE, null=True, db_column="IDPLANTILLAREP"
    )
    IdDocumento = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCUMENTO"
    )

    class Meta:
        ordering = ("Nombre", "Descripcion", "Contenido", "FHImpresion", "FHGuardado")
        verbose_name_plural = "Reportes"

    def __str__(self):
        return f"{self.Nombre}"


class recibo(models.Model):
    """Tabla de control de recbos de pago

    Returns:
        int: Identificador del recibo
    """

    IdRecibo = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDREPORTE"
    )
    Nombre = models.CharField(
        max_length=100, null=False, unique=True, db_column="NOMBRE"
    )
    Descripcion = models.TimeField(db_column="DESCRIPCION")
    Contenido = models.JSONField(db_column="CONTENIDO")
    Impreso = models.BooleanField(db_column="IMPRESO")
    FHImpresion = models.DateTimeField(db_column="FHIMPRESION")
    Guardado = models.BooleanField(db_column="GUARDADO")
    FHGuardado = models.DateTimeField(db_column="FHGUARDADO")
    Pago = models.FloatField(db_default=0.00, db_column="PAGODERECHOS")
    Recibo = models.TextField(db_column="RECIBOPAGO")
    FHPago = models.DateTimeField(db_column="FHPAGO")
    MetodoPago = models.PositiveSmallIntegerField(
        choices=Const.METODO_PAGO, db_default=0, db_column="METODOPAGO"
    )
    PorcentajeSubsidio = models.FloatField(db_default=0.00, db_column="PORCSUBSIDIO")
    MotivoSubsidio = models.TextField(db_column="MOTIVOSUBSIDIO")
    ConfirmacionPago = models.BooleanField(
        db_default=False, db_column="CONFIRMACIONPAGO"
    )
    CadenaConfirmacion = models.TextField(db_column="CADENACONFIRMACION")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdClaseReporte = models.ForeignKey(
        c_clase_reporte, on_delete=models.CASCADE, null=True, db_column="IDCLASEREPORTE"
    )
    IdPlantillaReporte = models.ForeignKey(
        plantilla_reporte, models.CASCADE, null=True, db_column="IDPLANTILLAREP"
    )
    IdDocumento = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCUMENTO"
    )

    def __str__(self):
        return self.idRecibo


class constancia(models.Model):
    IdConstancia = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDREPORTE"
    )
    Nombre = models.CharField(
        max_length=100, null=False, unique=True, db_column="NOMBRE"
    )
    Descripcion = models.TimeField(db_column="DESCRIPCION")
    Contenido = models.JSONField(db_column="CONTENIDO")
    Impreso = models.BooleanField(db_column="IMPRESO")
    FHImpresion = models.DateTimeField(db_column="FHIMPRESION")
    Guardado = models.BooleanField(db_column="GUARDADO")
    FHGuardado = models.DateTimeField(db_column="FHGUARDADO")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")
    Firmada = models.BooleanField(db_default=False, db_column="FIRMADA")
    FHElaboracion = models.DateTimeField(db_column="FHELABORACION")
    FHFirma = models.DateTimeField(db_column="FHFIRMA")

    IdUsuarioElaboro = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )
    Autorizacion = models.ForeignKey(
        autorizacion, on_delete=models.CASCADE, null=True, db_column="AUTORIZAICON"
    )

    IdPlantillaReporte = models.ForeignKey(
        plantilla_reporte, models.CASCADE, null=True, db_column="IDPLANTILLAREP"
    )
    IdDocumento = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCUMENTO"
    )

    def __str__(self):
        return self.IdConstancia


class certificado(models.Model):
    IdCertificado = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDREPORTE"
    )
    Nombre = models.CharField(
        max_length=100, null=False, unique=True, db_column="NOMBRE"
    )
    Descripcion = models.TimeField(db_column="DESCRIPCION")
    Contenido = models.JSONField(db_column="CONTENIDO")
    Impreso = models.BooleanField(db_column="IMPRESO")
    FHImpresion = models.DateTimeField(db_column="FHIMPRESION")
    Guardado = models.BooleanField(db_column="GUARDADO")
    FHGuardado = models.DateTimeField(db_column="FHGUARDADO")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")
    Firmada = models.BooleanField(db_default=False, db_column="FIRMADA")
    FHElaboracion = models.DateTimeField(db_column="FHELABORACION")
    FHFirma = models.DateTimeField(db_column="FHFIRMA")

    IdUsuarioElaboro = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )
    Autorizacion = models.ForeignKey(
        autorizacion, on_delete=models.CASCADE, null=True, db_column="AUTORIZAICON"
    )
    IdPlantillaReporte = models.ForeignKey(
        plantilla_reporte, models.CASCADE, null=True, db_column="IDPLANTILLAREP"
    )
    IdDocumento = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCUMENTO"
    )

    def __str__(self):
        return self.IdCertificado


class indice_libro(models.Model):
    IdLibro = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDLIBRO"
    )
    Libro = models.CharField(max_length=50, null=False, unique=True, db_column="LIBRO")
    Ubicacion = models.CharField(max_length=100, null=True, db_column="UBICACION")
    Disponible = models.BooleanField(db_default=False, db_column="DISPONIBLE")
    Estante = models.IntegerField(db_column="ESTANTE")
    Fila = models.IntegerField(db_column="FILA")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")

    def __str__(self):
        return self.IdLibro


class indice_registro(models.Model):
    IdRegistro = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDREGISTRO"
    )
    Registro = models.CharField(max_length=20, null=False, db_column="REGISTRO")
    RegistroBis = models.BooleanField(db_default=False, db_column="REGISTROBIS")
    ActoContenido = models.TextField(db_column="ACTO")
    FInscripcion = models.DateField(db_column="FINSCRIPCION")
    Titulares = models.JSONField(db_column="TITULARES")
    FTransicion = models.DateField(db_column="FTRANSICION")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")

    IdLibro = models.ForeignKey(
        indice_libro, on_delete=models.CASCADE, db_column="IDLIBRO"
    )

    def __str__(self):
        return self.IdRegistro


class acervo_historico(models.Model):
    IdActoAcervo = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDACTOACERVO",
    )
    Orden = models.IntegerField(db_default=0, db_column="ORDEN")

    FolioReal = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )
    IdRegistro = models.ForeignKey(
        indice_registro, on_delete=models.CASCADE, null=True, db_column="IDREGISTRO"
    )

    def __str__(self):
        return self.IdActoAcervo


class c_clase_acto(models.Model):
    """Catálogo de clases de actos

    Returns:
        int: Identificador de la clase de acto
    """

    IdClaseActo = models.SmallAutoField(
        primary_key=True,
        null=False,
        db_column="IDCLASEACTO",
        db_index=True,
        db_comment="Identificador de la clase de acto",
    )
    Nombre = models.CharField(
        max_length=50,
        db_column="NOMBRE",
        db_index=True,
        null=False,
        db_comment="Nombre de la clase de acto",
    )
    Descripcion = models.TextField(
        null=True, db_column="DESCRIPCION", db_comment="Descripción"
    )
    Limitativo = models.BooleanField(
        db_default=False,
        db_column="LIMITATIVA",
        db_comment="Clase de actos limitativos al dominio",
    )
    Modificatoria = models.BooleanField(
        db_default=False,
        db_column="MODIFICATORIA",
        db_comment="Clase de actos modifican el carátula/inmueble",
    )
    Traslativo = models.BooleanField(
        db_default=False,
        db_column="TRASLATIVO",
        db_comment="Clase de acto modifica dominio",
    )
    Judicial = models.BooleanField(
        db_default=False, db_column="JUDICIAL", db_comment="Clase de acto judicial"
    )
    Administrativo = models.BooleanField(
        db_default=False,
        db_column="ADMINISTRATIVO",
        db_comment="Clase de acto administrativo",
    )
    Aviso = models.BooleanField(
        db_default=False, db_column="AVISO", db_comment="Clase de acto de aviso"
    )
    Vigente = models.BooleanField(
        db_default=False, null=False, db_comment="Vigencia", db_column="Vigencia"
    )
    FHAlta = models.DateTimeField(db_column="FHALTA", db_comment="Fecha y hora de alta")
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF", db_comment="Fecha y hora de modificación"
    )

    class Meta:
        ordering = (
            "Nombre",
            "IdClaseActo",
        )
        verbose_name_plural = "Catálogo de clases de actos"

    def __str__(self):
        return self.IdClaseActo


class c_tipo_acto_inmobiliario(models.Model):
    """Catálogo de tipo de acto inmobiliario

    Returns:
        int: Identificador del tipo de acto.
    """

    IdTipoActo = models.SmallAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDTIPOACTO",
        db_comment="Identificador único",
    )
    Nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        db_column="NOMBRE",
        db_comment="Nombre del acto",
    )
    Descripcion = models.TextField(
        null=True, db_column="DESCRIPCION", db_comment="Descripción"
    )

    Tabla = models.CharField(
        max_length=50, db_index=True, db_column="TABLA", db_comment="Tabla"
    )
    Llave = models.CharField(
        max_length=50, db_column="LLAVEPRIMARIA", db_comment="Llave primaria"
    )

    TipoCampoLlave = models.SmallIntegerField(
        choices=Const.TIPO_CAMPO,
        db_default=0,
        db_column="TIPOCAMPO",
        db_comment="Tipo de campo",
    )

    Vigente = models.BooleanField(
        db_default=False, null=False, db_comment="Vigencia", db_column="Vigencia"
    )
    FHAlta = models.DateTimeField(db_column="FHALTA", db_comment="Fecha y hora de alta")
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF", db_comment="Fecha y hora de modificación"
    )

    ClaseActo = models.ForeignKey(
        c_clase_acto,
        on_delete=models.CASCADE,
        db_column="CLASEACTO",
        db_comment="Clase de acto",
        null=True,
    )

    class Meta:
        ordering = (
            "Nombre",
            "IdTipoActo",
            "Tabla",
            "Llave",
        )
        verbose_name_plural = "Catálogo tipos de actos"

    def __str__(self):
        return self.IdTipoActo


class c_tipo_acto_no_inmobiliario(models.Model):
    """Catálogo de tipo de acto no inmobiliario

    Returns:
        int: Identificador del tipo de acto.
    """

    IdTipoActo = models.SmallAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDTIPOACTO",
        db_comment="Identificador único",
    )
    Nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        db_column="NOMBRE",
        db_comment="Nombre del acto",
    )
    Descripcion = models.TextField(
        null=True, db_column="DESCRIPCION", db_comment="Descripción"
    )

    Tabla = models.CharField(
        max_length=50, db_index=True, db_column="TABLA", db_comment="Tabla"
    )
    Llave = models.CharField(
        max_length=50, db_column="LLAVEPRIMARIA", db_comment="Llave primaria"
    )

    TipoCampoLlave = models.SmallIntegerField(
        choices=Const.TIPO_CAMPO,
        db_default=0,
        db_column="TIPOCAMPO",
        db_comment="Tipo de campo",
    )

    Vigente = models.BooleanField(
        db_default=False, null=False, db_comment="Vigencia", db_column="Vigencia"
    )
    FHAlta = models.DateTimeField(db_column="FHALTA", db_comment="Fecha y hora de alta")
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF", db_comment="Fecha y hora de modificación"
    )

    ClaseActo = models.ForeignKey(
        c_clase_acto,
        on_delete=models.CASCADE,
        db_column="CLASEACTO",
        db_comment="Clase de acto",
        null=True,
    )

    class Meta:
        ordering = (
            "Nombre",
            "IdTipoActo",
            "Tabla",
            "Llave",
        )
        verbose_name_plural = "Catálogo tipos de actos"

    def __str__(self):
        return self.IdTipoActo


class acto_inmobiliario(models.Model):
    """Tabla de actos inmobiliarios

    Returns:
        str: Folio correspondiente al acto
    """

    FolioActo = models.CharField(
        primary_key=True,
        unique=True,
        null=False,
        max_length=40,
        db_index=True,
        db_column="FOLIOACTO",
        db_comment="Folio del acto",
    )

    ActoHistorico = models.BooleanField(
        db_default=False, db_column="ACTOHISTORICO", db_comment="Acto histórico"
    )
    FHInscripcion = models.DateTimeField(
        db_column="FHINSCRIPCION", db_comment="Fecha y hora de la inscripción"
    )
    FHCancelacion = models.DateTimeField(
        db_column="FHCANCELACION", db_comment="Fecha y hora de la cancelación"
    )
    Vigente = models.BooleanField(
        db_default=True, db_column="VIGENTE", db_comment="Vigente"
    )
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES", db_comment="Datos adicionales"
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA", db_comment="Fecha y hora del alta del registro"
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF", db_comment="Fecha y hora de la última modificación"
    )

    FolioReal = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )

    TipoActoInmobiliario = models.ForeignKey(
        c_tipo_acto_inmobiliario,
        on_delete=models.CASCADE,
        null=True,
        db_column="TIPOACTO",
        db_comment="Tipo de acto inmobiliario",
    )

    def __str__(self):
        return self.FolioActo


class r_acto_instrumento(models.Manager):
    """Tabla de relación actos e instrumentos

    Nota: Un acto puede contar con varios instrumentos legale y
    viceversa
    """

    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdInstrumento = models.ForeignKey(
        instrumento, on_delete=models.CASCADE, db_column="IDINSTRUMENTO"
    )
    RolInstrumento = models.PositiveSmallIntegerField(
        choices=Const.ROL_INSTRUMENTO, db_default=0, db_column="ROLINSTRUMENTO"
    )


class fiduciario(models.Model):
    """Tabla de fiduciarios

    Returns:
        int: Identificador del fiduciario
    """

    idFiduciario = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDFIDUCIARIO",
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdPersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, null=True, db_column="IDPERSONAMORAL"
    )
    IdRepresentacion = models.ForeignKey(
        representacion_legal,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDREPRESENTACION",
    )

    def __str__(self):
        return self.idFiduciario


class fiduciante(models.Model):
    """Tabla de fiduciantes

    Returns:
        int: Identificador del fiduciante
    """

    IdFiduciante = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDFIDUCIANTE",
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    # SI TipoPersona = 0 debe verificarse IdPersonaFisica y si es 2  entonces IdPersonaMoral
    TipoPersona = models.PositiveSmallIntegerField(
        choices=Const.TIPO_PERSONA, db_default=0, db_column="TIPOPERSONA"
    )

    IdPersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.CASCADE, null=True, db_column="IDPERSONAFISICA"
    )
    IdPersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, null=True, db_column="IDPERSONAMORAL"
    )

    def __str__(self):
        return self.IdFiduciante


class fideicomiso(models.Model):
    """Tabla de fideicomisos

    Returns:
        int: Identificador del fideicomiso
    """

    IdFideicomiso = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDFIDEICOMISO",
    )
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    Descripcion = models.TextField(db_column="DESCRIPCION")
    Objeto = models.TextField(db_column="OBJETO")
    Contraprestaciones = models.TimeField(db_column="CONTRAPRESTACIONES")
    FInicio = models.DateField(db_column="FINICIO")
    FConclusion = models.DateField(db_column="FCONCLUSION")

    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdFiduciario = models.ForeignKey(
        fiduciario, on_delete=models.CASCADE, null=True, db_column="IDFIDUCIARIO"
    )
    IdFiduciante = models.ForeignKey(
        fiduciante, on_delete=models.CASCADE, null=True, db_column="FIDUCIANTE"
    )

    def __str__(self):
        return self.IdFideicomiso


class partcipante(models.Model):
    IdParte = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDPARTICIPANTE",
    )
    Porcentaje = models.FloatField(db_default=0.0, db_column="PORCENTAJE")
    RolEnElActo = models.PositiveSmallIntegerField(
        choices=Const.ROL_PARTICIPANTE, db_default=0, null=False, db_column="ROL"
    )
    TipoPersona = models.PositiveSmallIntegerField(
        choices=Const.TIPO_PERSONA, db_default=0, null=True, db_column="TIPOPERSONA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdPersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.CASCADE, null=True, db_column="IDPERSONAFISICA"
    )
    IdPersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, null=True, db_column="IDPERSONAMORAL"
    )
    IdRepresentacion = models.ForeignKey(
        representacion_legal,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDREPRESENTACION",
    )

    def __str__(self):
        return self.IdParte


class inmatriculacion_folio_inmobiliario(models.Model):

    IdInmatriculacion = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDINMATRICULACION",
    )
    Tipo = models.IntegerField(
        choices=Const.TIPO_INMATRICULACION, db_default=0, db_column="TIPO"
    )
    FHCreacionFolio = models.DateTimeField(db_column="FHCREACIONFOLIO")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdRegistro = models.ForeignKey(
        indice_registro, on_delete=models.CASCADE, null=True, db_column="IDREGISTRO"
    )
    FolioRealNuevo = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )

    def __str__(self):
        return self.IdInmatriculacion


class r_inm_folio_inmob_usuario(models.Model):

    Rol = models.PositiveSmallIntegerField(
        choices=Const.ROL_USUARIO_FOLIO_INMOBILIARIO, db_default=0, db_column="ROL"
    )

    IdInmatriculacion = models.ForeignKey(
        inmatriculacion_folio_inmobiliario,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDINMATRICULACION",
    )
    IdUsuario = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )


class traslado_dominio(models.Model):

    IdTrasladoDominio = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDTRASLADO"
    )
    ValorTransaccion = models.FloatField(db_default=0.0, db_column="VALORTRANSACCION")
    ImpuestoPagado = models.FloatField(db_default=0.0, db_column="IMPUESTOPAGADO")
    ReferenciaPago = models.CharField(max_length=100, db_column="REFPAGOIMPUESTO")
    Excencion = models.FloatField(db_default=0.0, db_column="EXCENCION")
    MotivoExcencion = models.TextField(db_column="MOTIVOEXCENCION")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    TipoCambio = models.FloatField(db_default=1.0, db_column="TIPOCAMBIO")
    CveMoneda = models.ForeignKey(
        c_moneda, on_delete=models.CASCADE, null=True, db_column="CVEMONEDA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdFideicomiso = models.ForeignKey(
        fideicomiso, on_delete=models.CASCADE, null=True, db_column="IDFIDEICOMISO"
    )

    def __str__(self):
        return self.IdTrasladoDominio


class fusion(models.Model):
    IdFusion = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDFUSION"
    )
    Superficie = models.FloatField(db_default=0.0, null=False, db_column="SUPERFICIE")
    SuperficieConstruccion = models.FloatField(
        db_default=0.0, null=False, db_column="SUPERFICIECONST"
    )
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdFusion


class r_inmueble_fusion(models.Model):

    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdFusion = models.ForeignKey(
        fusion, on_delete=models.CASCADE, null=True, db_column="IDFUSION"
    )
    FolioRealFusionado = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )


class fraccionamiento(models.Model):
    IdFraccionamiento = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDFRACCIONAMIENTO",
    )
    Nombre = models.CharField(max_length=100, null=True)
    Superficie = models.FloatField(db_default=0.0, null=False, db_column="SUPERFICIE")
    SuperficieConstruccion = models.FloatField(
        db_default=0.0, null=False, db_column="SUPERFICIECONST"
    )
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    FolioMatriz = models.ForeignKey(
        folio_inmobiliario, models.CASCADE, null=True, db_column="FOLIOMATRIZ"
    )
    IdDocumentoAutorizacion = models.ForeignKey(
        documento, models.CASCADE, null=True, db_column="IDDOCAUTORIZACION"
    )
    IdInmatriculacion = models.ForeignKey(
        inmatriculacion_folio_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="IDINMATRICULACION",
    )

    def __str__(self):
        return self.IdFraccionamiento


class fraccion(models.Model):

    IdFraccion = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDFRACCION"
    )
    Superficie = models.FloatField(db_default=0.0, null=False, db_column="SUPERFICIE")
    SuperficieConstruccion = models.FloatField(
        db_default=0.0, null=False, db_column="SUPERFICIECONST"
    )
    IdInmatriculacion = models.ForeignKey(
        inmatriculacion_folio_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="IDINMATRICULACION",
    )

    def __str__(self):
        return self.IdFraccion


class subdivision(models.Model):
    IdSubdivision = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDFRACCIONAMIENTO",
    )
    Superficie = models.FloatField(db_default=0.0, null=False, db_column="SUPERFICIE")
    SuperficieConstruccion = models.FloatField(
        db_default=0.0, null=False, db_column="SUPERFICIECONST"
    )
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    FolioMatriz = models.ForeignKey(
        folio_inmobiliario, models.CASCADE, null=True, db_column="FOLIOMATRIZ"
    )
    IdDocumentoAutorizacion = models.ForeignKey(
        documento, models.CASCADE, null=True, db_column="IDDOCAUTORIZACION"
    )
    IdInmatriculacion = models.ForeignKey(
        inmatriculacion_folio_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="IDINMATRICULACION",
    )

    def __str__(self):
        return self.IdSubdivision


class condominio(models.Model):
    IdCondominio = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDCONDOMINIO",
    )
    Nombre = models.CharField(max_length=100, null=True)
    SuperficieComun = models.FloatField(
        db_default=0.0, null=False, db_column="SUPERFICIECOMUN"
    )
    SuperficieConstConstruccion = models.FloatField(
        db_default=0.0, null=False, db_column="SUPERFONSTCOMUN"
    )
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdDocumentoAutorizacion = models.ForeignKey(
        documento, models.CASCADE, null=True, db_column="IDDOCAUTORIZACION"
    )

    def __str__(self):
        return self.IdCondominio


class gravamen(models.Model):

    IdGravamen = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDGRAVAMEN"
    )
    TipoCambio = models.FloatField(db_default=1.0, null=False, db_column="TIPOCAMBIO")
    FInicioVigencia = models.DateField(db_column="FINICIO")
    Plazo = models.IntegerField(db_default=0, db_column="PLAZO")
    EscalaPlazo = models.PositiveSmallIntegerField(
        choices=Const.ESCALA_TIEMPO, db_default=0, db_column="ESCALAPLAZO"
    )
    Monto = models.FloatField(db_default=0.0, db_column="MONTO")
    TasaInteres = models.FloatField(db_default=0.0, db_column="TASAINTERES")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    CveMoneda = models.ForeignKey(
        c_moneda, on_delete=models.CASCADE, null=True, db_column="CVEMONEDA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdGravamen


class cesion(models.Model):
    IdCesion = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDCESION"
    )
    FInicioVigencia = models.DateField(db_column="FINICIO")
    Monto = models.FloatField(db_default=0.0, db_column="MONTO")
    Motivos = models.TextField(db_column="MOTIVOS")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    TipoCambio = models.FloatField(db_default=1.0, null=False, db_column="TIPOCAMBIO")
    IdGravamen = models.ForeignKey(
        gravamen, models.CASCADE, null=True, db_column="IDGRAVAMEN"
    )
    CveMoneda = models.ForeignKey(
        c_moneda, on_delete=models.CASCADE, null=True, db_column="CVEMONEDA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdCesion


class reserva_dominio(models.Model):
    IdReservaDominio = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDRESERVA"
    )
    FInicioVigencia = models.DateField(db_column="FINICIO")
    FConclusionVigencia = models.DateField(db_column="FCONCLUSION")
    Monto = models.FloatField(db_default=0.0, db_column="MONTO")
    Motivos = models.TextField(db_column="MOTIVOS")
    TasaInteres = models.FloatField(db_default=0.0, db_column="TASAINTERES")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    TipoCambio = models.FloatField(db_default=1.0, null=False, db_column="TIPOCAMBIO")
    IdGravamen = models.ForeignKey(
        gravamen, models.CASCADE, null=True, db_column="IDGRAVAMEN"
    )
    CveMoneda = models.ForeignKey(
        c_moneda, on_delete=models.CASCADE, null=True, db_column="CVEMONEDA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdReservaDominio


class usufructo(models.Model):
    IdUsufructo = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDUSUFRUCTO",
    )

    Vitalicio = models.BooleanField(db_default=False, db_column="VITALICIO")
    FInicio = models.DateField(db_column="FINICIO")
    FConclusion = models.DateField(db_column="FCONCLUSION")
    Condiciones = models.TextField(null=False, db_column="CONDICIONES")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdUsufructo


class usufructuario(models.Model):
    IdUsufructuario = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDUSUFRUCTUARIO",
    )
    Porcentaje = models.FloatField(db_default=0.0, db_column="PORCENTAJE")

    IdPersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.CASCADE, null=True, db_column="IDPERSONAFISICA"
    )
    IdPersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, null=True, db_column="IDPERSONAMORAL"
    )
    IdRepresentacion = models.ForeignKey(
        representacion_legal,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDREPRESENTANTE",
    )

    IdUsufructo = models.ForeignKey(
        usufructo, on_delete=models.CASCADE, null=True, db_column="IDUSUFRUCTO"
    )

    def __str__(self):
        return self.IdUsufructuario


class demandante(models.Model):
    idDemandante = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDDEMANDANTE",
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdPersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.CASCADE, null=True, db_column="IDPERSONAFISICA"
    )
    IdPersonaMoral = models.ForeignKey(
        persona_moral, on_delete=models.CASCADE, null=True, db_column="IDPERSONAMORAL"
    )
    IdRepresentacion = models.ForeignKey(
        representacion_legal,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDREPRESENTANTE",
    )

    def __str__(self):
        return self.idDemandante


class c_tipo_sentencia(models.Model):
    idTipoSentencia = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDTIPOSENTENCIA",
    )
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    Descripcion = models.TextField(db_column="DESCRIPCION")

    def __str__(self):
        return self.idTipoSentencia


class sentencia(models.Model):
    IdSentencia = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDSENTENCIA",
    )
    FAuto = models.DateField(db_column="FAUTO")
    FVigencia = models.DateField(db_column="FVIGENCIA")
    Objeto = models.TextField(null=False, db_column="OBJETO")
    Extracto = models.TextField(null=False, db_column="EXTRACTO")
    IdJuzgado = models.ForeignKey(
        fedatario_y_funcionario,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDJUZGADO",
    )
    IdDemandante = models.ForeignKey(
        demandante, on_delete=models.CASCADE, null=True, db_column="IDDEMANDANTE"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdTipoSentencia = models.ForeignKey(
        c_tipo_sentencia,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPOSENTENCIA",
    )

    def __str__(self):
        return self.IdSentencia


class c_tipo_embargo(models.Model):
    IdTipoEmbargo = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDTIPOEMBARGO",
    )
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    Descripcion = models.TextField(db_column="DESCRIPCION")

    def __str__(self):
        return self.IdTipoEmbargo


class emabargo(models.Model):
    IdEmbargo = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDEMBARGO"
    )
    FAuto = models.DateField(db_column="FAUTO")
    FVigencia = models.DateField(db_column="FVIGENCIA")
    Objeto = models.TextField(null=False, db_column="OBJETO")
    Extracto = models.TextField(null=False, db_column="EXTRACTO")
    IdJuzgado = models.ForeignKey(
        fedatario_y_funcionario,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDJUZGADO",
    )
    IdDemandante = models.ForeignKey(
        demandante, on_delete=models.CASCADE, null=True, db_column="IDDEMANDANTE"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdTipoEmbargo = models.ForeignKey(
        c_tipo_sentencia,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPOEMBARGO",
    )

    def __str__(self):
        return self.IdEmbargo


class c_tipo_aviso_preventivo(models.Model):
    IdTipoAvisoPreventivo = models.SmallAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDTIPOAVISO",
    )
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    Descripcion = models.TextField(db_column="DESCRIPCION")
    PlazoEnDias = models.PositiveSmallIntegerField(
        db_default=90, db_column="PLAZOVIGENCIA"
    )
    Vence = models.BooleanField(db_default=True, db_column="VENCE")

    def __str__(self):
        return self.IdTipoAvisoPreventivo


class aviso_preventivo(models.Model):
    IdAvisoPreventivo = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDAVISOPREVENTIVO",
    )
    FInicio = models.DateField(db_column="FINICIO")
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )
    IdTipoAviso = models.ForeignKey(
        c_tipo_aviso_preventivo,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPOAVISO",
    )


class contrato_arrendamiento(models.Model):
    """Tabla de contratos de arrendamientos

    Returns:
        int: Identificador del contrato registrado
    """

    IdContrato = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDCONTRATO"
    )
    EscalaPlazo = models.PositiveSmallIntegerField(
        choices=Const.ESCALA_TIEMPO, db_default=0, db_column="ESCALAPLAZO"
    )
    Plazo = models.PositiveSmallIntegerField(db_default=0, db_column="PLAZO")
    TipoCambio = models.FloatField(db_default=1.0, db_column="TIPOCAMBIO")
    Depostivo = models.FloatField(db_default=0.0, db_column="DEPOSITO")
    PagoAnticipado = models.BooleanField(db_default=False, db_column="PAGOANTICIPADO")
    CondicionesGenerales = models.TextField(null=False, db_column="CONDICIONES")

    CveMondeda = models.ForeignKey(
        c_moneda, on_delete=models.CASCADE, null=True, db_column="CVEMONEDA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdContrato


class acto_vario(models.Model):
    """Actos que no están definido en el catálogo de tipos de actos

    Nota: Los abogados se refienen a los actos no "encuadrados" o que
    no se "encuadran" en un tipo ya definido

    Un acto_vario se asocia a un acto_no_inmobiliario, este último
    tiene un folio.

    Returns:
        int: Identificador de la entrada del acto
    """

    IdActoVario = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDACTOVARIO",
    )
    Objeto = models.TextField(null=False, db_column="OBJETO")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    TipoCambio = models.FloatField(db_default=1.0, db_column="TIPOCAMBIO")
    CveMondeda = models.ForeignKey(
        c_moneda, on_delete=models.CASCADE, null=True, db_column="CVEMONEDA"
    )
    FolioActo = models.OneToOneField(
        acto_inmobiliario,
        models.CASCADE,
        null=True,
        db_column="FOLIOACTO",
        verbose_name="Acto",
        help_text="Acto al que corresponde",
    )

    def __str__(self):
        return self.IdActoVario


class acto_no_inmobiliario(models.Model):
    """Tabla de actos no imobiliarios

    Nota: No son parte de los actos asociados a organizaciones mercantiles, civiles, etc.
    No son parte del registro de comercio.

     Returns:
        str: Folio del acto no imboliario
    """

    FolioActo = models.CharField(
        primary_key=True,
        unique=True,
        null=False,
        max_length=40,
        db_index=True,
        db_column="FOLIOACTO",
    )
    ActoHistorico = models.BooleanField(db_default=False, db_column="ACTOHISTORICO")
    FHInscripcion = models.DateTimeField(db_column="FHINSCRIPCION")
    FHCancelacion = models.DateTimeField(db_column="FHCANCELACION")
    Vigente = models.BooleanField(db_default=True, db_column="VIGENTE")
    Objeto = models.TextField(null=False, db_column="OBJETO")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    FolioReal = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )

    def __str__(self):
        return self.FolioActo


class r_acto_no_inm_instrumento(models.Model):
    """Tabla de relación entre los actos y los folios no inmbiliarios (carátulas)"""

    FolioActo = models.ForeignKey(
        acto_no_inmobiliario, on_delete=models.CASCADE, db_column="FOLIOACTO"
    )
    IdInstrumento = models.ForeignKey(
        instrumento, on_delete=models.CASCADE, db_column="IDINSTRUMENTO"
    )
    RolInstrumento = models.PositiveSmallIntegerField(
        choices=Const.ROL_INSTRUMENTO, db_default=0, db_column="ROLINSTRUMENTO"
    )


class lista_negra_folios_inmobiliarios(models.Model):
    """Lista negra de folios inmobiliarios

    Returns:
        str: Folio en la lista negra, causa y fecha y hora de
        la incorporación.
    """

    IdEntrada = models.BigAutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        verbose_name="Identificador único",
        db_column="IDENTRADA",
    )
    FolioReal = models.CharField(
        max_length=40,
        unique=True,
        null=False,
        db_column="FOLIOREAL",
        db_index=True,
        verbose_name="Folio real",
        help_text="Folio real en la lista negra",
    )
    Causa = models.SmallIntegerField(
        choices=Const.CAUSA_LISTA_NEGRA_FOLIO,
        null=False,
        db_column="CAUSA",
        db_default=0,
        verbose_name="Causa",
        help_text="Causa de la incorporación a la lista negra",
    )
    Observaciones = models.TextField(
        db_column="OBSERVACIONES",
        verbose_name="Observaciones",
        help_text="Observaciones",
        null=True,
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        db_default=now(),
        verbose_name="Fecha y hora incorporación",
        help_text="Fecha y hora de la incorporación",
    )
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    class Meta:
        ordering = ("FolioReal", "FHAlta", "Causa")
        verbose_name_plural = "Lista negra de folios inmobiliarios"

    def __str__(self):
        return f"{self.FolioReal}, {self.Causa}, {self.FHAlta}"


class lista_negra_folios_no_inmobiliarios(models.Model):
    """Lista negra de folios no inmobiliarios

    Returns:
        str: Folio en la lista negra, causa y fecha y hora de
        la incorporación.
    """

    IdEntrada = models.BigAutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        verbose_name="Identificador único",
        db_column="IDENTRADA",
    )
    FolioReal = models.CharField(
        max_length=40,
        unique=True,
        null=False,
        db_column="FOLIOREAL",
        db_index=True,
        verbose_name="Folio real",
        help_text="Folio real en la lista negra",
    )
    Causa = models.SmallIntegerField(
        choices=Const.CAUSA_LISTA_NEGRA_FOLIO,
        null=False,
        db_column="CAUSA",
        db_default=0,
        verbose_name="Causa",
        help_text="Causa de la incorporación a la lista negra",
    )
    Observaciones = models.TextField(
        db_column="OBSERVACIONES",
        verbose_name="Observaciones",
        help_text="Observaciones",
        null=True,
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        db_default=now(),
        verbose_name="Fecha y hora incorporación",
        help_text="Fecha y hora de la incorporación",
    )
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    class Meta:
        ordering = ("FolioReal", "FHAlta", "Causa")
        verbose_name_plural = "Lista negra de folios no inmobiliarios"

    def __str__(self):
        return f"{self.FolioReal}, {self.Causa}, {self.FHAlta}"


class control_siger(models.Model):
    """Configuración básica y control

    Returns:
        str: Variable=Valor
    """

    idEntrada = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column="IDENTRADA",
        verbose_name="Identificador único",
    )
    Variable = models.CharField(
        max_length=50,
        null=False,
        db_column="VARIABLE",
        db_default="VAR",
        unique=True,
        db_index=True,
        verbose_name="Variable",
        help_text="Variable",
    )
    Valor = models.CharField(
        max_length=200,
        db_column="VALOR",
        db_default="VAL",
        null=False,
        verbose_name="Valor",
        help_text="Valor",
    )

    class Meta:
        ordering = ("Variable", "Valor")
        verbose_name_plural = "Tabla de control y configuración"

    def __str__(self):
        return f"{self.Variable}={self.Valor}"
