from django.contrib import admin
from adminusr.models import usuario, c_dependencia, c_area, c_oficina

# Register your models here.


class usuarioAdmin(admin.ModelAdmin):
    list_display = (
        "Nombre",
        "PrimerApellido",
        "SegundoApellido",
        "Cargo",
        "CURP",
        "RFC",
    )
    search_fields = (
        "Nombre",
        "PrimerApellido",
        "SegundoApellido",
        "Cargo",
        "CURP",
        "RFC",
    )
    exclude = ("IdUsuario", "FHAlta", "FHModificacion")


admin.site.register(usuario, usuarioAdmin)


class c_dependenciaAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "NivelGobierno", "Poder")
    search_fields = ("Nombre", "NombreAnterior", "NivelGobierno", "Poder")
    exclude = ("IdDependencia",)


admin.site.register(c_dependencia, c_dependenciaAdmin)


class c_areaAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    search_fields = ("Nombre",)
    exclude = ("IdArea",)


admin.site.register(c_area, c_areaAdmin)


class c_oficinaAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Descripcion")
    exclude = ("IdOficina",)


admin.site.register(c_oficina, c_oficinaAdmin)


# ****************************************************************************
# Desactivar el orden alfabético
def get_app_list(self, request, app_label=None):
    """Return the installed apps that have been registered in admin.py"""
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    return app_list


admin.AdminSite.get_app_list = get_app_list
