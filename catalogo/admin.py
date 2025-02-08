from django.contrib import admin
from catalogo.models import (
    c_clase_reporte,
    c_regimen_fiscal,
    c_uso_cdfi,
    c_tipo_recibo,
    c_moneda,
    c_nombre_vialidad,
    c_clase_documento,
    c_tipo_documento_identidad,
    c_asentamiento_humano,
    c_pais,
    c_entidad,
    c_localidad,
    c_municipio,
)

# Register your models here.




class c_clase_reporteAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    exclude = ("IdClaseReporte",)
    search_fields = ("Nombre", "Descripcion")


admin.site.register(c_clase_reporte, c_clase_reporteAdmin)


class c_tipo_reciboAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    exclude = ("IdTipoRecibo",)
    search_fields = ("Nombre", "Descripcion")


admin.site.register(c_tipo_recibo, c_tipo_reciboAdmin)


class c_regimen_fiscalAdmin(admin.ModelAdmin):
    list_display = ("ClaveSAT", "Nombre", "Descripcion", "PersonaMoral")
    exlude = ("IdRegimenFiscal",)
    search_fields = ("ClaveSAT", "Nombre", "Descripcion", "PersonaMoral")


admin.site.register(c_regimen_fiscal, c_regimen_fiscalAdmin)


class c_uso_cdfiAdmin(admin.ModelAdmin):
    list_display = (
        "ClaveSAT",
        "Nombre",
        "Descripcion",
        "PersonaFisica",
        "PersonaMoral",
    )
    exclude = ("IdUsoCDFI",)
    search_fields = (
        "ClaveSAT",
        "Nombre",
        "Descripcion",
        "PersonaFisica",
        "PersonaMoral",
    )


admin.site.register(c_uso_cdfi, c_uso_cdfiAdmin)


class c_monedaAdmin(admin.ModelAdmin):
    list_display = ("CveMoneda", "Moneda")
    search_fields = ("CveMoneda", "Moneda")


admin.site.register(c_moneda, c_monedaAdmin)


class c_nombre_vialidadAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Aliases")
    search_fields = ("Nombre", "Aliases")
    exclude = ("IdNombreVialidad",)


admin.site.register(c_nombre_vialidad, c_nombre_vialidadAdmin)


# Modelos relativos al manejo de documentos


class c_clase_documentoAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Expira", "Oficial")
    search_fields = ("Nombre",)
    exclude = ("IdClaseDocumento",)


admin.site.register(c_clase_documento, c_clase_documentoAdmin)


class c_tipo_documento_identidadAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Expira")
    search_fields = ("Nombre",)
    exclude = ("IdTipoDocumentoIdentidad",)


admin.site.register(c_tipo_documento_identidad, c_tipo_documento_identidadAdmin)


class c_paisAdmin(admin.ModelAdmin):
    list_display = ("CvePais", "Nombre")
    search_fields = ("Nombre", "CvePais")


admin.site.register(c_pais, c_paisAdmin)


class c_entidadAdmin(admin.ModelAdmin):
    list_display = ("CveGeograficaEntidad", "Nombre")
    search_fields = ("Nombre",)


admin.site.register(c_entidad, c_entidadAdmin)


class c_munificioAdmin(admin.ModelAdmin):
    list_display = ("CveGeograficaMunicipio", "Nombre")
    search_fields = ("Nombre",)


admin.site.register(c_municipio, c_munificioAdmin)


class c_localidadAdmin(admin.ModelAdmin):
    list_display = ("CveGeograficaLocalidad", "Nombre")
    search_fields = ("Nombre",)


admin.site.register(c_localidad, c_localidadAdmin)


class c_asentamiento_humanoAdmin(admin.ModelAdmin):
    list_display = ("ClaveGeograficaAsentamiento", "Nombre", "CodigoPostal")
    search_fields = ("Nombre", "CodigoPostal")


admin.site.register(c_asentamiento_humano, c_asentamiento_humanoAdmin)


# ****************************************************************************
# Desactivar el orden alfabético
def get_app_list(self, request, app_label=None):
    """Return the installed apps that have been registered in admin.py"""
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    return app_list


admin.AdminSite.get_app_list = get_app_list
