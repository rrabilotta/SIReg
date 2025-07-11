# Generated by Django 5.1.5 on 2025-02-08 01:35

import datetime
import django.db.models.deletion
import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminusr', '0001_initial'),
        ('catalogo', '0001_initial'),
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bitacora',
            fields=[
                ('IdEntrada', models.BigAutoField(db_column='IDENTRADA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('FHEntrada', models.DateTimeField(db_column='FHENTRADA')),
                ('Operacion', models.TextField(db_column='OPERACION')),
                ('Detalles', models.JSONField(db_column='DETALLES')),
                ('Tipo', models.PositiveSmallIntegerField(choices=[(0, 'General'), (1, 'Advertencia'), (2, 'Error'), (3, 'Operación'), (4, 'Modificación'), (5, 'Alta'), (6, 'Baja')], db_column='TIPO', db_default=0)),
            ],
        ),
        migrations.CreateModel(
            name='c_aplicacion',
            fields=[
                ('IdAplicacion', models.AutoField(db_column='IDAPP', db_index=True, primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre de la aplicación', max_length=50, unique=True, verbose_name='Aplicación')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción de la aplicación', verbose_name='Descripción')),
                ('DireccionRelativa', models.CharField(db_column='DIRECCIONRELATIVA', db_default='', help_text='Dirección relativa de la aplicaación respecto a root del sitio', max_length=100, verbose_name='Dirección relativa')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA', db_default=datetime.datetime(2025, 2, 8, 1, 35, 37, 75395, tzinfo=datetime.timezone.utc))),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF', null=True)),
            ],
            options={
                'verbose_name_plural': 'Aplicaciones',
                'ordering': ['Nombre', 'DireccionRelativa'],
            },
        ),
        migrations.CreateModel(
            name='c_clase_tramite',
            fields=[
                ('IdClaseTramite', models.AutoField(db_column='IDCLASETRAMITE', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=50, unique=True, verbose_name='Clase de trámite')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de clases de trámites',
                'ordering': ('Nombre', 'Descripcion'),
            },
        ),
        migrations.CreateModel(
            name='c_tarifa',
            fields=[
                ('IdTarifa', models.AutoField(db_column='IDTARIFA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=100, verbose_name='Tarifa')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', verbose_name='Descripción')),
                ('Tarifa', models.FloatField(db_column='TARIFA', db_default=0.0, verbose_name='Tarifa')),
                ('Vigente', models.BooleanField(db_column='VIGENTE', db_default=False, verbose_name='¿Está vigente?')),
            ],
            options={
                'verbose_name_plural': 'Tarifas y derechos',
                'ordering': ('Vigente', 'Nombre', 'Tarifa'),
            },
        ),
        migrations.CreateModel(
            name='c_tipo_acto',
            fields=[
                ('IdTipoActo', models.AutoField(db_column='IDTIPOACTO', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=50, unique=True, verbose_name='Tipo de acto')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', verbose_name='Descripción')),
                ('EsInmobiliario', models.BooleanField(db_column='ACTOINMOBILIARIO', db_default=True, help_text='¿Es un acto asociado a un folio inmobiliario?', verbose_name='Asociado a un inmueble')),
                ('ModificaFolio', models.BooleanField(db_column='MODIFICAINMUEBLE', db_default=False, help_text='¿El acto modifica algún dato de la carátura?', verbose_name='Modifica folio')),
                ('Inmatricula', models.BooleanField(db_column='INMATRICULA', db_default=False, help_text='Indicar si contempla la inmatriculación', verbose_name='Crea nuevo(s) folio(s)')),
                ('ModificaDominio', models.BooleanField(db_column='ACTODOMINIO', db_default=False, help_text='Cambia el dominio sobre el inmueble (propietarios, usuafructuarios, etc.)', verbose_name='Afecta al dominio')),
                ('LimitaDominio', models.BooleanField(db_column='LIMITADOMINIO', db_default=False, help_text='¿Es un acto que limita el dominio? (gravámenes, usufructo, etc.)', verbose_name='Limita el dominio')),
                ('CorreccionError', models.BooleanField(db_column='CORRECCION', db_default=False, help_text='¿Corrige algún error atribuible a la institución?', verbose_name='Corrección de error(es)')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de tipos de actos',
                'ordering': ('Nombre', 'Descripcion'),
            },
        ),
        migrations.CreateModel(
            name='nodo_tarea',
            fields=[
                ('IdNodoTarea', models.BigAutoField(db_column='IDNODOTAREA', primary_key=True, serialize=False, unique=True)),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF')),
            ],
        ),
        migrations.CreateModel(
            name='t_ejecucion_tarea',
            fields=[
                ('IdEjecucionTarea', models.BigAutoField(db_column='IDEJECUCIONTAREA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Estatus', models.PositiveSmallIntegerField(choices=[(0, 'No iniciado'), (1, 'Recibido'), (2, 'En proceso'), (3, 'Rechazado'), (4, 'Resuelto'), (5, 'Entregado'), (98, 'Cancelado'), (99, 'Finalizado')], db_column='ESTATUS', db_default=0)),
                ('FHInicio', models.DateTimeField(db_column='FHINICIO')),
                ('FHConclusion', models.DateTimeField(db_column='FHCONCLUSION')),
                ('ServicioEjecutado', models.JSONField(db_column='SERVICIOEJECUTADO')),
                ('ResultadosEjecucion', models.JSONField(db_column='RESULTADOEJECUCION')),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF')),
                ('Finalizado', models.BooleanField(db_column='FINALIZADO', db_default=False)),
            ],
        ),
        migrations.CreateModel(
            name='t_nodo_etapa',
            fields=[
                ('IdNodoEtapa', models.BigAutoField(db_column='IDNODOETAPA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES')),
                ('FHalta', models.DateTimeField(db_column='FHALTA')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF')),
            ],
        ),
        migrations.CreateModel(
            name='t_requisito',
            fields=[
                ('IdRequisito', models.BigAutoField(db_column='IDREQUISITO', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre del requisito', max_length=100, verbose_name='Requisito')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción del requisito', null=True, verbose_name='Descripción')),
                ('FundamentoLegal', models.TextField(db_column='FUNDAMENTO', help_text='Fundamento legal que sustenta el requisito', null=True, verbose_name='Fundamento legal')),
                ('DocumentoOriginal', models.BooleanField(db_column='DOCORIGINAL', db_default=True, help_text='Si se requiere el documento original', verbose_name='Documento original')),
                ('DocumentoCopia', models.BooleanField(db_column='DOCCOPIA', db_default=True, help_text='Documento requerido en copia', verbose_name='Documento en copia')),
                ('DocumentoDigital', models.BooleanField(db_column='DOCDIGITAL', db_default=True, help_text='El documento puede ser entrago en formato digital', verbose_name='Documento digital')),
                ('FirmaElectronica', models.BooleanField(db_column='FIRMAELECTRONICA', db_default=False, help_text='Firma digital requerida', verbose_name='Requiere firma digital')),
                ('Vigente', models.BooleanField(default=False, help_text='¿Es un requisito vigente?', verbose_name='Vigente')),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES', help_text='Datos adicionales en formato JSon', null=True, verbose_name='Datos adicionales')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 2, 8, 1, 35, 37, 73897, tzinfo=datetime.timezone.utc), help_text='Fecha y hora del alta', verbose_name='Fecha y hora del alta')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF', help_text='Fecha y hora de la última modificación', null=True, verbose_name='Fecha y hora de la última modificación')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de requisitos',
                'ordering': ('Nombre', 'Vigente'),
            },
        ),
        migrations.CreateModel(
            name='t_tarea',
            fields=[
                ('IdTarea', models.BigAutoField(db_column='IDTAREA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, max_length=100)),
                ('Descripcion', models.TextField(db_column='DESCRIPCION')),
                ('Activo', models.BooleanField(db_column='ACTIVO', db_default=False)),
                ('Parametros', models.CharField(db_column='PARAMETROS', max_length=200, null=True)),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF')),
            ],
        ),
        migrations.CreateModel(
            name='c_modulo',
            fields=[
                ('IdModulo', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre del módulo', max_length=50, unique=True, verbose_name='Módulo')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción del módulo', verbose_name='Descripción')),
                ('Modulo', models.CharField(db_column='MODULO', db_default='', help_text='Módulo Django', max_length=50, verbose_name='Módulo')),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES', null=True)),
                ('FHAlta', models.DateTimeField(db_column='FHALTA', db_default=datetime.datetime(2025, 2, 8, 1, 35, 37, 75533, tzinfo=datetime.timezone.utc))),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF', null=True)),
                ('idAplicacion', models.ForeignKey(help_text='Aplicación a la que corresponde', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.c_aplicacion', verbose_name='Aplicación')),
            ],
            options={
                'verbose_name_plural': 'Módulos registrales',
                'ordering': ['Nombre'],
            },
        ),
        migrations.CreateModel(
            name='c_tipo_tramite',
            fields=[
                ('IdTipoTramite', models.AutoField(db_column='IDTIPOTRAMITE', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', help_text='Nombre del tipo de trámite', max_length=50, unique=True, verbose_name='Tipo de trámite')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción del tipo de trámite', null=True, verbose_name='Descripción')),
                ('TipoVigente', models.BooleanField(db_column='TIPOVIGENTE', default=False, help_text='Indicar si el tipo de trámite se encuentra vigente', verbose_name='¿Está vigente?')),
                ('IdClaseTramite', models.ForeignKey(db_column='IDCLASETRAMITE', help_text='Clasificación del trámite', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.c_clase_tramite', verbose_name='Clase de trámite')),
                ('IdTipoActo', models.ForeignKey(db_column='IDTIPOACTO', help_text='Acto del tipo de trámite', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.c_tipo_acto', verbose_name='Tipo de acto al que corresponde')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de tipos de trámites',
                'ordering': ('Nombre',),
            },
        ),
        migrations.CreateModel(
            name='promovente',
            fields=[
                ('IdPromovente', models.BigAutoField(db_column='IDPROMOVENTE', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('NumeroDocumentoIdentidad', models.CharField(db_column='NUMDOCIDENTIDAD', max_length=40)),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF')),
                ('IdDocumentoIdentidad', models.ForeignKey(db_column='IDDOCIDENTIDAD', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.documento')),
                ('IdFedatarioFuncionario', models.ForeignKey(db_column='IDFEDATARIOFUNCIONARIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.fedatario_y_funcionario')),
                ('IdInteresJuridico', models.ForeignKey(db_column='IDINTERESJURIDICO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.c_interes_juridico')),
                ('IdPersonaFisica', models.ForeignKey(db_column='IDPERSONAFISICA', null=True, on_delete=models.Model, to='registro.persona_fisica')),
                ('IdPersonaMoral', models.ForeignKey(db_column='IDPERSONAMORAL', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.persona_moral')),
                ('IdRepresentacion', models.ForeignKey(db_column='IDREPRESENTACION', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.representacion_legal')),
                ('IdUsuarioInterno', models.ForeignKey(db_column='IDUSUARIOINTERNO', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='solicitante',
            fields=[
                ('IdSolicitante', models.BigAutoField(db_column='IDSOLICITANTE', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('CURP', models.CharField(db_column='CURP', db_index=True, max_length=20, null=True)),
                ('RFC', models.CharField(db_column='RFC', db_index=True, max_length=15)),
                ('NumeroDocumentoIdentidad', models.CharField(db_column='NUMDOCIDENTIDAD', max_length=40)),
                ('Nombre', models.CharField(db_column='NOMBRE', max_length=100)),
                ('PrimerApellido', models.CharField(db_column='APELLIDO1', max_length=100)),
                ('SegundoApellido', models.CharField(db_column='APELLIDO2', max_length=100)),
                ('Telefono', models.CharField(db_column='TELEFONO', max_length=20)),
                ('CorreoElectronico', models.EmailField(db_column='CORREO', max_length=254)),
                ('SolicitanteInterno', models.BooleanField(db_column='SOLINTERNO', db_default=False)),
                ('Vialidad', models.CharField(db_column='NOMVIALIDAD', db_index=True, max_length=100, null=True)),
                ('TipoVialidad', models.PositiveSmallIntegerField(choices=[(0, 'Calle'), (1, 'Avenida'), (2, 'Periférico'), (3, 'Cerrada'), (4, 'Calzada'), (5, 'Eje vial'), (6, 'Privada'), (7, 'Circuito'), (8, 'Viaducto'), (9, 'Pasaje'), (10, 'Peatonal'), (11, 'Continuación'), (12, 'Callejón'), (13, 'Corredor'), (14, 'Prolongación'), (15, 'Andador'), (16, 'Carretera'), (17, 'Boulevard'), (18, 'Ampliación'), (19, 'Circunvalación'), (20, 'Glorieta'), (21, 'Carretera'), (22, 'Retorno'), (23, 'Enlace'), (24, 'Vereda'), (25, 'Diagonal'), (26, 'Retorno U'), (27, 'Rampa de frenado'), (28, 'Otro')], db_column='TIPOVIALIDAD', db_default=0)),
                ('NumeroExterior', models.CharField(db_column='NUMEXTERIOR', db_default='', db_index=True, help_text='Número exterior, manzana-lote, kilómetro, etc.', max_length=30, null=True, verbose_name='Número exterior')),
                ('NumeroInterior', models.CharField(db_column='NUMINTERIOR', db_default='', help_text='Número interior, casa, departamento, etc.', max_length=30, null=True, verbose_name='Número interior')),
                ('ClaveGeoAsentamiento', models.ForeignKey(db_column='CLAVEASENTAMIENTO', help_text='Colonia, barrio, pueblo, etc.', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_asentamiento_humano', verbose_name='Asentamiento')),
                ('ClaveGeoLocalidad', models.ForeignKey(db_column='CVEGEOLOCALIDAD', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_localidad', verbose_name='Localidad')),
                ('IdFedatarioFuncionario', models.ForeignKey(db_column='IDFEDFUNC', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.fedatario_y_funcionario')),
                ('IdTipoDocumentoIdentidad', models.ForeignKey(db_column='IDTIPODOCIDENT', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.c_tipo_documento_identidad')),
            ],
        ),
        migrations.CreateModel(
            name='r_solicitante_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RolUsuario', models.PositiveSmallIntegerField(choices=[(0, 'Desconocido'), (1, 'Supervisión'), (2, 'Recepción'), (3, 'Inscripción'), (4, 'Certificación'), (5, 'Calificación'), (6, 'Jurídico'), (7, 'Externo autorizado'), (8, 'Auditoría')], db_column='ROLUSUARIO')),
                ('IdUsuario', models.ForeignKey(db_column='IDUSUARIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.usuario')),
                ('IdSolicitante', models.ForeignKey(db_column='IDSOLICITANTE', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='t_etapa',
            fields=[
                ('idEtapa', models.BigAutoField(db_column='IDETAPA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Version', models.PositiveSmallIntegerField(db_column='VERSION', db_default=1, help_text='Versión', verbose_name='Version')),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre de la etapa', max_length=100, verbose_name='Etapa')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción de la etapa', null=True, verbose_name='Descripción')),
                ('Activo', models.BooleanField(db_column='ACTIVO', db_default=False, help_text='Indicar si la etapa está activa (disponible)', verbose_name='Activo')),
                ('FundamentoLegal', models.TextField(db_column='FUNDAMENTO', help_text='Fundamento legal que sustenta la etapa (opcional)', null=True, verbose_name='Fundamento legal')),
                ('TiempoReglamentario', models.PositiveSmallIntegerField(db_column='TREGLAMENTARIO', help_text='Tiempo máximo (en días)', verbose_name='Tiempo máximo')),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES', help_text='Datos adicionales en formato JSon', null=True, verbose_name='Datos adicionales')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 2, 8, 1, 35, 37, 74559, tzinfo=datetime.timezone.utc), help_text='Fecha y hora del alta', verbose_name='Fecha y hora del alta')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF', help_text='Fecha y hora de la última modificación', null=True, verbose_name='Fecha y hora de la última modificación')),
                ('IdArea', models.ForeignKey(db_column='IDAREA', help_text='Área responsable de ejecutar la etapa', on_delete=django.db.models.deletion.CASCADE, to='adminusr.c_area', verbose_name='Área designada')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de etapas',
                'ordering': ('Nombre', 'Version', 'Activo'),
            },
        ),
        migrations.CreateModel(
            name='r_tarea_nodo_tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentido', models.PositiveSmallIntegerField(choices=[(0, 'Actual'), (1, 'Anterior'), (2, 'Siguiente'), (3, 'Error'), (4, 'Final')], db_column='SENTIDO', db_default=0)),
                ('IdTareaNodoTarea', models.ForeignKey(db_column='IDNODOTAREA', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.nodo_tarea')),
                ('IdTarea', models.ForeignKey(db_column='IDTAREA', null=True, on_delete=django.db.models.expressions.Case, to='tramite.t_etapa')),
            ],
        ),
        migrations.CreateModel(
            name='r_rol_etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rol', models.PositiveSmallIntegerField(choices=[(0, 'Deconocido'), (1, 'Inicio'), (2, 'Reinicio'), (3, 'Suspensión')], db_column='ROL', db_default=0, help_text='Rol del usuario', verbose_name='Rol')),
                ('IdEtapa', models.ForeignKey(db_column='IDETAPA', help_text='Etapa', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_etapa', verbose_name='Etapa')),
            ],
        ),
        migrations.AddField(
            model_name='nodo_tarea',
            name='IdEtapa',
            field=models.ForeignKey(db_column='IDETAPA', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_etapa'),
        ),
        migrations.CreateModel(
            name='r_etapa_nodo_etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentido', models.PositiveSmallIntegerField(choices=[(0, 'Actual'), (1, 'Anterior'), (2, 'Siguiente'), (3, 'Error'), (4, 'Final')], db_column='SENTIDO', db_default=0)),
                ('IdEtapa', models.ForeignKey(db_column='IDETAPA', null=True, on_delete=django.db.models.expressions.Case, to='tramite.t_etapa')),
                ('IdNodoEtapa', models.ForeignKey(db_column='IDNODOETAPA', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_nodo_etapa')),
            ],
        ),
        migrations.CreateModel(
            name='t_solicitud',
            fields=[
                ('IdSolicitud', models.BigAutoField(db_column='IDSOLICITUD', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('IdSolicitudRelacionada', models.BigIntegerField(db_column='IDSOLICITUDRELACIONADA')),
                ('Estatus', models.PositiveSmallIntegerField(choices=[(0, 'No iniciado'), (1, 'Recibido'), (2, 'En proceso'), (3, 'Rechazado'), (4, 'Resuelto'), (5, 'Entregado'), (98, 'Cancelado'), (99, 'Finalizado')], db_column='ESTATUS', db_default=0)),
                ('Inmobiliario', models.BooleanField(db_column='INMOBILIARIO', db_default=True, verbose_name='Inmobiliario')),
                ('FHSolicitud', models.DateTimeField(db_column='FHSOLICITUD')),
                ('FHPrelacion', models.DateTimeField(db_column='FHPRELACION')),
                ('FHConclusion', models.DateTimeField(db_column='FHCONCLUSION')),
                ('FHAsignacion', models.DateTimeField(db_column='FHASIGNACION')),
                ('Observaciones', models.TextField(db_column='OBSERVACIONES')),
                ('FCompromiso', models.DateField(db_column='FCOMPROMISO')),
                ('Urgencia', models.PositiveSmallIntegerField(choices=[(0, 'Normal'), (1, 'Urgente'), (2, 'Muy urgente')], db_column='URGENCIA', db_default=0)),
                ('Finalizado', models.BooleanField(db_column='FINALIZADO', db_default=False)),
                ('IdActoInmobiliario', models.ForeignKey(db_column='IDACTOINMOBILIARIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.acto_inmobiliario', verbose_name='Acto inmobiliario')),
                ('IdActoNoImobiliario', models.ForeignKey(db_column='IDACTONOINMOBILIARIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.acto_no_inmobiliario', verbose_name='Acto no inmobiliario')),
                ('IdInteresJuridico', models.ForeignKey(db_column='IDINTERESJURIDICO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.c_interes_juridico')),
                ('IdOficina', models.ForeignKey(db_column='IDOFICINA', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.c_oficina')),
                ('IdPromovente', models.ForeignKey(db_column='IDPROMOVENTE', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.promovente')),
                ('IdRecibo', models.ForeignKey(db_column='IDRECIBO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.recibo')),
                ('IdSolicitante', models.ForeignKey(db_column='IDSOLICITANTE', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.solicitante')),
                ('IdTarifa', models.ForeignKey(db_column='IDTARIFA', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.c_tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='t_ejecucion_etapa',
            fields=[
                ('IdEjecucionEtapa', models.BigAutoField(db_column='IDEJECETAPA', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Estatus', models.PositiveSmallIntegerField(choices=[(0, 'No iniciado'), (1, 'Recibido'), (2, 'En proceso'), (3, 'Rechazado'), (4, 'Resuelto'), (5, 'Entregado'), (98, 'Cancelado'), (99, 'Finalizado')], db_column='ESTATUS', db_default=0)),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF')),
                ('Finalizado', models.BooleanField(db_column='FINALIZADO', db_default=False)),
                ('IdEjecucionEtapaSiguiente', models.BigIntegerField(db_column='IDEJECUCIONETAPASIGUIENTE')),
                ('IdEjecucionEtapaAnterior', models.BigIntegerField(db_column='IDEJECUCIONETAPAANTERIOR')),
                ('IdEtapa', models.ForeignKey(db_column='IDETAPA', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_etapa')),
                ('IdSolicitud', models.ForeignKey(db_column='IDSOLICITUD', on_delete=django.db.models.deletion.CASCADE, to='tramite.t_solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='r_solicitud_rol_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RolUsuario', models.PositiveSmallIntegerField(choices=[(0, 'Desconocido'), (1, 'Supervisión'), (2, 'Recepción'), (3, 'Inscripción'), (4, 'Certificación'), (5, 'Calificación'), (6, 'Jurídico'), (7, 'Externo autorizado'), (8, 'Auditoría')], db_column='ROLUSUARIO', db_default=0)),
                ('IdUsuario', models.ForeignKey(db_column='IDUSUARIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.usuario')),
                ('IdSolicitud', models.ForeignKey(db_column='IDSOLICITUD', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='r_requisito_solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FHVerificacion', models.BooleanField(db_column='FHVERIFICACION')),
                ('Estatus', models.PositiveSmallIntegerField(choices=[(0, 'No se ha cumplido'), (1, 'Entregado/cumple pero sin verificarse'), (2, 'Verificado')], db_default=0)),
                ('IdDocumento', models.ForeignKey(db_column='IDDOCUMENTO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.documento')),
                ('IdUsuarioVerificador', models.ForeignKey(db_column='IDUSUARIOVERIFICADOR', null=True, on_delete=django.db.models.deletion.CASCADE, to='adminusr.usuario')),
                ('IdRequisito', models.ForeignKey(db_column='IDREQUISITO', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_requisito')),
                ('IdSolicitud', models.ForeignKey(db_column='IDSOLICITUD', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='r_folio_no_inmobiliario_solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FolioReal', models.ForeignKey(db_column='FOLIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.folio_no_inmobiliario')),
                ('IdSolicitud', models.ForeignKey(db_column='IDSOLICITUD', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='r_folio_inmobiliario_solicitud',
            fields=[
                ('IdFolioSolicitud', models.BigAutoField(db_column='IDFOLIOSOLICITUD', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('FolioReal', models.ForeignKey(db_column='FOLIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.folio_inmobiliario')),
                ('IdSolicitud', models.ForeignKey(db_column='IDSOLICITUD', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='t_tramite',
            fields=[
                ('IdTramite', models.BigAutoField(db_column='IDTRAMITE', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(db_column='NOMBRE', db_index=True, help_text='Nombre del trámite (debe ser único)', max_length=100, verbose_name='Trámite')),
                ('Descripcion', models.TextField(db_column='DESCRIPCION', help_text='Descripción del trámite', verbose_name='Descripción')),
                ('Version', models.PositiveSmallIntegerField(db_column='VERSION', db_default=1, help_text='Versión del trámite', verbose_name='Versión')),
                ('Activo', models.BooleanField(db_column='ACTIVO', db_default=False, help_text='¿EStá activo?', verbose_name='Activo')),
                ('FundamentoLegal', models.TextField(db_column='FUNDAMENTO', help_text='Fundamento jurídico', verbose_name='Fundamento')),
                ('URLReferencia', models.URLField(db_column='URL', verbose_name='URL')),
                ('DatosAdicionales', models.JSONField(db_column='DATOSADICIONALES', help_text='Datos adicionales en formato JSon', verbose_name='Datos adicionales')),
                ('FHAlta', models.DateTimeField(db_column='FHALTA', default=datetime.datetime(2025, 2, 8, 1, 35, 37, 74251, tzinfo=datetime.timezone.utc), help_text='Fecha y hora del alta', verbose_name='Fecha y hora del alta')),
                ('FHModificacion', models.DateTimeField(db_column='FHMODIF', help_text='Fecha y hora de la última modificación', verbose_name='Fecha y hora de la última modificación')),
                ('IdTipoTramite', models.ForeignKey(db_column='IDTIPOTRAMITE', help_text='Tipo de trámite al que corresponde', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.c_tipo_tramite', verbose_name='Tipo de trámite')),
            ],
            options={
                'verbose_name_plural': 'Catálogo de trámites',
                'ordering': ('Nombre', 'Version', 'Activo'),
            },
        ),
        migrations.AddField(
            model_name='t_solicitud',
            name='IdTramite',
            field=models.ForeignKey(db_column='IDTRAMITE', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_tramite'),
        ),
        migrations.AddField(
            model_name='t_nodo_etapa',
            name='idTramite',
            field=models.ForeignKey(db_column='IDTRAMITE', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_tramite'),
        ),
        migrations.CreateModel(
            name='r_requisito_tramite',
            fields=[
                ('IdRequisitoTramite', models.BigAutoField(db_column='IDREQTRAMITE', db_index=True, primary_key=True, serialize=False, unique=True)),
                ('idRequisito', models.ForeignKey(db_column='IDREQUISITO', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_requisito')),
                ('idTramite', models.ForeignKey(db_column='IDTRAMITE', null=True, on_delete=django.db.models.deletion.CASCADE, to='tramite.t_tramite')),
            ],
        ),
    ]
