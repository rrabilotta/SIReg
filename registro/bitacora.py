import json
from adminusr.models import usuario


class bitacora:
    OPERACIONES = ((0, "Alta"), (1, "Cambio"), (2, "Baja"))

    def __init__(self):
        pass

    def diccionarioAJSon(diccionario) -> str:
        if not diccionario == None:
            return None
        else:
            return json.dump(diccionario, indent=4)

    def mensaje(
        self,
        idOperacion: int = 0,
        operacion: str = None,
        estatusAnterior: str = None,
        estatusPosterior: str = None,
    ) -> str:

        if operacion == None or idOperacion < 0 or idOperacion > 2:
            return None
        texto = self.OPERACIONES[idOperacion]
        if estatusAnterior != None:
            texto += ", " + json.dumps(estatusAnterior, indent=4)
        if estatusPosterior != None:
            texto += ", " + json.dumps(estatusPosterior, indent=4)
        return texto

    def operacion(
        self, modulo: str, usuarioInterno: usuario, operacion: str, descripcion: str
    ) -> dict:
        dictOperacion = {}
        if modulo == None:
            return None
        dictOperacion["MODULO"] = modulo
        if usuarioInterno == None:
            return None
        dictOperacion["USUARIO"] = (
            f"({usuarioInterno.IdUsuario}) {usuarioInterno.Nombre}.{usuarioInterno.PrimerApellido} {usuarioInterno.SegundoApellido}"
        )
        if operacion == None:
            return None
        dictOperacion["OPERACION"] = operacion
        if descripcion == None:
            return None
        dictOperacion["DESCRIPCION"] = descripcion
        return dictOperacion

    def estadoOriginal(self, entidad: str, camposValores: tuple) -> dict:
        dictEstadoOriginal = {}
        if entidad == None or camposValores == None:
            return None
        dictEstadoOriginal["ENTIDAD"] = entidad
        for Par in camposValores:
            dictEstadoOriginal[str(Par(0)).upper()] = str(Par(1))
        return dictEstadoOriginal

    def estadoFinal(self, entidad: str, camposValores: tuple) -> dict:
        dictEstadoOriginal = {}
        if entidad == None or camposValores == None:
            return None
        dictEstadoOriginal["ENTIDAD"] = entidad
        for Par in camposValores:
            dictEstadoOriginal[str(Par(0)).upper()] = str(Par(1))
        return dictEstadoOriginal
