from equipo import Equipo
from pumas import Pumas
from clubAmerica import ClubAmerica

class CruzAzul(Equipo):
    def __init__(self):
        super().__init__()
        self._estadio = ""
        self._ciudad = ""
        self._contrincante_uno = ""
        self._contrincante_dos = ""

    def get_nombre_estadio(self):
        return self._estadio

    def set_nombre_estadio(self, estadio):
        self._estadio = estadio

    def get_ciudad(self):
        return self._ciudad

    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

    def get_contrincante(self):
        return self._contrincante_uno

    def set_contrincante(self):
        self._contrincante_uno = Pumas().get_nombre_equipo()

    def get_contrincante_dos(self):
        return self._contrincante_dos

    def set_contrincante_dos(self):
        self._contrincante_dos = ClubAmerica().get_nombre_equipo()

    def mostrar_info_cruz_azul(self):
        info_equipo = super().mostrar_info_equipo()
        return f"{info_equipo}, Estado: {self._estadio}, Ciudad: {self._ciudad} 1er Partido: {self._nombre_equipo} VS {self._contrincante_uno}, 2do Partido: {self._nombre_equipo} VS {self._contrincante_dos}"
