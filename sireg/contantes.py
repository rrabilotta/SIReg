class Const:
    CAUSA_LISTA_NEGRA_FOLIO = (
        (0, "No se puede determinar"),
        (1, "Por cancelación"),
        (2, "Por error material"),
        (3, "Por error inmaterial"),
        (4, "Por orden judicial"),
        (5, "Por error sistemático"),
    )

    TIPO_RELACION = (
        (0, "Desconocido"),
        (1, "Lugar de emisión"),
        (2, "Lugar de registro"),
    )

    TIPO_VIALIDAD = (
        (0, "Calle"),
        (1, "Avenida"),
        (2, "Periférico"),
        (3, "Cerrada"),
        (4, "Calzada"),
        (5, "Eje vial"),
        (6, "Privada"),
        (7, "Circuito"),
        (8, "Viaducto"),
        (9, "Pasaje"),
        (10, "Peatonal"),
        (11, "Continuación"),
        (12, "Callejón"),
        (13, "Corredor"),
        (14, "Prolongación"),
        (15, "Andador"),
        (16, "Carretera"),
        (17, "Boulevard"),
        (18, "Ampliación"),
        (19, "Circunvalación"),
        (20, "Glorieta"),
        (21, "Carretera"),
        (22, "Retorno"),
        (23, "Enlace"),
        (24, "Vereda"),
        (25, "Diagonal"),
        (26, "Retorno U"),
        (27, "Rampa de frenado"),
        (28, "Otro"),
    )
    
    ESTATUS_TRAMITE = (
        (0, "No iniciado"),
        (1, "Recibido"),
        (2, "En proceso"),
        (3, "Rechazado"),
        (4, "Resuelto"),
        (5, "Entregado"),
        (98, "Cancelado"),
        (99, "Finalizado"),
    )
    
    NIVEL_URGENCIA = (
        (0, "Normal"), 
        (1, "Urgente"), 
        (2, "Muy urgente")
    )
    
    UBICACION_VIALIDAD = (
        (0, "Vialidad"), 
        (1, "Entrecalle"), 
        (2, "Calle trasera")
    )
    
    EMISOR_INSTRUMENTO = (
        (0, "Notario"),
        (1, "Corredor Público"),
        (2, "Poder judicial"),
        (3, "Fiscalía"),
        (4, "Poder ejecutivo"),
        (5, "Poder legislativo"),
        (6, "Notario y/o Corredor Público"),
        (7, "Autoridad en el extranjero"),
    )
    
    TIPO_CAMPO = (
        (0, "Sin definir"),
        (1, "Int"),
        (2, "Text"),
        (3, "Date"),
        (4, "Date-time"),
        (5, "URL"),
        (6, "Email"),
        (7, "Currency"),
        (8, "Geometry"),
        (9, "Name-field"),
        (10, "Password-field"),
    )
    
    NIVEL_GOBIERNO = (
        (0, "Sin determinar"),
        (1, "Municipal"),
        (2, "Estatal o provincial"),
        (3, "Federal o nacional"),
        (4, "Gobierno extranjero"),
    )
    
    PODER = (
        (0, "Sin determinar"),
        (1, "Ejecutivo"),
        (2, "Legislativo"),
        (3, "Judicial"),
        (4, "Electoral"),
        (5, "Otro"),
    )
    
    TIPO_FEDATARIO_FUNCIONARIO = (
        (0, "Notario"),
        (1, "Corredor Público"),
        (2, "Juez"),
        (3, "Funcionario municipal"),
        (4, "Funcionario estatal"),
        (5, "Funcionario federal"),
        (6, "Funcionario extranjero"),
    )
    
    FORMATO_DOCUMENTOS = (
        (0, "Desconocido"),
        (1, "PDF"),
        (2, "DOC (Word)"),
        (3, "DOCX (Word)"),
        (4, "XLS (Excel)"),
        (5, "XLSX (Excel)"),
        (6, "TXT"),
        (7, "CSV"),
        (8, "PNG"),
        (9, "JPEG"),
        (10, "TIFF"),
    )
    
    ROL_USUARIO_DOCUMENTO = (
        (0, "Desconocido"),
        (1, "Carga"),
        (2, "Digitalización"),
        (3, "Verificación"),
        (4, "Cotejo"),
        (5, "Auditoría"),
    )
    
    TIPO_ENTRADA_BITACORA = (
        (0, "General"),
        (1, "Advertencia"),
        (2, "Error"),
        (3, "Operación"),
        (4, "Modificación"),
        (5, "Alta"),
        (6, "Baja"),
    )
    
    ESTADO_CIVIL = (
        (0, "Soltero(a)"),
        (1, "Casado(a)"),
        (2, "Divorciado(s)"),
        (3, "Viudo(a)"),
    )
    
    REGIMEN_MATRIMONIAL = (
        (0, "Sin definir"),
        (1, "Bienes mancomunados"),
        (2, "Bienes separados"),
    )
    
    TIPO_PERSONA = (
        (0, "Persona física"), 
        (1, "Persona moral")
    )
    
    AMBITO = (
        (0, "Urbano"), 
        (1, "Rural"), 
        (2, "Suburbano"), 
        (3, "Rústico")
    )
    
    METODO_INMATRICULACION = (
        (0, "Inmatriculación"),
        (1, "Inmatriculación judicial"),
        (2, "Pase a folio"),
        (3, "Por fusión"),
        (4, "Por subdivisión"),
    )
    
    LADO = (
        (0, "Norte"),
        (1, "Sur"),
        (2, "Oriente (Este)"),
        (3, "Poniente (Oeste)"),
        (4, "Norte-Poniente"),
        (5, "Sur-Poniente"),
        (6, "Norte-oriente"),
        (7, "Sur-oriente"),
    )
    
    METODO_PAGO = (
        (0, "Sin determinar"),
        (1, "Efectivo"),
        (2, "Tarjeta de débito"),
        (3, "Tarjeta de creédito"),
    )
    
    ROL_USUARIO = (
        (0, "Desconocido"),
        (1, "Supervisión"),
        (2, "Recepción"),
        (3, "Inscripción"),
        (4, "Certificación"),
        (5, "Calificación"),
        (6, "Jurídico"),
        (7, "Externo autorizado"),
        (8, "Auditoría"),
    )
    
    SENTIDO = (
        (0, "Actual"),
        (1, "Anterior"),
        (2, "Siguiente"),
        (3, "Error"),
        (4, "Final"),
    )
    
    ROL_USUARIO_MODULO = (
        (0, "Deconocido"),
        (1, "Inicio"),
        (2, "Reinicio"),
        (3, "Suspensión"),
    )
    
    ROL_INSTRUMENTO = (
        (0, "Desconocido"),
        (1, "Inscripción"),
        (2, "Cancelación"),
        (3, "Corrección de error material"),
        (4, "Orden judicial"),
    )
    
    TIPO_INMATRICULACION = (
        (0, "Inmatriculación"),
        (1, "Inmatriculación judicial"),
        (2, "Pase a folio real"),
        (3, "Por subdivisión"),
        (4, "Por fusión"),
    )
    
    ROL_USUARIO_FOLIO_INMOBILIARIO = (
        (0, "Desconocido"),
        (1, "Capturista"),
        (2, "Registrador"),
        (3, "Supervisor"),
        (4, "Legal"),
    )
    
    ESCALA_TIEMPO = (
        (0, "Años"), 
        (1, "Años"), 
        (2, "Semanas"), 
        (3, "Días")
    )
    
    ESTATUS_REQUISITO_SOLICITUD = (
        (0, "No se ha cumplido"),
        (1, "Entregado/cumple pero sin verificarse"),
        (2, "Verificado"),
    )
    
    ROL_PARTICIPANTE = (
        (0, "Sin definir"),
        (1, "Enajenante"),
        (2, "Adquiriente"),
        (3, "Acreedor"),
        (4, "Adquiriente"),
        (5, "Deudor"),
        (6, "Garante"),
        (7, "Cedente"),
        (8, "Cesionario"),
        (9, "Usufructuario"),
        (10, "Demandante"),
    )

    TIPO_FOLIO_REAL = (
        (0, "Folio real inmobiliario"),
        (1, "Folio real no inmobiliario"),
        (2, "Folio real mercantil"),
        (3, "Folio real registro civil"),
    )

    TIPO_NUMERACION_INMUEBLE = (
        (0, "Número exterior - interior"),
        (1, "Km"),
        (2, "Manzana - lote"),
        (3, "Edificio - departamento"),
        (4, "Privada - casa"),
        (5, "Unidad - edificio - departamento"),
    )
