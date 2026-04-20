#==========================================================================================================
# ====================================================================
# ARCHIVO PROVISTO POR EL PROFESOR: pokedex.py
# ====================================================================
# Este archivo simula una base de datos. Contiene la información en crudo
# de los Pokémon disponibles. Usted debe importar este catálogo en su main.py
# y utilizar estos datos para instanciar sus objetos.
# ====================================================================

CATALOGO_POKEMON = {
    "1": {"tipo": "Fuego", "nombre": "Charmander", "hp_maximo": 100, "energia_maxima": 50},
    "2": {"tipo": "Fuego", "nombre": "Vulpix", "hp_maximo": 90, "energia_maxima": 60},
    "3": {"tipo": "Agua", "nombre": "Squirtle", "hp_maximo": 110, "energia_maxima": 45},
    "4": {"tipo": "Agua", "nombre": "Psyduck", "hp_maximo": 95, "energia_maxima": 55},
    "5": {"tipo": "Planta", "nombre": "Bulbasaur", "hp_maximo": 105, "energia_maxima": 50},
    "6": {"tipo": "Planta", "nombre": "Oddish", "hp_maximo": 90, "energia_maxima": 60},
    "7": {"tipo": "Electrico", "nombre": "Pikachu", "hp_maximo": 80, "energia_maxima": 70},
    "8": {"tipo": "Electrico", "nombre": "Magnemite", "hp_maximo": 75, "energia_maxima": 80}
}

def mostrar_catalogo_disponible():
    """
    Imprime en la consola el catálogo de Pokémon disponibles de forma tabulada.
    """
    print("\n" + "="*45)
    print("         CATÁLOGO POKÉMON OFICIAL")
    print("="*45)
    
    for clave, datos in CATALOGO_POKEMON.items():
        print(f"[{clave}] {datos['nombre']} | Tipo: {datos['tipo']} | HP: {datos['hp_maximo']} | EP: {datos['energia_maxima']}")
    
    print("="*45 + "\n")

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
        
        if valor < 0:
            self.__ep = 0
        elif valor > self.__ep_max:
            self.__ep = self.__ep_max
        else:
            self.__ep = valor

    @property
    def hp_max(self): return self.__hp_max

    @property
    def ep_max(self): return self.__ep_max


    def esta_con_vida(self):
        """Retorna True si el Pokémon tiene HP mayor a 0."""
        return self.hp > 0

    def mostrar_interfaz(self, es_rival=False):
        """Dibuja la interfaz visual de salud y energía en consola."""
        ancho = 40
        tag = "[RIVAL]" if es_rival else "[TU POKÉMON]"
        
        def generar_barra(actual, maximo, color_bloque="▰"):
            if maximo == 0: return "▱" * 10
            bloques = int((actual / maximo) * 10)
            return color_bloque * bloques + "▱" * (10 - bloques)

        barra_hp = generar_barra(self.hp, self.hp_max)
        barra_ep = generar_barra(self.ep, self.ep_max)
        
