from ligaFutbol import LigaFutbol

class Equipo(LigaFutbol):
    def __init__(self):
        super().__init__()
        self._nombre_equipo = ""
        self._valor_equipo = 0

    def get_nombre_equipo(self):
        return self._nombre_equipo

    def set_nombre_equipo(self, nombre_equipo):
        self._nombre_equipo = nombre_equipo

    def get_valor_equipo(self):
        return self._valor_equipo

    def set_valor_equipo(self, valor_equipo):
        self._valor_equipo = valor_equipo

    def mostrar_info_equipo(self):
        info_liga = super().mostrar_info_liga()
        return f"{info_liga}, Equipo: {self._nombre_equipo}, Valor: ${self._valor_equipo}mdd"
