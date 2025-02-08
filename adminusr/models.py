from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from sireg.contantes import Const
from catalogo.models import c_asentamiento_humano, c_localidad


# Create your models here.


class c_area(models.Model):
    """Catálogo de áreas (de una organización)

    Returns:
        int: Identificador del área
    """

    IdArea = models.BigAutoField(
        primary_key=True, unique=True, db_index=True, db_column="IDAREA"
    )
    Nombre = models.CharField(
        max_length=50, unique=True, null=False, db_column="NOMBRE", verbose_name="Área"
    )
    Descripcion = models.TextField(
        db_column="DESCRIPCION", null=True, verbose_name="Descripción"
    )

    class Meta:
        ordering = ("Nombre",)
        verbose_name_plural = "Áreas de la organización"

    def __str__(self):
        return f"{self.Nombre}"


class c_dependencia(models.Model):
    """Catálogo de dependencias

    Returns:
        int: Identificado de la dependencia
    """

    IdDependencia = models.BigAutoField(
        primary_key=True, null=False, db_index=True, db_column="IDDEPENDENCIA"
    )
    NivelGobierno = models.PositiveSmallIntegerField(
        null=False,
        db_default=0,
        choices=Const.NIVEL_GOBIERNO,
        db_column="NIVELGOBIERNO",
        verbose_name="Nivel de Goberno",
    )
    Poder = models.IntegerField(
        null=False,
        db_default=0,
        choices=Const.PODER,
        db_column="PODER",
        verbose_name="¿A cuál poder pertenece?",
    )
    Nombre = models.CharField(
        max_length=100, null=False, db_column="NOMBRE", verbose_name="Dependencia"
    )
    NombreAnterior = models.CharField(
        max_length=100,
        null=True,
        db_column="NOMBREANTERIOR",
        verbose_name="Nombre anterior (si lo tuviese)",
    )
    FHAlta = models.DateTimeField(db_column="FHALTA", verbose_name="Fecha del alta")
    FHModificacion = models.DateTimeField(
        db_column="FMODIF", verbose_name="Fecha de la última modificación"
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
        db_column="NUMEXTERIOR",
        verbose_name="Número exterior",
        null=True,
        default="",
        help_text="Número exterior, manzana-lote, kilómetro, etc.",
    )
    NumeroInterior = models.CharField(
        max_length=30,
        db_column="NUMINTERIOR",
        verbose_name="Número interior",
        null=True,
        help_text="Número interior, casa, departamento, etc.",
    )
    ClaveGeogAsentamiento = models.ForeignKey(
        c_asentamiento_humano,
        on_delete=models.CASCADE,
        null=True,
        db_column="CLAVEASENTAMIENTO",
        verbose_name="Asentamiento",
        help_text="Clase de asentamiento humano: Colonia, barrio, pueblo, etc.",
    )
    ClaveGeogLocalidad = models.ForeignKey(
        c_localidad,
        on_delete=models.CASCADE,
        db_column="CVEGEOLOCALIDAD",
        null=True,
        verbose_name="Localidad",
        help_text="Clave de localidad",
    )

    class Meta:
        ordering = (
            "Nombre",
            "NombreAnterior",
            "Poder",
            "NivelGobierno",
        )
        verbose_name_plural = "Catálogo de dependencias"

    def __str__(self):
        return f"{self.Nombre}, {self.ClaveEntidadJurisdiccion}"


class c_oficina(models.Model):
    """Catálogo de oficinas

    Returns:
        int: Identificador de la oficina
    """

    IdOficina = models.BigAutoField(
        primary_key=True, unique=True, db_index=True, db_column="IDOFICINA"
    )
    Nombre = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        db_column="NOMBRE",
        verbose_name="Oficina",
    )
    prefijo_oficina = models.CharField(
        max_length=2,
        db_column="PREFIJOOFICINA",
        db_default="00",
        null=False,
        verbose_name="Prefijo",
        help_text="Prefijo (2 posiciones) de la oficina registral",
    )
    Descripcion = models.TextField(db_column="DESCRIPCION", verbose_name="Descripción")
    Receptora = models.BooleanField(
        db_default=False,
        db_column="RECEPTORA",
        verbose_name="¿Es receptora de solicitudes de trámites",
    )
    Virtual = models.BooleanField(
        db_default=False, db_column="VIRTUAL", verbose_name="¿Es una oficina virtual?"
    )
    Registro = models.BooleanField(
        db_default=False, db_column="REGISTRO", verbose_name="¿Inscriben actos?"
    )
    ConAcervo = models.BooleanField(
        db_default=False,
        db_column="CONACERVO",
        verbose_name="¿Cuenta con un acervo histórico?",
    )
    Activo = models.BooleanField(
        db_default=False, db_column="ACTIVO", verbose_name="¿Es una oficina activa?"
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
        null=True,
        db_default="",
        db_column="NUMEXTERIOR",
        verbose_name="Número exterior",
        help_text="Número exterior, manzana-lote, kilómetro, etc.",
    )
    NumeroInterior = models.CharField(
        max_length=30,
        db_column="NUMINTERIOR",
        null=True,
        db_default="",
        verbose_name="Número interior",
        help_text="Número interior, casa, departamento, etc.",
    )
    ClaveGeogAsentamiento = models.ForeignKey(
        c_asentamiento_humano,
        on_delete=models.CASCADE,
        null=True,
        db_column="CLAVEASENTAMIENTO",
        verbose_name="Asentamiento",
        help_text="Clase de asentamiento humano: Colonia, barrio, pueblo, etc.",
    )

    class Meta:
        ordering = ("Nombre", "Descripcion")
        verbose_name_plural = "Oficinas de la institución"

    def __str__(self):
        return f"{self.Nombre}"


class usuario(models.Model):
    """Tabla de usuarios

    Nota: Es la entidad central de control de los usuarios.
    De esta tabla deben excluirse aquellos que no son funcionarios
    del registro

    Returns:
        int: Identificador del usuario
    """

    IdUsuario = models.BigIntegerField(
        primary_key=True, null=False, db_index=True, db_column="IDUSUARIO"
    )
    Nombre = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="NOMBRE",
        verbose_name="Nombre",
    )
    PrimerApellido = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="APELLIDO1",
        verbose_name="Primer apellido",
    )
    SegundoApellido = models.CharField(
        max_length=100,
        null=False,
        db_index=True,
        db_column="APELLIDO2",
        verbose_name="Segundo apellido",
    )
    CURP = models.CharField(
        max_length=20,
        null=False,
        db_index=True,
        db_column="CURP",
        verbose_name="Clave única de registro de población",
    )
    RFC = models.CharField(
        max_length=15,
        null=True,
        db_column="RFC",
        verbose_name="Registro federal de contribuyentes",
    )
    PreguntaSeguridad = models.TextField(
        db_column="PREGUNTASEGURIDAD", verbose_name="Pregunta de seguridad"
    )
    RespuestaSeguridad = models.TextField(
        db_column="RESPUESTASEGURIDAD", verbose_name="Respuesta de seguridad"
    )
    Activo = models.BooleanField(
        db_default=False, db_column="ACTIVO", verbose_name="¿Es un usuairo activo?"
    )
    MotivoBaja = models.CharField(
        max_length=200,
        null=True,
        db_column="MOTIVOBAJA",
        verbose_name="Si no está activo: ¿Cuál es el motivo?",
    )
    Cargo = models.CharField(
        max_length=100, null=True, db_column="CARGO", verbose_name="Cargo que tiene"
    )
    AccesoFueraHorario = models.BooleanField(
        db_default=False,
        db_column="ACCESOFHORARIO",
        verbose_name="¿Accede fuera del horario laboral?",
    )

    FHAlta = models.DateTimeField(db_column="FHALTA", default=now())
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Usuario del sistema"
    )
    IdArea = models.ForeignKey(
        c_area,
        on_delete=models.CASCADE,
        null=True,
        db_column="IDAREA",
        verbose_name="Área al que está adscrito(a)",
    )
    idOficina = models.ForeignKey(c_oficina, on_delete=models.CASCADE, null=True, db_column='IDOFICINA',verbose_name='Oficina')

    class Meta:
        ordering = ("PrimerApellido", "SegundoApellido", "Nombre", "Cargo")
        verbose_name_plural = "Usuarios intstitucionales"

    def __str__(self):
        return f"{self.Nombre}, {self.PrimerApellido}, {self.SegundoApellido}, {self.Cargo}, {self.CURP}, {self.RFC}"


class fedatario_y_funcionario(models.Model):
    """Tabla de usuarios y fedatarios

    Returns:
        int: Identificador del fedatario o funcionario
    """

    idFedatarioFuncionario = models.BigAutoField(
        primary_key=True, null=False, db_index=True, unique=True, db_column="IDFEDFUNC"
    )
    Activo = models.BooleanField(db_default=False, db_column="ACTIVO")
    Nombre = models.CharField(max_length=100, null=False, db_column="NOMBRE")
    PrimerApellido = models.CharField(max_length=100, null=False, db_column="APELLIDO1")
    SegundoApellido = models.CharField(
        max_length=100, null=False, db_column="APELLIDO2"
    )
    Telefono = models.CharField(max_length=15, db_column="TELEFONO")
    CorreoElectronico = models.EmailField(db_column="CORREOELECTRONICO")
    NombreOficina = models.CharField(max_length=50, null=False, db_column="OFICINA")
    Tipo = models.IntegerField(
        choices=Const.TIPO_FEDATARIO_FUNCIONARIO, db_default=0, db_column="TIPO"
    )
    Nombramiento = models.CharField(max_length=100, db_column="NOMBRAMIENTO")
    FNombramiento = models.DateField(db_column="FNOMBRAMIENTO")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    IdDependencia = models.ForeignKey(
        c_dependencia, on_delete=models.CASCADE, null=True, db_column="IDDEPENDENCIA"
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
        null=True,
        db_default="",
        db_column="NUMEXTERIOR",
        verbose_name="Número exterior",
        help_text="Número exterior, manzana-lote, kilómetro, etc.",
    )
    NumeroInterior = models.CharField(
        max_length=30,
        db_column="NUMINTERIOR",
        db_default="",
        null=True,
        verbose_name="Número interior",
        help_text="Número interior, casa, departamento, etc.",
    )
    ClaveGeogAsentamiento = models.ForeignKey(
        c_asentamiento_humano,
        on_delete=models.CASCADE,
        null=True,
        db_column="CLAVEASENTAMIENTO",
        verbose_name="Asentamiento",
        help_text="Clase de asentamiento humano: Colonia, barrio, pueblo, etc.",
    )

    def __str__(self):
        return self.idFedatarioFuncionario


class usuario_oficial_externo(models.Model):
    """Tabla con los usuarios externos que acceden

    Returns:
        int: Identificador del usuario oficial externo
    """

    IdUsuarioOficialExterno = models.BigIntegerField(
        primary_key=True, null=False, db_index=True, db_column="IDUSUARIO"
    )
    PreguntaSeguridad = models.TextField(db_column="PREGUNTASEGURIDAD")
    RespuestaSeguridad = models.TextField(db_column="RESPUESTASEGURIDAD")
    Activo = models.BooleanField(db_default=False, db_column="ACTIVO")
    MotivoBaja = models.CharField(max_length=200, null=True, db_column="MOTIVOBAJA")
    DatosAdicionales = models.JSONField(db_column="DATOSADICIONALES")
    FHAlta = models.DateTimeField(db_column="FHALTA")
    FHModificacion = models.DateTimeField(db_column="FHMODIF")

    # En fedatario_y_funcionario se encuentran los detalles del usuario.
    IdFedatarioFuncionario = models.ForeignKey(
        fedatario_y_funcionario,
        null=True,
        on_delete=models.CASCADE,
        db_column="IDFEDFUNC",
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.IdUsuario


class usuario_externo(models.Model):
    IdUsuarioExterno = models.BigIntegerField(
        primary_key=True, null=False, db_index=True, db_column="IDUSUARIO"
    )
    Nombre = models.CharField(
        max_length=100, null=False, db_index=True, db_column="NOMBRE"
    )
    PrimerApellido = models.CharField(
        max_length=100, null=False, db_index=True, db_column="APELLIDO1"
    )
    SegundoApellido = models.CharField(
        max_length=100, null=False, db_index=True, db_column="APELLIDO2"
    )
    CURP = models.CharField(max_length=20, null=False, db_index=True, db_column="CURP")
    RFC = models.CharField(max_length=15, null=True, db_column="RFC")
    PreguntaSeguridad = models.TextField(db_column="PREGUNTASEGURIDAD")
    RespuestaSeguridad = models.TextField(db_column="RESPUESTASEGURIDAD")
    Activo = models.BooleanField(db_default=False, db_column="ACTIVO")
    MotivoBaja = models.CharField(max_length=200, null=True, db_column="MOTIVOBAJA")

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.IdUsuarioExterno
