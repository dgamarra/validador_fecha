class FechaError(Exception):
    def __init__(self, mensaje="Error en la fecha inválida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MesInvalidoError(FechaError):
    def __init__(self, mensaje="Error en mes inválido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DiaInvalidoError(FechaError):
    def __init__(self, mensaje="Error el día inválido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ValidadorFecha:
    def __init__(self, dia: int, mes: int, anio: int):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def es_bisiesto(self) -> bool:
        """Determina si el año es bisiesto"""
        pass

    def validar_mes(self) -> bool:
        """Valida que el mes esté entre 1 y 12"""
        pass

    def validar_dia(self) -> bool:
        """Valida el día según el mes y año"""
        pass

    def validar_fecha(self) -> bool:
        """Orquesta la validación completa"""
        pass