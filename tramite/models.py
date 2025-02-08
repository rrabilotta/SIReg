from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from sireg.contantes import Const
from adminusr.models import usuario, c_area, c_oficina, fedatario_y_funcionario
from catalogo.models import (
    c_asentamiento_humano,
    c_localidad,
    c_tipo_documento_identidad,
)
from registro.models import (
    acto_inmobiliario,
    acto_no_inmobiliario,
    documento,
    persona_fisica,
    persona_moral,
    representacion_legal,
    c_interes_juridico,
    recibo,
    folio_inmobiliario,
    folio_no_inmobiliario,
)


# Create your models here.


class c_tarifa(models.Model):
    """Tabla de tarifas

    Returns:
        int: Identificador de la tarifa
    """

    IdTarifa = models.AutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDTARIFA"
    )
    Nombre = models.CharField(
        max_length=100, null=False, db_column="NOMBRE", verbose_name="Tarifa"
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")
    Tarifa = models.FloatField(
        db_default=0.00, null=False, db_column="TARIFA", verbose_name="Tarifa"
    )
    Vigente = models.BooleanField(
        db_default=False, db_column="VIGENTE", verbose_name="¿Está vigente?"
    )

    class Meta:
        ordering = ("Vigente", "Nombre", "Tarifa")
        verbose_name_plural = "Tarifas y derechos"

    def __str__(self):
        return f"{self.Nombre}, {self.Vigente}"


class c_tipo_acto(models.Model):
    """Catálogo de tipos de actos

    Returns:
        int: Identificador de tipo de acto
    """

    IdTipoActo = models.AutoField(
        primary_key=True, unique=True, null=False, db_index=True, db_column="IDTIPOACTO"
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Tipo de acto",
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")

    EsInmobiliario = models.BooleanField(
        db_default=True,
        db_column="ACTOINMOBILIARIO",
        verbose_name="Asociado a un inmueble",
        help_text="¿Es un acto asociado a un folio inmobiliario?",
    )
    ModificaFolio = models.BooleanField(
        db_default=False,
        db_column="MODIFICAINMUEBLE",
        verbose_name="Modifica folio",
        help_text="¿El acto modifica algún dato de la carátura?",
    )
    Inmatricula = models.BooleanField(
        db_default=False,
        db_column="INMATRICULA",
        verbose_name="Crea nuevo(s) folio(s)",
        help_text="Indicar si contempla la inmatriculación",
    )
    ModificaDominio = models.BooleanField(
        db_default=False,
        db_column="ACTODOMINIO",
        verbose_name="Afecta al dominio",
        help_text="Cambia el dominio sobre el inmueble (propietarios, usuafructuarios, etc.)",
    )
    LimitaDominio = models.BooleanField(
        db_default=False,
        db_column="LIMITADOMINIO",
        verbose_name="Limita el dominio",
        help_text="¿Es un acto que limita el dominio? (gravámenes, usufructo, etc.)",
    )
    CorreccionError = models.BooleanField(
        db_default=False,
        db_column="CORRECCION",
        verbose_name="Corrección de error(es)",
        help_text="¿Corrige algún error atribuible a la institución?",
    )
  

    class Meta:
        ordering = ("Nombre", "Descripcion")
        verbose_name_plural = "Catálogo de tipos de actos"

    def __str__(self):
        return f"{self.Nombre}"



class c_clase_tramite(models.Model):
    """Catálogo de clases de trámites

    Debemos entender que la clase de trámite como por ejemplo (sin limitarse)
    1. Inscripción
    2. Corrección
    3. Emisión de constancia
    4. Emisión de certificado
    5. Aviso
    6. Inmatriculación
    7. Transición a folio real electrónico
    8. etc.
    Returns:
        int: Identificador de la clase de trámite
    """

    IdClaseTramite = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDCLASETRAMITE",
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Clase de trámite",
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")

    class Meta:
        ordering = ("Nombre", "Descripcion")
        verbose_name_plural = "Catálogo de clases de trámites"

    def __str__(self):
        return f"{self.Nombre}"


class t_requisito(models.Model):
    IdRequisito = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDREQUISITO",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Requisito",
        help_text="Nombre del requisito",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        null=True,
        verbose_name="Descripción",
        help_text="Descripción del requisito",
    )
    FundamentoLegal = models.TextField(
        db_column="FUNDAMENTO",
        null=True,
        verbose_name="Fundamento legal",
        help_text="Fundamento legal que sustenta el requisito",
    )
    DocumentoOriginal = models.BooleanField(
        db_default=True,
        db_column="DOCORIGINAL",
        verbose_name="Documento original",
        help_text="Si se requiere el documento original",
    )
    DocumentoCopia = models.BooleanField(
        db_default=True,
        db_column="DOCCOPIA",
        verbose_name="Documento en copia",
        help_text="Documento requerido en copia",
    )
    DocumentoDigital = models.BooleanField(
        db_default=True,
        db_column="DOCDIGITAL",
        verbose_name="Documento digital",
        help_text="El documento puede ser entrago en formato digital",
    )
    FirmaElectronica = models.BooleanField(
        db_default=False,
        db_column="FIRMAELECTRONICA",
        verbose_name="Requiere firma digital",
        help_text="Firma digital requerida",
    )
    Vigente = models.BooleanField(
        default=False, verbose_name="Vigente", help_text="¿Es un requisito vigente?"
    )
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES",
        verbose_name="Datos adicionales",
        null=True,
        help_text="Datos adicionales en formato JSon",
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        verbose_name="Fecha y hora del alta",
        help_text="Fecha y hora del alta",
        default=now(),
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        null=True,
        verbose_name="Fecha y hora de la última modificación",
        help_text="Fecha y hora de la última modificación",
    )

    class Meta:
        ordering = ("Nombre", "Vigente")
        verbose_name_plural = "Catálogo de requisitos"

    def __str__(self):
        return f"{self.Nombre}, {self.Vigente}"

class c_tipo_tramite(models.Model):
    """Catálogo de tipo de trámite

    Returns:
        int: Identificador del tipo de trámite
    """

    IdTipoTramite = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDTIPOTRAMITE",
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Tipo de trámite",
        help_text="Nombre del tipo de trámite",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        null=True,
        verbose_name="Descripción",
        help_text="Descripción del tipo de trámite",
    )

    IdClaseTramite = models.ForeignKey(
        c_clase_tramite,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDCLASETRAMITE",
        verbose_name="Clase de trámite",
        help_text="Clasificación del trámite",
    )
    IdTipoActo = models.ForeignKey(
        c_tipo_acto,
        models.CASCADE,
        null=True,
        db_column="IDTIPOACTO",
        verbose_name="Tipo de acto al que corresponde",
        help_text="Acto del tipo de trámite",
    )
    TipoVigente = models.BooleanField(
        default=False,
        db_column="TIPOVIGENTE",
        verbose_name="¿Está vigente?",
        help_text="Indicar si el tipo de trámite se encuentra vigente",
    )

    class Meta:
        ordering = ("Nombre",)
        verbose_name_plural = "Catálogo de tipos de trámites"

    def __str__(self):
        return f"{self.Nombre}, {self.IdClaseTramite}"


class t_tramite(models.Model):
    IdTramite = models.BigAutoField(
        primary_key=True, null=False, unique=True, db_index=True, db_column="IDTRAMITE"
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Trámite",
        help_text="Nombre del trámite (debe ser único)",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        verbose_name="Descripción",
        help_text="Descripción del trámite",
    )
    Version = models.PositiveSmallIntegerField(
        db_default=1,
        null=False,
        db_column="VERSION",
        verbose_name="Versión",
        help_text="Versión del trámite",
    )
    Activo = models.BooleanField(
        db_default=False,
        db_column="ACTIVO",
        verbose_name="Activo",
        help_text="¿EStá activo?",
    )
    FundamentoLegal = models.TextField(
        db_column="FUNDAMENTO",
        verbose_name="Fundamento",
        help_text="Fundamento jurídico",
    )
    URLReferencia = models.URLField(db_column="URL", verbose_name="URL")
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES",
        verbose_name="Datos adicionales",
        help_text="Datos adicionales en formato JSon",
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        verbose_name="Fecha y hora del alta",
        help_text="Fecha y hora del alta",
        default=now(),
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        verbose_name="Fecha y hora de la última modificación",
        help_text="Fecha y hora de la última modificación",
    )

    IdTipoTramite = models.ForeignKey(
        c_tipo_tramite,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPOTRAMITE",
        verbose_name="Tipo de trámite",
        help_text="Tipo de trámite al que corresponde",
    )

    class Meta:
        ordering = ("Nombre", "Version", "Activo")
        verbose_name_plural = "Catálogo de trámites"

    def __str__(self):
        return f"{self.Nombre}, {self.Version},{self.Activo}"

class r_requisito_tramite(models.Model):
    IdRequisitoTramite = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDREQTRAMITE",
    )

    idTramite = models.ForeignKey(
        t_tramite, on_delete=models.CASCADE, null=True, db_column="IDTRAMITE"
    )
    idRequisito = models.ForeignKey(
        t_requisito, on_delete=models.CASCADE, null=True, db_column="IDREQUISITO"
    )


class t_etapa(models.Model):
    idEtapa = models.BigAutoField(
        primary_key=True, db_index=True, unique=True, db_column="IDETAPA"
    )
    Version = models.PositiveSmallIntegerField(
        db_default=1,
        null=False,
        db_column="VERSION",
        verbose_name="Version",
        help_text="Versión",
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Etapa",
        help_text="Nombre de la etapa",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        null=True,
        verbose_name="Descripción",
        help_text="Descripción de la etapa",
    )
    Activo = models.BooleanField(
        db_default=False,
        db_column="ACTIVO",
        verbose_name="Activo",
        help_text="Indicar si la etapa está activa (disponible)",
    )
    FundamentoLegal = models.TextField(
        db_column="FUNDAMENTO",
        null=True,
        verbose_name="Fundamento legal",
        help_text="Fundamento legal que sustenta la etapa (opcional)",
    )
    TiempoReglamentario = models.PositiveSmallIntegerField(
        db_column="TREGLAMENTARIO",
        verbose_name="Tiempo máximo",
        help_text="Tiempo máximo (en días)",
    )
    DatosAdicionales = models.JSONField(
        db_column="DATOSADICIONALES",
        verbose_name="Datos adicionales",
        null=True,
        help_text="Datos adicionales en formato JSon",
    )
    FHAlta = models.DateTimeField(
        db_column="FHALTA",
        verbose_name="Fecha y hora del alta",
        help_text="Fecha y hora del alta",
        default=now(),
    )
    FHModificacion = models.DateTimeField(
        db_column="FHMODIF",
        verbose_name="Fecha y hora de la última modificación",
        null=True,
        help_text="Fecha y hora de la última modificación",
    )

    IdArea = models.ForeignKey(
        c_area,
        on_delete=models.CASCADE,
        null=False,
        db_column="IDAREA",
        verbose_name="Área designada",
        help_text="Área responsable de ejecutar la etapa",
    )

    class Meta:
        ordering = ("Nombre", "Version", "Activo")
        verbose_name_plural = "Catálogo de etapas"

    def __str__(self):
        return str(self.IdArea)


class t_nodo_etapa(models.Model):
    IdNodoEtapa = models.BigAutoField(
        primary_key=True, unique=True, db_index=True, db_column="IDNODOETAPA"
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHalta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    idTramite = models.ForeignKey(
        t_tramite, on_delete=models.CASCADE, null=True, db_column="IDTRAMITE"
    )

    def __str__(self):
        return self.IdNodoEtapa


class r_etapa_nodo_etapa(models.Model):

    Sentido = models.PositiveSmallIntegerField(
        choices=Const.SENTIDO, db_default=0, db_column="SENTIDO"
    )
    IdEtapa = models.ForeignKey(
        t_etapa, on_delete=models.Case, null=True, db_column="IDETAPA"
    )
    IdNodoEtapa = models.ForeignKey(
        t_nodo_etapa, on_delete=models.CASCADE, null=True, db_column="IDNODOETAPA"
    )


class t_tarea(models.Model):
    IdTarea = models.BigAutoField(
        primary_key=True, unique=True, db_index=True, db_column="IDTAREA"
    )
    Nombre = models.CharField(
        max_length=100, null=False, db_index=True, db_column="NOMBRE"
    )
    Descripcion = models.TextField(db_column="DESCRIPCION")
    Activo = models.BooleanField(db_default=False, db_column="ACTIVO")
    Parametros = models.CharField(max_length=200, null=True, db_column="PARAMETROS")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    def __str__(self):
        return self.IdTarea


class nodo_tarea(models.Model):
    IdNodoTarea = models.BigAutoField(
        primary_key=True, unique=True, null=False, db_column="IDNODOTAREA"
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdEtapa = models.ForeignKey(
        t_etapa, on_delete=models.CASCADE, null=True, db_column="IDETAPA"
    )

    def __str__(self):
        return self.IdNodoTarea


class r_tarea_nodo_tarea(models.Model):
    """Tabla de relación que permite asociar una tarea o tareas con otra u otas"""

    Sentido = models.PositiveSmallIntegerField(
        choices=Const.SENTIDO, db_default=0, db_column="SENTIDO"
    )
    IdTarea = models.ForeignKey(
        t_etapa, on_delete=models.Case, null=True, db_column="IDTAREA"
    )
    IdTareaNodoTarea = models.ForeignKey(
        nodo_tarea, on_delete=models.CASCADE, null=True, db_column="IDNODOTAREA"
    )


class c_aplicacion(models.Model):
    """Catálogo de aplicaciones

    Returns:
        str : Nombre y dirección relativa
    """

    IdAplicacion = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        verbose_name="Identificador",
        db_column="IDAPP",
    )
    Nombre = models.CharField(
        max_length=50,
        null=False,
        db_index=True,
        unique=True,
        db_column="NOMBRE",
        verbose_name="Aplicación",
        help_text="Nombre de la aplicación",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        verbose_name="Descripción",
        help_text="Descripción de la aplicación",
    )
    DireccionRelativa = models.CharField(
        max_length=100,
        null=False,
        db_default="",
        db_column="DIRECCIONRELATIVA",
        verbose_name="Dirección relativa",
        help_text="Dirección relativa de la aplicaación respecto a root del sitio",
    )
    FHAlta = models.DateTimeField(db_column="FHALTA", db_default=now())
    FHModificacion = models.DateTimeField(db_column="FHMODIF", null=True)

    class Meta:
        ordering = ["Nombre", "DireccionRelativa"]
        verbose_name_plural = "Aplicaciones"

    def __str__(self):
        return f"{self.Nombre}, {self.DireccionRelativa}"


class c_modulo(models.Model):
    """Catálogo de módulos sustantivos asociados

    Returns:
        str : Nombre del módulo y su aplicación
    """

    IdModulo = models.AutoField(
        primary_key=True, unique=True, null=False, verbose_name="Identificador"
    )
    Nombre = models.CharField(
        max_length=50,
        null=False,
        db_index=True,
        unique=True,
        db_column="NOMBRE",
        verbose_name="Módulo",
        help_text="Nombre del módulo",
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION",
        verbose_name="Descripción",
        help_text="Descripción del módulo",
    )
    Modulo = models.CharField(
        max_length=50,
        null=False,
        db_default="",
        db_column="MODULO",
        verbose_name="Módulo",
        help_text="Módulo Django",
    )
    idAplicacion = models.ForeignKey(
        c_aplicacion,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Aplicación",
        help_text="Aplicación a la que corresponde",
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES", null=True)
    FHAlta = models.DateTimeField(db_column="FHALTA", db_default=now())
    FHModificacion = models.DateTimeField(db_column="FHMODIF", null=True)

    class Meta:
        ordering = [
            "Nombre",
        ]
        verbose_name_plural = "Módulos registrales"

    def __str__(self):
        if self.idAplicacion != None:
            return f"{self.Nombre}, {self.idAplicacion.Nombre}, {self.idAplicacion.DireccionRelativa}"
        else:
            return f"{self.Nombre}, <Sin aplicación asociada>"


class bitacora(models.Model):
    """Bitácora

    Returns:
        int: Identificador de la entrada
    """

    IdEntrada = models.BigAutoField(
        primary_key=True, unique=True, db_index=True, null=False, db_column="IDENTRADA"
    )
    FHEntrada = models.DateTimeField(db_column="FHENTRADA")
    Operacion = models.TextField(db_column="OPERACION")
    Detalles = models.JSONField(db_column="DETALLES")
    EstadoInicial = models.JSONField(db_column="ESTADOINICIAL", null=True)
    EstadoFinal = models.JSONField(db_column="ESTADOFINAL", null=True)
    Tipo = models.PositiveSmallIntegerField(
        choices=Const.TIPO_ENTRADA_BITACORA, db_column="TIPO", db_default=0
    )

    def __str__(self):
        return self.IdEntrada


class solicitante(models.Model):
    IdSolicitante = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDSOLICITANTE",
    )
    CURP = models.CharField(max_length=20, null=True, db_index=True, db_column="CURP")
    RFC = models.CharField(max_length=15, db_index=True, db_column="RFC")
    NumeroDocumentoIdentidad = models.CharField(
        max_length=40, db_column="NUMDOCIDENTIDAD"
    )
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    PrimerApellido = models.CharField(max_length=100, null=False, db_column="APELLIDO1")
    SegundoApellido = models.CharField(
        max_length=100, null=False, db_column="APELLIDO2"
    )
    Telefono = models.CharField(max_length=20, db_column="TELEFONO")
    CorreoElectronico = models.EmailField(db_column="CORREO")
    SolicitanteInterno = models.BooleanField(db_default=False, db_column="SOLINTERNO")
    IdFedatarioFuncionario = models.ForeignKey(
        fedatario_y_funcionario,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDFEDFUNC",
    )
    IdTipoDocumentoIdentidad = models.ForeignKey(
        c_tipo_documento_identidad,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDTIPODOCIDENT",
    )
    Vialidad = models.CharField(
        max_length=100, null=True, db_index=True, db_column="NOMVIALIDAD"
    )
    TipoVialidad = models.PositiveSmallIntegerField(
        choices=Const.TIPO_VIALIDAD, db_default=0, db_column="TIPOVIALIDAD"
    )
    NumeroExterior = models.CharField(
        max_length=30,
        db_index=True,
        db_default="",
        null=True,
        db_column="NUMEXTERIOR",
        verbose_name="Número exterior",
        help_text="Número exterior, manzana-lote, kilómetro, etc.",
    )
    NumeroInterior = models.CharField(
        max_length=30,
        db_default="",
        null=True,
        db_column="NUMINTERIOR",
        verbose_name="Número interior",
        help_text="Número interior, casa, departamento, etc.",
    )
    ClaveGeoAsentamiento = models.ForeignKey(
        c_asentamiento_humano,
        on_delete=models.CASCADE,
        null=True,
        db_column="CLAVEASENTAMIENTO",
        verbose_name="Asentamiento",
        help_text="Colonia, barrio, pueblo, etc.",
    )
    ClaveGeoLocalidad = models.ForeignKey(
        c_localidad,
        on_delete=models.CASCADE,
        db_column="CVEGEOLOCALIDAD",
        null=True,
        verbose_name="Localidad",
    )

    def __str__(self):
        return self.IdSolicitante


class r_solicitante_usuario(models.Model):
    """Tabla de relación entre el solicitante y el usuario

    Returns:
        int: Identificador de la relación
    """

    RolUsuario = models.PositiveSmallIntegerField(
        choices=Const.ROL_USUARIO, db_column="ROLUSUARIO"
    )
    IdSolicitante = models.ForeignKey(
        solicitante, on_delete=models.CASCADE, null=True, db_column="IDSOLICITANTE"
    )
    IdUsuario = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )


class promovente(models.Model):
    IdPromovente = models.BigAutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_index=True,
        db_column="IDPROMOVENTE",
    )
    NumeroDocumentoIdentidad = models.CharField(
        max_length=40, null=False, db_column="NUMDOCIDENTIDAD"
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdPersonaFisica = models.ForeignKey(
        persona_fisica, on_delete=models.Model, null=True, db_column="IDPERSONAFISICA"
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
    IdUsuarioInterno = models.ForeignKey(
        usuario, models.CASCADE, null=True, db_column="IDUSUARIOINTERNO"
    )
    IdFedatarioFuncionario = models.ForeignKey(
        fedatario_y_funcionario,
        models.CASCADE,
        null=True,
        db_column="IDFEDATARIOFUNCIONARIO",
    )
    IdInteresJuridico = models.ForeignKey(
        c_interes_juridico,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDINTERESJURIDICO",
    )
    IdDocumentoIdentidad = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCIDENTIDAD"
    )

    def __str__(self):
        return self.IdPromovente


class r_rol_etapa(models.Model):

    IdEtapa = models.ForeignKey(
        t_etapa,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDETAPA",
        verbose_name="Etapa",
        help_text="Etapa",
    )
    Rol = models.PositiveSmallIntegerField(
        choices=Const.ROL_USUARIO_MODULO,
        db_default=0,
        db_column="ROL",
        verbose_name="Rol",
        help_text="Rol del usuario",
    )

    def __str__(self):
        return self.IdRolEtapa


class t_solicitud(models.Model):
    """Tabla de solicitudes

    Returns:
        int: Identificador de la solicitud
    """

    IdSolicitud = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDSOLICITUD",
    )
    IdSolicitudRelacionada = models.BigIntegerField(db_column="IDSOLICITUDRELACIONADA")
    Estatus = models.PositiveSmallIntegerField(
        choices=Const.ESTATUS_TRAMITE, db_default=0, db_column="ESTATUS"
    )
    Inmobiliario = models.BooleanField(db_default=True, db_column='INMOBILIARIO', verbose_name='Inmobiliario')
    IdSolicitante = models.ForeignKey(
        solicitante, on_delete=models.CASCADE, null=True, db_column="IDSOLICITANTE"
    )
    IdPromovente = models.ForeignKey(
        promovente, on_delete=models.CASCADE, null=True, db_column="IDPROMOVENTE"
    )

    FHSolicitud = models.DateTimeField(db_column="FHSOLICITUD")
    FHPrelacion = models.DateTimeField(db_column="FHPRELACION")
    FHConclusion = models.DateTimeField(db_column="FHCONCLUSION")
    FHAsignacion = models.DateTimeField(db_column="FHASIGNACION")
    Observaciones = models.TextField(db_column="OBSERVACIONES")
    FCompromiso = models.DateField(db_column="FCOMPROMISO")
    Urgencia = models.PositiveSmallIntegerField(
        choices=Const.NIVEL_URGENCIA, db_column="URGENCIA", db_default=0
    )
    Finalizado = models.BooleanField(db_column="FINALIZADO", db_default=False)

    IdRecibo = models.ForeignKey(
        recibo, on_delete=models.CASCADE, null=True, db_column="IDRECIBO"
    )

    IdInteresJuridico = models.ForeignKey(
        c_interes_juridico,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDINTERESJURIDICO",
    )
    IdTramite = models.ForeignKey(
        t_tramite, on_delete=models.CASCADE, null=True, db_column="IDTRAMITE"
    )
    IdOficina = models.ForeignKey(
        c_oficina, on_delete=models.CASCADE, null=True, db_column="IDOFICINA"
    )
    IdTarifa = models.ForeignKey(
        c_tarifa, models.CASCADE, null=True, db_column="IDTARIFA"
    )
    IdActoInmobiliario = models.ForeignKey(acto_inmobiliario, on_delete=models.CASCADE, null=True, db_column='IDACTOINMOBILIARIO',verbose_name='Acto inmobiliario')
    IdActoNoImobiliario = models.ForeignKey(acto_no_inmobiliario,on_delete=models.CASCADE, null=True, db_column='IDACTONOINMOBILIARIO',verbose_name='Acto no inmobiliario')

    def __str__(self):
        return self.IdSolicitud


class r_solicitud_rol_usuario(models.Model):
    """Relación usuario con la solicitud"""

    RolUsuario = models.PositiveSmallIntegerField(
        choices=Const.ROL_USUARIO, db_default=0, db_column="ROLUSUARIO"
    )
    IdSolicitud = models.ForeignKey(
        t_solicitud, on_delete=models.CASCADE, null=True, db_column="IDSOLICITUD"
    )
    IdUsuario = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIO"
    )

    def __str__(self):
        return self.IdSolicitudUsuario


class t_ejecucion_etapa(models.Model):
    """Tabla de control de la ejecución de las etapas correspondiente
    a una solicitud

    Returns:
        int: Identificador de la entrada de la ejecución de una etapa
    """

    IdEjecucionEtapa = models.BigAutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_index=True,
        db_column="IDEJECETAPA",
    )
    Estatus = models.PositiveSmallIntegerField(
        choices=Const.ESTATUS_TRAMITE, db_default=0, db_column="ESTATUS"
    )
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")
    Finalizado = models.BooleanField(db_column="FINALIZADO", db_default=False)

    IdSolicitud = models.ForeignKey(
        t_solicitud, on_delete=models.CASCADE, null=False, db_column="IDSOLICITUD"
    )
    IdEtapa = models.ForeignKey(
        t_etapa, on_delete=models.CASCADE, null=True, db_column="IDETAPA"
    )
    IdEjecucionEtapaSiguiente = models.BigIntegerField(
        db_column="IDEJECUCIONETAPASIGUIENTE"
    )
    IdEjecucionEtapaAnterior = models.BigIntegerField(
        db_column="IDEJECUCIONETAPAANTERIOR"
    )


class t_ejecucion_tarea(models.Model):
    """Tabla de control de la ejecución de las tareas

    Returns:
        int: Identificador de la ejecución
    """

    IdEjecucionTarea = models.BigAutoField(
        primary_key=True,
        null=False,
        db_index=True,
        unique=True,
        db_column="IDEJECUCIONTAREA",
    )
    Estatus = models.PositiveSmallIntegerField(
        choices=Const.ESTATUS_TRAMITE, db_default=0, db_column="ESTATUS"
    )
    FHInicio = models.DateTimeField(db_column="FHINICIO")
    FHConclusion = models.DateTimeField(db_column="FHCONCLUSION")
    ServicioEjecutado = models.JSONField(db_column="SERVICIOEJECUTADO")
    ResultadosEjecucion = models.JSONField(db_column="RESULTADOEJECUCION")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")
    Finalizado = models.BooleanField(db_column="FINALIZADO", db_default=False)

    def __str__(self):
        return self.IdEjecucionTarea


class r_folio_inmobiliario_solicitud(models.Model):
    """Tabla de relaciones de solicitudes y folios inmobiliarios

    Nota: Dado que una solicitud puede incluir varios folios y un folio
    puede ser objeto de varias solicitudes se ha optado por esta solución
    """

    IdFolioSolicitud = models.BigAutoField(
        primary_key=True,
        unique=True,
        db_index=True,
        null=False,
        db_column="IDFOLIOSOLICITUD",
    )

    IdSolicitud = models.ForeignKey(
        t_solicitud, on_delete=models.CASCADE, null=True, db_column="IDSOLICITUD"
    )
    FolioReal = models.ForeignKey(
        folio_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )


class r_folio_no_inmobiliario_solicitud(models.Model):
    """Tabla de relaciones de solicitudes y folios no inmobiliarios

    Nota: Dado que una solicitud puede incluir varios folios y un folio
    puede ser objeto de varias solicitudes se ha optado por esta solución

    """

    IdSolicitud = models.ForeignKey(
        t_solicitud, on_delete=models.CASCADE, null=True, db_column="IDSOLICITUD"
    )
    FolioReal = models.ForeignKey(
        folio_no_inmobiliario, on_delete=models.CASCADE, null=True, db_column="FOLIO"
    )

    def __str__(self):
        return self.IdFolioSolicitud


class r_requisito_solicitud(models.Model):
    """Tabla de relación de los requisitos correspondiente a una solitud

    Nota: Debe referirse para encontrar cuáles son los requisitos que deben
    cumplirse a la entidad r_requisito_tramite. Esta simplemente establece
    los estatus de los difernetes requisitos
    """

    FHVerificacion = models.BooleanField(db_column="FHVERIFICACION")
    Estatus = models.PositiveSmallIntegerField(
        choices=Const.ESTATUS_REQUISITO_SOLICITUD, db_default=0, null=False
    )

    IdSolicitud = models.ForeignKey(
        t_solicitud, on_delete=models.CASCADE, null=True, db_column="IDSOLICITUD"
    )
    IdRequisito = models.ForeignKey(
        t_requisito, on_delete=models.CASCADE, null=True, db_column="IDREQUISITO"
    )
    IdDocumento = models.ForeignKey(
        documento, on_delete=models.CASCADE, null=True, db_column="IDDOCUMENTO"
    )
    IdUsuarioVerificador = models.ForeignKey(
        usuario, on_delete=models.CASCADE, null=True, db_column="IDUSUARIOVERIFICADOR"
    )
