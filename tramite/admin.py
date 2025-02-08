from django.contrib import admin
from tramite.models import (
    t_etapa,
    t_tramite,
    t_requisito,
    c_clase_tramite,
    c_tipo_tramite,
    c_aplicacion,
    c_modulo,
    c_tarifa,
    c_tipo_acto
)

# Register your models here.


# Modelos relativos a los trámites y solicitudes

class c_tarifaAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Tarifa", "Vigente")
    exclude = ("IdTarifa",)
    search_fields = ("Nombre", "Tarifa", "Descripcion", "Vigente")


admin.site.register(c_tarifa, c_tarifaAdmin)


class c_tipo_actoAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    exclude = ("IdTipoActo",)


admin.site.register(c_tipo_acto, c_tipo_actoAdmin)


class t_etapaAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion", "Activo")
    exclude = ("IdEtapa", "DatosAdicionales", "FHAlta", "FHModificacion")
    search_fields = ("Nombre", "Descripcion", "Activo")


admin.site.register(t_etapa, t_etapaAdmin)


class t_tramiteAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Version", "Descripcion", "Activo")
    exclude = ("IdTramite", "DatosAdicionales", "FHAlta", "FHModificacion")
    search_fields = ("Nombre", "Descripcion", "Version")


admin.site.register(t_tramite, t_tramiteAdmin)


class t_requisitoAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion", "Vigente")
    exclude = ("IdRequisito", "DatosAdicionales", "FHAlta", "FHModificacion")
    search_fields = ("Nombre", "Activo", "Descripcion")


admin.site.register(t_requisito, t_requisitoAdmin)


class c_clase_tramiteAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    exclude = ("IdClaseTramite",)
    search_fields = ("Nombre", "Descripcion")


admin.site.register(c_clase_tramite, c_clase_tramiteAdmin)


class c_tipo_tramiteAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "IdClaseTramite")
    excludo = ("IdTipoTramite",)
    search_fields = ("Nombre", "Descripcion")


admin.site.register(c_tipo_tramite, c_tipo_tramiteAdmin)


class c_aplicacionAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion", "DireccionRelativa")
    search_fields = ("Nombre", "Descripcion", "DireccionRelativa")
    exclude = ("DatosAdicionales", "FHAlta", "FHModificacion", "IdAplicacion")


admin.site.register(c_aplicacion, c_aplicacionAdmin)


class c_moduloAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion", "Modulo")
    search_fields = ("Nombre", "Descripcion", "Modulo")
    exclude = ("DatosAdicionales", "FHAlta", "FHModificacion", "IdModulo")


admin.site.register(c_modulo, c_moduloAdmin)


# ****************************************************************************
# Desactivar el orden alfabético
def get_app_list(self, request, app_label=None):
    """Return the installed apps that have been registered in admin.py"""
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    return app_list


admin.AdminSite.get_app_list = get_app_list
