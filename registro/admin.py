from django.contrib import admin
from registro.models import (
    c_interes_juridico,
    c_tipo_instrumento,
    instrumento,
)


class c_interes_juridicosAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    exclude = ("IdInteresJuridico",)
    search_fields = ("Nombre",)


admin.site.register(c_interes_juridico, c_interes_juridicosAdmin)


class instrumentoAdmin(admin.ModelAdmin):
    list_display = (
        "Nombre",
        "Descripcion",
        "FechaInstrumento",
        "FHAlta",
        "IdFedFun",
        "IdDocumento",
    )
    search_fields = ("Nombre", "Descripcion", "Extracto", "FechaInstrumento", "FHAlta")
    exclude = ("FHAlta", "FHModificacion", "IdInstrumento")


admin.site.register(instrumento, instrumentoAdmin)


class c_tipo_instrumentoAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion", "Emisor")
    search_fields = ("Nombre", "Descripcion", "Emisor")
    exclude = ("IdTipoInstrumento",)


admin.site.register(c_tipo_instrumento, c_tipo_instrumentoAdmin)



# ****************************************************************************
# Desactivar el orden alfabético
def get_app_list(self, request, app_label=None):
    """Return the installed apps that have been registered in admin.py"""
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    return app_list


admin.AdminSite.get_app_list = get_app_list
