# ====================================================================
# SISTEMA POKÉMON 
# ====================================================================

import random  
try:
    from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
except ImportError:
    print("\n[!] ERROR CRÍTICO: No se encontró el archivo 'pokedex.py'.")
    print("Asegúrese de que el archivo del profesor esté en la misma carpeta.")
    exit()


class Pokemon:
    """Clase base que define la estructura principal y el encapsulamiento."""

    def __init__(self, nombre, tipo, hp_max, ep_max):

        self.nombre = nombre
        self.tipo = tipo

        self.__hp_max = hp_max
        self.__ep_max = ep_max

        self.hp = hp_max
        self.ep = ep_max


    @property
    def hp(self):
       
        return self.__hp

    @hp.setter
    def hp(self, valor):
       
        if valor < 0:

            self.__hp = 0
        elif valor > self.__hp_max:
            self.__hp = self.__hp_max
        else:
            self.__hp = valor

    @property
    def ep(self):
       
        return self.__ep

    @ep.setter
    def ep(self, valor):
        
