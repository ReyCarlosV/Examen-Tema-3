class Televisa:
    def __init__(self):
        self._empresa = ""
        self._dueno = ""

    def get_empresa(self):
        return self._empresa

    def set_empresa(self, empresa):
        self._empresa = empresa

    def get_dueno(self):
        return self._dueno

    def set_dueno(self, dueno):
        self._dueno = dueno

    def mostrar_info_televisa(self):
        return f"Empresa: {self._empresa}, Dueño: {self._dueno}"
