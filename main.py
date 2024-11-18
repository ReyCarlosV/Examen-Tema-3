from pumas import Pumas
from cruzAzul import CruzAzul
from fuerzasBasicas import FuerzasBasicas

def main():
    pumas = Pumas()
    pumas.set_nombre_liga("LigaMx")
    pumas.set_nombre_equipo("Pumas")
    pumas.set_valor_equipo(44.75)
    pumas.set_nombre_estadio("Olimpico Universitario")
    pumas.set_ciudad("Ciudad de Mexico")

    fuerzas_basicas = FuerzasBasicas()
    fuerzas_basicas.set_nombre_liga("LigaMx")
    fuerzas_basicas.set_nombre_equipo("Club America")
    fuerzas_basicas.set_valor_equipo(83.6)
    fuerzas_basicas.set_nombre_estadio("Azteca")
    fuerzas_basicas.set_ciudad("Ciudad de Mexico")
    fuerzas_basicas.set_empresa("Televisa")
    fuerzas_basicas.set_dueno("Emilio Azcarraga")
    fuerzas_basicas.set_nombre_director("Raul Herrera")
    fuerzas_basicas.set_jovenes_promesas("2")

    cruz_azul = CruzAzul()
    cruz_azul.set_nombre_liga("LigaMx")
    cruz_azul.set_nombre_equipo("Cruz Azul")
    cruz_azul.set_valor_equipo(47.80)
    cruz_azul.set_nombre_estadio("Ciudad de los Deportes")
    cruz_azul.set_ciudad("Ciudad de Mexico")
    cruz_azul.set_contrincante_uno(pumas.get_nombre_equipo())
    cruz_azul.set_contrincante_dos(fuerzas_basicas.get_nombre_equipo())

    print("Pumas:")
    print(pumas.mostrar_info_pumas())

    print("\nCruz Azul:")
    print(cruz_azul.mostrar_info_cruz_azul())

    print("\nFuerzas Basicas del America:")
    print(fuerzas_basicas.mostrar_info_fuerzas_basicas())

if __name__ == "__main__":
    main()
