class LigaFutbol:
    def __init__(self):
        self._nombre_liga = ""

    def get_nombre_liga(self):
        return self._nombre_liga

    def set_nombre_liga(self, nombre_liga):
        self._nombre_liga = nombre_liga

    def mostrar_info_liga(self):
        return f"Liga: {self._nombre_liga}"
