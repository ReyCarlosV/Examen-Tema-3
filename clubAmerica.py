from equipo import Equipo
from televisa import Televisa

class ClubAmerica(Equipo, Televisa):
    def __init__(self):
        Equipo.__init__(self)
        Televisa.__init__(self)
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

    def mostrar_info_club_america(self):
        info_equipo = Equipo.mostrar_info_equipo(self)
        info_televisa = Televisa.mostrar_info_televisa(self)
        return f"{info_televisa}, {info_equipo}, Estadio: {self._estadio}, Ciudad: {self._ciudad}"
