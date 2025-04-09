class ValidadorFecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def es_bisiesto(self, anio):
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            return True
        else:
            return False

    def validar_fecha(self):
        try:
            d = int(self.dia)
            m = int(self.mes)
            a = int(self.anio)

            if m < 1 or m > 12:
                raise ValueError("Mes inválido")

            if m in [1, 3, 5, 7, 8, 10, 12]:
                if d < 1 or d > 31:
                    raise ValueError("Día inválido para este mes")
            elif m in [4, 6, 9, 11]:
                if d < 1 or d > 30:
                    raise ValueError("Día inválido para este mes")
            elif m == 2:
                if self.es_bisiesto(a):
                    if d < 1 or d > 29:
                        raise ValueError("Día inválido para febrero bisiesto")
                else:
                    if d < 1 or d > 28:
                        raise ValueError("Día inválido para febrero")

            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
        except:
            print("Error inesperado")
            return False


def main():
    print("VALIDACIÓN DE FECHAS")
    dia = input("Ingrese el día: ")
    mes = input("Ingrese el mes: ")
    anio = input("Ingrese el año: ")

    validador = ValidadorFecha(dia, mes, anio)

    if validador.validar_fecha():
        print("La fecha es válida")
    else:
        print("La fecha NO es válida")


if __name__ == "__main__":
    main()