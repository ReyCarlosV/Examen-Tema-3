from equipo import Equipo

class Pumas(Equipo):
    def __init__(self):
        super().__init__()
        self._estadio = ""
        self._ciudad = ""

    def get_nombre_estadio(self):
        return self._estadio

    def set_nombre_estadio(self, estadio):
        self._estadio = estadio

    def get_ciudad(self):
        return self._ciudad

    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

    def mostrar_info_pumas(self):
        info_equipo = super().mostrar_info_equipo()
        return f"{info_equipo}, Estado: {self._estadio}, Ciudad: {self._ciudad}"
