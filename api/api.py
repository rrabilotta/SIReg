from ninja import Router, ModelSchema, Field, FilterSchema, Query
from django.urls import reverse
from django.utils.text import slugify
from catalogo.models import (
    c_moneda,
    c_pais,
    c_entidad,
    c_municipio,
    c_localidad,
    c_asentamiento_humano,
)
from django.shortcuts import get_object_or_404

router = Router()

@router.get("/version/")
def version(request):
    data = {"version": "0.0.1"}
    return data


class c_monedaSerializer(ModelSchema):
    class Meta:
        model = c_moneda
        fields = "__all__"


# Servicios generales de información


@router.get("/monedas/", response=list[c_monedaSerializer])
def monedas(request):
    return c_moneda.objects.all()


@router.get("/monedas/{clave_moneda}", response=c_monedaSerializer)
def moneda(request, clave_moneda):
    moneda = get_object_or_404(c_moneda, CveMoneda=clave_moneda)
    return moneda


class c_paisSeriaLizer(ModelSchema):
    class Meta:
        model = c_pais
        fields = "__all__"


@router.get("/paises/", response=list[c_paisSeriaLizer])
def paises(request):
    return c_pais.objects.filter(Moneda__isnull=False)


@router.get("/paises/{clave_pais}", response=c_paisSeriaLizer)
def pais(request, clave_pais):
    pais = get_object_or_404(c_pais, CvePais=clave_pais)
    return pais


class c_entidadSerializer(ModelSchema):
    class Meta:
        model = c_entidad
        fields = "__all__"


@router.get("/entidades/", response=list[c_entidadSerializer])
def entidades(request):
    return c_entidad.objects.filter(ClavePais__isnull=False)


@router.get("/entidades/{clave_entidad}", response=c_entidadSerializer)
def entidad(request, clave_entidad):
    entidad = get_object_or_404(c_entidad, CveGeograficaEntidad=clave_entidad)
    return entidad


class c_municipioSerializer(ModelSchema):
    class Meta:
        model = c_municipio
        fields = "__all__"


@router.get("/municipios/", response=list[c_municipioSerializer])
def municipios(request):
    return c_municipio.objects.filter(ClaveGeogEntidad__isnull=False)


@router.get("/municipios/{clave_municipio}", response=c_municipioSerializer)
def municipio(request, clave_municipio):
    municipio = get_object_or_404(c_municipio, CveGeograficaMunicipio=clave_municipio)
    return municipio


class c_localidadSerializer(ModelSchema):
    class Meta:
        model = c_localidad
        fields = "__all__"


@router.get("/localidades/", response=list[c_localidadSerializer])
def localidades(request):
    return c_localidad.objects.filter(ClaveGeogMunicipio__isnull=False)


@router.get("/localidades/{clave_localidad}", response=c_localidadSerializer)
def localidad(request, clave_localidad):
    localidad = get_object_or_404(c_localidad, CveGeograficaLocalidad=clave_localidad)
    return localidad


class c_asentamiento_humanoSerializer(ModelSchema):

    class Meta:
        model = c_asentamiento_humano
        fields = [
            "ClaveGeograficaAsentamiento",
            "Nombre",
            "CodigoPostal",
            "TipoAsentamiento",
            "ClaveAsentamiento",
            "ClaveGeogLocalidad",
        ]


@router.get(
    "/asentamientos/{clave_asentamiento}", response=c_asentamiento_humanoSerializer
)
def asentamiento(request, clave_asentamiento):
    asentamiento = get_object_or_404(
        c_asentamiento_humano, ClaveGeograficaAsentamiento=clave_asentamiento
    )
    return asentamiento
