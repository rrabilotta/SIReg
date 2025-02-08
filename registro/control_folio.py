from django.db import models
from django.utils.timezone import now
from sireg.settings import (
    CLAVE_ENTIDAD,
    PREFIJO_INMOBILIARIO,
    PREFIJO_NO_INMOBILIARIO,
)
from sireg.contantes import Const
from .models import (
    folio_inmobiliario,
    folio_no_inmobiliario,
    acto_inmobiliario,
    acto_no_inmobiliario,
    lista_negra_folios_inmobiliarios,
    lista_negra_folios_no_inmobiliarios,
)
from adminusr.models import c_area, c_oficina, usuario
from catalogo.models import c_asentamiento_humano


class control_folio:
    tipoFolio = 0  # 0=inmobiliario, otro valor no inmobiliario
    usuarioOperador: usuario
    Folio: str

    def __init__(self, tipo: int, usuarioOperador: usuario):
        self.tipoFolio = tipo
        self.usuarioOperador = usuarioOperador

    def _extraerParteNum(folio: str, posicion: int) -> int:
        strParteNum = folio[posicion:]
        if strParteNum.isnumeric():
            return int(strParteNum)
        else:
            return -1
        return 0

    def _encontrarEnListaNegra(folio: str, tipoFolio: int) -> bool:
        if tipoFolio == Const.TIPO_FOLIO_REAL(0):
            if lista_negra_folios_inmobiliarios.objects.get(FolioReal=folio):
                return True
        elif tipoFolio == Const.TIPO_FOLIO_REAL(1):
            if lista_negra_folios_no_inmobiliarios.objects.get(FolioReal=folio):
                return True
        else:
            return False
        return False

    def nuevoFolio(self) -> bool:

        if self.tipoFolio == 0:
            prefijoFolio = (
                PREFIJO_INMOBILIARIO
                + CLAVE_ENTIDAD
                + self.usuarioOperador.idOficina.prefijo_oficina
            )
            folios = folio_inmobiliario.objects.all()
        else:
            prefijoFolio = (
                PREFIJO_NO_INMOBILIARIO
                + CLAVE_ENTIDAD
                + self.usuarioOperador.idOficina.prefijo_oficina
            )
            folios = folio_no_inmobiliario.objects.all()

        if len(folios) > 0:
            ultimoFolio = folios.last()
            strParteNum = ultimoFolio.FolioReal[len(self.prefijoFolio) + 1 :]
            intParteNum = self._extraerParteNum(strParteNum, len(self.prefijoFolio) + 1)
            intParteNum += 1
        else:
            intParteNum = 1

        folioCandidato = f"{prefijoFolio}{intParteNum:0>9}"

        if self._encontrarEnListaNegra(folioCandidato, self.tipoFolio) == True:
            return False

        self.Folio = folioCandidato

        return True


class CaratulaInmobiliaria:
    """Clase que crea una carátula a través de una incersión
    de un registro nuevo en la entidad folio_inmobiliario

    Raises:
        Exception: Por no poder crear un nuevo folio real único
        o por error en crear el registro en folio_inmobiliario

    Returns:
        bool: Verdadero si crea la carátula, Falso sino.
    """

    __usuarioOperador: usuario
    __FolioReal: str
    __Caratula: folio_inmobiliario = None

    def __init__(self, usuarioOperador: usuario):
        self.__usuarioOperador = usuarioOperador

    def Crear(
        self,
        claveCatastral: str = None,
        folioMatriz: str = None,
        folioCondominio: str = None,
        nombreInmueble: str = None,
        descripcion: str = None,
        observaciones: str = None,
        esFolioMatriz: bool = False,
        esCondominio: bool = False,
        superficieIndiviso: float = 0.0,
        superficieSuelo: float = 0.0,
        superficieConstruccion: float = 0.0,
        ambito: int = 0,
        vialidad: str = None,
        tipoVialidad: int = 0,
        numeroExterior: str = None,
        numeroInterior: str = None,
        km: str = None,
        manzana: str = None,
        lote: str = None,
        claveGeogAsentamiento: str = None,
    ) -> bool:
        """Crea una carátula.

        Args:
            claveCatastral (str): Clave catastral. Defaults to None.
            folioMatriz (str, optional): Folio matriz que le da origen. Defaults to None.
            folioCondominio (str, optional): Folio del condominio al que pertence. Defaults to None.
            nombreInmueble (str, optional): Nombre del inmueble. Defaults to None.
            descripcion (str, optional): Descripción del inmueble. Defaults to None.
            observaciones (str, optional): Observaciones del registrador. Defaults to None.
            esFolioMatriz (bool, optional): Verdadero si es folio matriz de otro(s) inmueble(s). Defaults to False.
            esCondominio (bool, optional): Verdadero si es el inmueble pivote de un condominio. Defaults to False.
            superficieIndiviso (float, optional): Superficie indiviso (área común). Defaults to 0.0.
            superficieSuelo (float, optional): Superficie del suelo. Defaults to 0.0.
            superficieConstruccion (float, optional): Superficie de construcción. Defaults to 0.0.
            ambito (int, optional): 0=Urbano, 1=Rústico, 2=Rural. Defaults to 0.
            vialidad (str, optional): Nombre de la vialidad. Defaults to None.
            tipoVialidad (int, optional): Tipo de vialidad (ver Const). Defaults to 0.
            numeroExterior (str, optional): Número exterior. Defaults to None.
            numeroInterior (str, optional): Número interior. Defaults to None.
            km (str, optional): Kilómetro. Defaults to None.
            manzana (str, optional): Manzana. Defaults to None.
            lote (str, optional): Lote. Defaults to None.
            claveGeogAsentamiento (str, optional): Clave geográfica del asentamiento. Defaults to None.

        Raises:
            Exception: Cuando no puede crear el folio o crear un nuevo registro.

        Returns:
            bool: Verdadero si la carátula es creada o falsa si no.
        """
        ControlFolio = control_folio(self.__usuarioOperador)
        if ControlFolio.nuevoFolio() == True:
            self.__FolioReal = ControlFolio.Folio
        else:
            raise Exception(f"Error: No puedo crear nuevo nuevo folio")
        NuevaCaratula = folio_inmobiliario.objects.create()
        NuevaCaratula.FolioReal = self.__FolioReal
        NuevaCaratula.ClaveCatastral = claveCatastral
        if folioMatriz:
            NuevaCaratula.FolioMatriz = str(folioMatriz).strip()
        if folioCondominio:
            NuevaCaratula.FolioCondominio = str(folioCondominio).strip()
        if nombreInmueble:
            NuevaCaratula.NombreInmueble = str(nombreInmueble).upper()
        else:
            NuevaCaratula.NombreInmueble = "S/N"
        if descripcion:
            NuevaCaratula.Descripcion = str(descripcion).upper().strip()
        else:
            NuevaCaratula.Descripcion = "S/D"
        if observaciones:
            NuevaCaratula.Observaciones = str(observaciones).upper().strip()
        else:
            NuevaCaratula.Observaciones = "S/O"
        NuevaCaratula.EsFolioMatriz = esFolioMatriz
        NuevaCaratula.EsCondominio = esCondominio
        NuevaCaratula.SuperficieIndiviso = superficieIndiviso
        NuevaCaratula.SuperficieSuelo = superficieSuelo
        NuevaCaratula.SuperficieConstruccion = superficieConstruccion
        NuevaCaratula.Ambito = ambito
        if vialidad:
            NuevaCaratula.Vialidad = vialidad.upper().strip()
        else:
            NuevaCaratula.Vialidad = "S/N"
        NuevaCaratula.TipoVialidad = tipoVialidad
        NuevaCaratula.NumeroExterior = numeroExterior
        NuevaCaratula.NumeroInterior = numeroInterior
        NuevaCaratula.Km = km
        NuevaCaratula.Manzana = manzana
        NuevaCaratula.Lote = lote
        if claveGeogAsentamiento:
            asentamiento = c_asentamiento_humano.objects.get(
                ClaveGeograficaAsentamiento=claveGeogAsentamiento
            )
            if asentamiento.DoesNotExist() == False:
                NuevaCaratula.ClaveGeoAsentamiento = (
                    asentamiento.ClaveGeograficaAsentamiento
                )
            else:
                NuevaCaratula.ClaveGeoAsentamiento = None
        else:
            NuevaCaratula.ClaveGeoAsentamiento = None
        try:
            NuevaCaratula.save()
        except Exception:
            raise (f"Error: {Exception.__str__}")
        finally:
            self.__Caratula = NuevaCaratula
        return True

    def FolioReal(self):
        if self.__Caratula != None:
            return str(self.__Caratula.FolioReal)
        else:
            return None

    def ActualizarFolioMatriz(self, folioMatriz: str = None) -> bool:
        if self.__Caratula == None:
            return False
        if folioMatriz == None:
            self.__Caratula.FolioMatriz = None
        else:
            self.__Caratula.FolioMatriz = folioMatriz
        try:
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True

    def ActualizarFolioCondominio(self, folioCondominio: str = None) -> bool:
        if self.__Caratula == None:
            return False
        if folioCondominio == None:
            self.__Caratula.FolioCondominio = None
        else:
            self.__Caratula.FolioCondominio = folioCondominio
        try:
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True

    def ActualizarCoordenadas(
        self, latitud: float = 0.00, longitud: float = 0.00
    ) -> bool:
        """Actualiza los campos Latitud y Longitud de la
        carátula.
        Valores no pueden ser nulos, valor para ignorarlos es 0.00 para
        ambos.

        Args:
            latitud (float, optional): Latitud. Defaults to 0.00.
            longitud (float, optional): Longitud. Defaults to 0.00.

        Returns:
            bool: Verdadero si las coordenadas se actualizaron
        """
        if self.__Caratula == None:
            return False
        self.__Caratula.Latitud = latitud
        self.__Caratula.Longitud = longitud
        try:
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True

    def ActualizarNombre(self, nombre: str = None) -> bool:
        if self.__Caratula == None:
            return False
        if nombre != None:
            self.__Caratula.NombreInmueble = nombre
        else:
            return False
        try:
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True

    def ActualizarDescripcion(self, descripcion: str = None) -> bool:
        if self.__Caratula == None:
            return False
        if descripcion != None:
            self.__Caratula.Descripcion = descripcion
        else:
            self.__Caratula.Descripcion = None
        try:
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True

    def CancelarFolio(
        self,
        cancelacion: bool = False,
        folioProdujoCancelacion: str = None,
        folioActoProdujoCancelacion: str = None,
    ) -> bool:
        """Cancela o revierte la cancelación de un folio real inmobiliario
            Uso:
            obj.CancelarFolio(False,None,None) para revertir
            obj.CancelarFolio(True, FolioInmueble, FolioActo) para cancelar el folio

        Args:
            cancelacion (bool, optional): Verdadero para cancelar,
            Falso para revertir. Defaults to False.
            folioProdujoCancelacion (str, optional):
            Folio que produjo la cancelación. Defaults to None.
            folioActoProdujoCancelacion (str, optional):
            Acto que produjo la cancelación. Defaults to None.

        Returns:
            bool: Verdadero si la cancelación o su reversión fue exitosa.
        """
        if self.__Caratula == None:
            return False
        if cancelacion == True and (
            folioProdujoCancelacion == None or folioActoProdujoCancelacion == None
        ):
            return False
        if cancelacion == False:
            self.__Caratula.FolioCancelado = False
            self.__Caratula.FolioProdCancelacion = None
            self.__Caratula.FolioActoProdCancelacion = None
        else:
            if folioProdujoCancelacion != None and folioActoProdujoCancelacion != None:
                self.__Caratula.FolioCancelado = True
                self.__Caratula.FolioProdCancelacion = folioProdujoCancelacion
                self.__Caratula.FolioActoProdCancelacion = folioActoProdujoCancelacion
            else:
                return False
        try:
            self.__Caratula.FHCancelacion = now()
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True

    def ActualizarSuperficies(
        self,
        superficieSuelo: float = None,
        superficieConstruccion: float = None,
        superficieIndiviso: float = None,
    ) -> bool:
        if self.__Caratula == None:
            return False
        if superficieSuelo != None:
            if superficieSuelo > 0.00:
                self.__Caratula.SuperficieSuelo = superficieSuelo
            else:
                return False
        if superficieConstruccion != None:
            if superficieConstruccion >= 0:
                self.__Caratula.SuperficieConstruccion = superficieConstruccion
            else:
                return False
        if superficieIndiviso != None:
            if superficieIndiviso >= 0:
                self.__Caratula.SuperficieIndiviso = superficieIndiviso
            else:
                return False
        try:
            self.__Caratula.FHModificacion = now()
            self.__Caratula.objects.update()
        except Exception:
            raise (f"Error: {Exception.__str__()}")
        return True
