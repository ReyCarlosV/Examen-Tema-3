from clubAmerica import ClubAmerica

class FuerzasBasicas(ClubAmerica):
    def __init__(self):
        super().__init__()
        self._nombre_director = ""
        self._jovenes_promesas = 0

    def get_nombre_entrenador(self):
        return self._nombre_director

    # Setter para nombre_director
    def set_nombre_director(self, nombre_director):
        self._nombre_director = nombre_director

    def get_jovenes_promesas(self):
        return self._jovenes_promesas

    def set_jovenes_promesas(self, jovenes_promesas):
        self._jovenes_promesas = jovenes_promesas

    def mostrar_info_fuerzas_basicas(self):
        info_club_america = super().mostrar_info_club_america()
        return f"{info_club_america}, Director: {self._nombre_director}, Promesas: {self._jovenes_promesas}"
